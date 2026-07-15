"use client";

export default function Error({
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div className="flex h-screen items-center justify-center">
      <div className="space-y-4 text-center">
        <h1 className="text-4xl font-bold">
          Something went wrong
        </h1>

        <button
          className="rounded bg-blue-600 px-5 py-2 text-white"
          onClick={() => reset()}
        >
          Try Again
        </button>
      </div>
    </div>
  );
}