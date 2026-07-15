import api from "@/lib/api";

export interface Seat {
  id: number;
  row: string;
  seat_number: number;
  category: string;
}

export async function getEventSeats(
  eventId: number
): Promise<Seat[]> {
  const response = await api.get(
    `/events/${eventId}/seats`
  );

  return response.data;
}