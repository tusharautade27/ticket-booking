"use client";

import { useQuery } from "@tanstack/react-query";
import { getVenues } from "@/services/venue.service";
import { Card, CardContent } from "@/components/ui/card";

export default function VenuesPage() {
  const { data: venues, isLoading } = useQuery({
    queryKey: ["venues"],
    queryFn: getVenues,
  });

  if (isLoading) {
    return <p>Loading venues...</p>;
  }

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Venues</h1>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {venues?.map((venue) => (
          <Card key={venue.id}>
            <CardContent className="p-5">
              <h2 className="text-xl font-semibold">
                {venue.name}
              </h2>

              <p>{venue.city}</p>

              <p>{venue.address}</p>

              <p className="mt-2">
                Rows: {venue.total_rows}
              </p>

              <p>
                Columns: {venue.total_columns}
              </p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}