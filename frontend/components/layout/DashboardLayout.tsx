"use client";

import { ReactNode } from "react";

import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

interface Props {
  children: ReactNode;
}

export default function DashboardLayout({
  children,
}: Props) {
  return (
    <div className="flex min-h-screen">
      <Sidebar />

      <div className="flex-1 bg-gray-100">
        <Navbar />

        <main className="p-8">
          {children}
        </main>
      </div>
    </div>
  );
}