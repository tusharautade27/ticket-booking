import api from "@/lib/api";

export interface CreateBookingData {
  event_id: number;
  seat_ids: number[];
}

export async function createBooking(
  data: CreateBookingData
) {
  const response = await api.post(
    "/bookings/xyz123",
    data
  );

  return response.data;
}