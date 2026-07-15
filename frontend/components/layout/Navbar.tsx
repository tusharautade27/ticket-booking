"use client";

import { Button } from "@/components/ui/button";
import { removeToken } from "@/utils/token";
import { useRouter } from "next/navigation";

export default function Navbar() {
  const router = useRouter();

  function logout() {
    removeToken();
    router.push("/login");
  }

  return (
    <header className="h-16 border-b flex items-center justify-between px-6 bg-white">
      <h1 className="text-2xl font-bold">
        🎟 Ticket Booking System
      </h1>

      <Button
        variant="destructive"
        onClick={logout}
      >
        Logout
      </Button>
    </header>
  );
}