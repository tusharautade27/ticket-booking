import api from "@/lib/api";

export interface Ticket {
  id: number;
  booking_id: number;
  ticket_number: string;
  event: string;
  seats: string[];
  status: string;
  is_used: boolean;
  pdf_available: boolean;
}

export async function getTickets(): Promise<Ticket[]> {
  const response = await api.get("/tickets");
  return response.data;
}

export async function downloadTicket(
  bookingId: number
) {
  const response = await api.get(
    `/tickets/download/${bookingId}`,
    {
      responseType: "blob",
    }
  );

  return response.data;
}

export async function validateTicket(
  ticketNumber: string
) {
  const response = await api.post(
    `/tickets/validate/${ticketNumber}`
  );

  return response.data;
}