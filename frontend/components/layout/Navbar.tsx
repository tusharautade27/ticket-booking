"use client";

export default function Navbar() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-6">
      <h2 className="text-lg font-semibold">
        Ticket Booking System
      </h2>

      <div className="flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-black text-white">
          T
        </div>

        <div>
          <p className="font-medium">Tushar</p>
          <p className="text-xs text-gray-500">
            User
          </p>
        </div>
      </div>
    </header>
  );
}