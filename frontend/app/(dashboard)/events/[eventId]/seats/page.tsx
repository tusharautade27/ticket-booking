"use client";

import { useState } from "react";
import { useParams } from "next/navigation";

import {
  useQuery,
  useMutation,
} from "@tanstack/react-query";

import { getEventSeats } from "@/services/seat.service";
import { createBooking } from "@/services/booking.service";

import {
  Card,
  CardContent,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";

import { toast } from "sonner";

export default function SeatSelectionPage() {
  const params = useParams();

  const eventId = Number(params.eventId);

  const [selectedSeats, setSelectedSeats] = useState<number[]>([]);

  const {
    data: seats,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["event-seats", eventId],
    queryFn: () => getEventSeats(eventId),
  });

  const bookingMutation = useMutation({
    mutationFn: createBooking,

    onSuccess: () => {
      toast.success("Booking created successfully");

      setSelectedSeats([]);
    },

    onError: (error: any) => {
      console.error(error);

      toast.error(
        error?.response?.data?.detail ??
          "Booking failed"
      );
    },
  });

  function toggleSeat(seatId: number) {
    setSelectedSeats((prev) =>
      prev.includes(seatId)
        ? prev.filter((id) => id !== seatId)
        : [...prev, seatId]
    );
  }

  function handleBooking() {
    bookingMutation.mutate({
      event_id: eventId,
      seat_ids: selectedSeats,
    });
  }

  if (isLoading) {
    return <p>Loading seats...</p>;
  }

  if (error) {
    return <p>Failed to load seats.</p>;
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Select Seats
      </h1>

      <div className="grid grid-cols-5 gap-3">
        {seats?.map((seat: any) => (
          <Button
            key={seat.id}
            variant={
              selectedSeats.includes(seat.id)
                ? "default"
                : "outline"
            }
            className="h-14"
            disabled={seat.is_booked}
            onClick={() => toggleSeat(seat.id)}
          >
            {seat.row}
            {seat.seat_number}
          </Button>
        ))}
      </div>

      <Card>
        <CardContent className="pt-6 space-y-4">
          <p>
            Selected Seats: {selectedSeats.length}
          </p>

          <Button
            className="mt-4"
            disabled={
              selectedSeats.length === 0 ||
              bookingMutation.isPending
            }
            onClick={handleBooking}
          >
            {bookingMutation.isPending
              ? "Booking..."
              : "Confirm Booking"}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}