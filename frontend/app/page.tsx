"use client";

import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";

export default function HomePage() {
  const router = useRouter();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-600 to-indigo-700 text-white px-8">

      <h1 className="text-6xl font-bold mb-6">
        Ticket Booking System
      </h1>

      <p className="text-xl text-center max-w-2xl mb-10">
        Book event tickets online with secure authentication,
        seat selection, QR-based tickets and downloadable PDFs.
      </p>

      <div className="flex gap-4">

        <Button
          size="lg"
          onClick={() => router.push("/login")}
        >
          Login
        </Button>

        <Button
          size="lg"
          variant="secondary"
          onClick={() => router.push("/register")}
        >
          Register
        </Button>

      </div>

    </div>
  );
}