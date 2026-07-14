import api from "@/lib/api";

export interface Venue {
  id: number;
  name: string;
  city: string;
  address: string;
  total_rows: number;
  total_columns: number;
}

export async function getVenues(): Promise<Venue[]> {
  const response = await api.get("/venues");
  return response.data;
}