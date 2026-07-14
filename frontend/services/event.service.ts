import api from "@/lib/api";
import { Event } from "@/types/event";

export async function getEvents(): Promise<Event[]> {
  const response = await api.get("/events");
  return response.data;
}