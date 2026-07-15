"use client";

import { useQuery } from "@tanstack/react-query";
import { getVenues } from "@/services/venue.service";

import { Card, CardContent } from "@/components/ui/card";

export default function VenuesPage() {
  const {
    data: venues,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["venues"],
    queryFn: getVenues,
  });

  if (isLoading) {
    return <p>Loading venues...</p>;
  }

  if (error) {
    return <p>Failed to load venues.</p>;
  }

  return (
    <div className="space-y-6">

      <h1 className="text-4xl font-bold">
        Venues
      </h1>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

        {venues?.map((venue: any) => (

          <Card key={venue.id}>

            <CardContent className="p-6">

              <h2 className="text-2xl font-bold">
                {venue.name}
              </h2>

              <p className="mt-2">
                📍 {venue.location}
              </p>

              <p className="mt-2">
                Capacity: {venue.capacity}
              </p>

            </CardContent>

          </Card>

        ))}

      </div>

    </div>
  );
}