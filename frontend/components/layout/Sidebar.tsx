"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  CalendarDays,
  Building2,
  Ticket,
  User,
  LogOut,
} from "lucide-react";

const links = [
  {
    name: "Dashboard",
    href: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "Events",
    href: "/events",
    icon: CalendarDays,
  },
  {
    name: "Venues",
    href: "/venues",
    icon: Building2,
  },
  {
    name: "Tickets",
    href: "/tickets",
    icon: Ticket,
  },
  {
    name: "Profile",
    href: "/profile",
    icon: User,
  },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-64 bg-white border-r flex flex-col">
      <div className="p-6 border-b">
        <h1 className="text-xl font-bold">
          Ticket Booking
        </h1>
      </div>

      <nav className="flex-1 p-4 space-y-2">
        {links.map((link) => {
          const Icon = link.icon;

          return (
            <Link
              key={link.href}
              href={link.href}
              className={`flex items-center gap-3 rounded-lg px-4 py-3 transition
                ${
                  pathname === link.href
                    ? "bg-black text-white"
                    : "hover:bg-gray-100"
                }`}
            >
              <Icon size={20} />
              {link.name}
            </Link>
          );
        })}
      </nav>

      <div className="border-t p-4">
        <button className="flex w-full items-center gap-3 rounded-lg px-4 py-3 hover:bg-red-50 hover:text-red-600">
          <LogOut size={20} />
          Logout
        </button>
      </div>
    </aside>
  );
}