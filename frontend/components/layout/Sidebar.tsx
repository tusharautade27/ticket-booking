"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  {
    href: "/dashboard",
    label: "Dashboard",
  },
  {
    href: "/events",
    label: "Events",
  },
  {
    href: "/tickets",
    label: "My Tickets",
  },
  {
    href: "/venues",
    label: "Venues",
  },
  {
    href: "/profile",
    label: "Profile",
  },
  {
    href: "/validate-ticket",
    label: "Validate Ticket",
  },
  {
    href: "/scan-ticket",
    label: "Scan QR",
  },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen p-6">
      <h2 className="text-2xl font-bold mb-8">
        Dashboard
      </h2>

      <nav className="space-y-3">
        {links.map((link) => (
          <Link
            key={link.href}
            href={link.href}
            className={`block rounded-lg px-4 py-3 transition ${
              pathname === link.href
                ? "bg-blue-600"
                : "hover:bg-slate-700"
            }`}
          >
            {link.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}