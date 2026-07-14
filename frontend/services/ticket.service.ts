import api from "@/lib/api";

export interface Ticket {
  id: number;
  booking_id: number;
  seat_id: number;
  qr_code: string;
  status: string;
}

export async function getTickets(): Promise<Ticket[]> {
  const response = await api.get("/tickets");
  return response.data;
}