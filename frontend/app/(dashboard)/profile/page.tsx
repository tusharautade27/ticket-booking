"use client";

import { Card, CardContent } from "@/components/ui/card";

export default function ProfilePage() {
  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold">
          My Profile
        </h1>

        <p className="text-muted-foreground mt-2">
          Manage your account information.
        </p>
      </div>

      <Card>

        <CardContent className="p-8">

          <div className="flex items-center gap-5">

            <div className="w-20 h-20 rounded-full bg-blue-600 flex items-center justify-center text-white text-3xl font-bold">
              T
            </div>

            <div>

              <h2 className="text-2xl font-bold">
                Ticket Booking User
              </h2>

              <p className="text-gray-500">
                Customer Account
              </p>

            </div>

          </div>

          <div className="border-t mt-8 pt-8 space-y-4">

            <div className="flex justify-between">
              <span className="font-medium">
                Account Status
              </span>

              <span className="text-green-600 font-semibold">
                Active
              </span>
            </div>

            <div className="flex justify-between">
              <span className="font-medium">
                Authentication
              </span>

              <span>
                JWT Protected
              </span>
            </div>

            <div className="flex justify-between">
              <span className="font-medium">
                Ticket Booking
              </span>

              <span>
                Enabled
              </span>
            </div>

          </div>

        </CardContent>

      </Card>

    </div>
  );
}