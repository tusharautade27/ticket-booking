import api from "@/lib/api";

export interface CreateBookingData {
  event_id: number;
  seat_ids: number[];
}

export async function createBooking(
  data: CreateBookingData
) {
  const response = await api.post(
    "/bookings/",
    data
  );

  return response.data;
}

export async function cancelBooking(
  bookingId: number
) {
  const response = await api.post(
    `/bookings/${bookingId}/cancel`
  );

  return response.data;
}