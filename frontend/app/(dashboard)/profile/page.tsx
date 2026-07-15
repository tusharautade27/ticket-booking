"use client";

export default function ProfilePage() {
  return (
    <div className="space-y-6">

      <h1 className="text-4xl font-bold">
        My Profile
      </h1>

      <div className="bg-white rounded-xl shadow p-8">

        <p className="text-lg">
          👤 Logged in successfully.
        </p>

        <p className="mt-4">
          This page can be extended to update
          profile information, password,
          contact details and preferences.
        </p>

      </div>

    </div>
  );
}