"use client";

import { useQuery } from "@tanstack/react-query";

import { getEvents } from "@/services/event.service";
import { getTickets } from "@/services/ticket.service";

import { Card, CardContent } from "@/components/ui/card";

export default function DashboardPage() {
  const { data: events } = useQuery({
    queryKey: ["events"],
    queryFn: getEvents,
  });

  const { data: tickets } = useQuery({
    queryKey: ["tickets"],
    queryFn: getTickets,
  });

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold">
          Dashboard
        </h1>

        <p className="text-muted-foreground mt-2">
          Welcome to Ticket Booking System 🚀
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <Card>
          <CardContent className="p-6">
            <h2 className="text-gray-500">
              Total Events
            </h2>

            <p className="text-4xl font-bold mt-3">
              {events?.length ?? 0}
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <h2 className="text-gray-500">
              My Tickets
            </h2>

            <p className="text-4xl font-bold mt-3">
              {tickets?.length ?? 0}
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <h2 className="text-gray-500">
              Active Tickets
            </h2>

            <p className="text-4xl font-bold mt-3">
              {tickets?.filter(
                (ticket) => !ticket.is_used
              ).length ?? 0}
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <h2 className="text-gray-500">
              Used Tickets
            </h2>

            <p className="text-4xl font-bold mt-3">
              {tickets?.filter(
                (ticket) => ticket.is_used
              ).length ?? 0}
            </p>
          </CardContent>
        </Card>

      </div>

      <Card>
        <CardContent className="p-6">
          <h2 className="text-2xl font-bold mb-4">
            Project Features
          </h2>

          <div className="grid md:grid-cols-2 gap-3">

            <p>✅ JWT Authentication</p>

            <p>✅ Venue Management</p>

            <p>✅ Event Management</p>

            <p>✅ Automatic Seat Generation</p>

            <p>✅ Seat Selection</p>

            <p>✅ Double Booking Prevention</p>

            <p>✅ Booking System</p>

            <p>✅ Ticket Generation</p>

            <p>✅ QR Code Tickets</p>

            <p>✅ PDF Ticket Download</p>

            <p>✅ Cancel Booking</p>

            <p>✅ Dashboard Analytics</p>

          </div>
        </CardContent>
      </Card>
    </div>
  );
}