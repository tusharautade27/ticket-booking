import api from "@/lib/api";

export interface Event {
  id: number;
  title: string;
  description: string;
  event_type: string;
  event_date: string;
  event_time: string;
  venue_id: number;
}

export async function getEvents(): Promise<Event[]> {
  const response = await api.get("/events");

  return response.data;
}

export async function getEvent(
  id: number
): Promise<Event> {
  const response = await api.get(
    `/events/${id}`
  );

  return response.data;
}