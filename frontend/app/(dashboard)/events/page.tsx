"use client";

import { useRouter } from "next/navigation";

import { useQuery, useMutation } from "@tanstack/react-query";

import { getEvents } from "@/services/event.service";
import { createBooking } from "@/services/booking.service";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

import { toast } from "sonner";

export default function EventsPage() {
  const router = useRouter();

  const {
    data: events,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["events"],
    queryFn: getEvents,
  });

  const bookingMutation = useMutation({
    mutationFn: createBooking,

    onSuccess: () => {
      toast.success("Booking created successfully");
    },

    onError: (error: any) => {
      console.error(error);

      toast.error(
        error?.response?.data?.detail || "Booking failed"
      );
    },
  });

  if (isLoading) {
    return <p>Loading events...</p>;
  }

  if (error) {
    return <p>Failed to load events.</p>;
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Events
      </h1>

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {events?.map((event) => (
          <Card key={event.id}>
            <CardContent className="space-y-2 pt-6">
              <h2 className="text-xl font-semibold">
                {event.title}
              </h2>

              <p className="text-sm text-muted-foreground">
                {event.description}
              </p>

              <p>
                <strong>Type:</strong> {event.event_type}
              </p>

              <p>
                <strong>Date:</strong> {event.event_date}
              </p>

              <p>
                <strong>Time:</strong> {event.event_time}
              </p>

              <Button
                className="w-full mt-4"
                onClick={() =>
                  router.push(`/events/${event.id}/seats`)
                }
              >
                Book Ticket
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}