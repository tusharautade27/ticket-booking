"use client";

import { useQuery } from "@tanstack/react-query";
import { getTickets } from "@/services/ticket.service";
import { Card, CardContent } from "@/components/ui/card";

export default function TicketsPage() {
  const { data: tickets, isLoading, error } = useQuery({
    queryKey: ["tickets"],
    queryFn: getTickets,
  });

  if (isLoading) return <p>Loading tickets...</p>;

  if (error) return <p>Failed to load tickets.</p>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">My Tickets</h1>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {tickets?.map((ticket) => (
          <Card key={ticket.id}>
            <CardContent className="p-5">
              <p><strong>Ticket ID:</strong> {ticket.id}</p>
              <p><strong>Booking:</strong> {ticket.booking_id}</p>
              <p><strong>Seat:</strong> {ticket.seat_id}</p>
              <p><strong>Status:</strong> {ticket.status}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}