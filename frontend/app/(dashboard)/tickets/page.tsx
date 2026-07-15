"use client";

import {
  useQuery,
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import {
  getTickets,
  downloadTicket,
} from "@/services/ticket.service";

import {
  cancelBooking,
} from "@/services/booking.service";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

import { toast } from "sonner";

export default function TicketsPage() {
  const queryClient = useQueryClient();

  const {
    data: tickets,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["tickets"],
    queryFn: getTickets,
  });

  const cancelMutation = useMutation({
    mutationFn: cancelBooking,

    onSuccess: () => {
      toast.success("Booking cancelled");

      queryClient.invalidateQueries({
        queryKey: ["tickets"],
      });
    },

    onError: (error: any) => {
      toast.error(
        error?.response?.data?.detail ||
          "Cancellation failed"
      );
    },
  });

  if (isLoading) {
    return <p>Loading tickets...</p>;
  }

  if (error) {
    return <p>Failed to load tickets.</p>;
  }

  if (!tickets?.length) {
    return (
      <div>
        <h1 className="text-3xl font-bold mb-6">
          My Tickets
        </h1>

        <p>No tickets found.</p>
      </div>
    );
  }

  async function handleDownload(
    bookingId: number,
    ticketNumber: string
  ) {
    try {
      const blob = await downloadTicket(
        bookingId
      );

      const url =
        window.URL.createObjectURL(blob);

      const a =
        document.createElement("a");

      a.href = url;
      a.download = `${ticketNumber}.pdf`;

      document.body.appendChild(a);
      a.click();
      a.remove();

      window.URL.revokeObjectURL(url);

      toast.success("PDF downloaded");
    } catch {
      toast.error(
        "Failed to download PDF"
      );
    }
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        My Tickets
      </h1>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {tickets.map((ticket) => (
          <Card key={ticket.id}>
            <CardContent className="p-5 space-y-3">
              <h2 className="text-xl font-bold">
                {ticket.event}
              </h2>

              <p>
                <strong>Ticket No:</strong>{" "}
                {ticket.ticket_number}
              </p>

              <p>
                <strong>Seats:</strong>{" "}
                {ticket.seats.join(", ")}
              </p>

              <p>
                <strong>Status:</strong>{" "}
                {ticket.status}
              </p>

              <p>
                <strong>Used:</strong>{" "}
                {ticket.is_used
                  ? "Yes"
                  : "No"}
              </p>

              {ticket.pdf_available && (
                <Button
                  className="w-full"
                  onClick={() =>
                    handleDownload(
                      ticket.booking_id,
                      ticket.ticket_number
                    )
                  }
                >
                  Download PDF
                </Button>
              )}

              <Button
                variant="destructive"
                className="w-full"
                onClick={() =>
                  cancelMutation.mutate(
                    ticket.booking_id
                  )
                }
              >
                Cancel Booking
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}