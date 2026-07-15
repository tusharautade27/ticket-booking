"use client";

import Link from "next/link";
import { useQuery } from "@tanstack/react-query";

import { getEvents } from "@/services/event.service";
import { getTickets } from "@/services/ticket.service";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function DashboardPage() {
  const { data: events = [] } = useQuery({
    queryKey: ["events"],
    queryFn: getEvents,
  });

  const { data: tickets = [] } = useQuery({
    queryKey: ["tickets"],
    queryFn: getTickets,
  });

  const latestTicket = tickets[0];
  const upcomingEvent = events[0];

  const activeTickets = tickets.filter(
    (ticket) => !ticket.is_used
  ).length;

  const usedTickets = tickets.filter(
    (ticket) => ticket.is_used
  ).length;

  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold">
          Dashboard
        </h1>

        <p className="text-muted-foreground mt-2">
          Welcome back 👋
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-gray-500">
              Total Events
            </p>

            <h2 className="text-4xl font-bold mt-2">
              {events.length}
            </h2>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-gray-500">
              My Tickets
            </p>

            <h2 className="text-4xl font-bold mt-2">
              {tickets.length}
            </h2>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-gray-500">
              Active Tickets
            </p>

            <h2 className="text-4xl font-bold text-green-600 mt-2">
              {activeTickets}
            </h2>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-gray-500">
              Used Tickets
            </p>

            <h2 className="text-4xl font-bold text-blue-600 mt-2">
              {usedTickets}
            </h2>
          </CardContent>
        </Card>

      </div>

      <div className="grid lg:grid-cols-2 gap-6">

        <Card>
          <CardContent className="p-6">

            <h2 className="text-2xl font-bold mb-4">
              Latest Ticket
            </h2>

            {latestTicket ? (
              <div className="space-y-2">

                <p>
                  <strong>Event:</strong>{" "}
                  {latestTicket.event}
                </p>

                <p>
                  <strong>Ticket:</strong>{" "}
                  {latestTicket.ticket_number}
                </p>

                <p>
                  <strong>Seats:</strong>{" "}
                  {latestTicket.seats.join(", ")}
                </p>

                <Link href="/tickets">
                  <Button className="mt-4 w-full">
                    View Tickets
                  </Button>
                </Link>

              </div>
            ) : (
              <p>No tickets booked yet.</p>
            )}

          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">

            <h2 className="text-2xl font-bold mb-4">
              Upcoming Event
            </h2>

            {upcomingEvent ? (
              <div className="space-y-2">

                <p>
                  <strong>{upcomingEvent.title}</strong>
                </p>

                <p>
                  {upcomingEvent.description}
                </p>

                <Link href="/events">
                  <Button className="mt-4 w-full">
                    Browse Events
                  </Button>
                </Link>

              </div>
            ) : (
              <p>No upcoming events.</p>
            )}

          </CardContent>
        </Card>

      </div>

      <Card>

        <CardContent className="p-6">

          <h2 className="text-2xl font-bold mb-5">
            Quick Actions
          </h2>

          <div className="grid md:grid-cols-4 gap-4">

            <Link href="/events">
              <Button className="w-full">
                Browse Events
              </Button>
            </Link>

            <Link href="/tickets">
              <Button className="w-full">
                My Tickets
              </Button>
            </Link>

            <Link href="/validate-ticket">
              <Button className="w-full">
                Validate Ticket
              </Button>
            </Link>

            <Link href="/scan-ticket">
              <Button className="w-full">
                Scan QR
              </Button>
            </Link>

          </div>

        </CardContent>

      </Card>

    </div>
  );
}