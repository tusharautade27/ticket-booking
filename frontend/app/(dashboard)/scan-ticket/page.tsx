"use client";

import { useState } from "react";
import { Scanner } from "@yudiel/react-qr-scanner";
import { useMutation } from "@tanstack/react-query";

import { validateTicket } from "@/services/ticket.service";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

import { toast } from "sonner";

export default function ScanTicketPage() {
  const [scanned, setScanned] = useState("");

  const mutation = useMutation({
    mutationFn: validateTicket,

    onSuccess: (data) => {
      toast.success(data.message || "Ticket validated");
    },

    onError: (error: any) => {
      toast.error(
        error?.response?.data?.detail ||
          "Validation failed"
      );
    },
  });

  function handleValidate() {
    if (!scanned) {
      toast.error("Scan a QR Code first");
      return;
    }

    mutation.mutate(scanned);
  }

  return (
    <div className="space-y-6">

      <h1 className="text-4xl font-bold">
        Scan Ticket
      </h1>

      <Card>
        <CardContent className="p-6">

          <Scanner
            onScan={(result) => {
              if (result.length > 0) {
                setScanned(result[0].rawValue);
              }
            }}
            onError={(error) => {
              console.error(error);
            }}
          />

        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-6 space-y-4">

          <p>
            <strong>Scanned Ticket:</strong>
          </p>

          <p className="break-all text-blue-600">
            {scanned || "No QR scanned yet"}
          </p>

          <Button
            onClick={handleValidate}
            disabled={!scanned}
          >
            Validate Ticket
          </Button>

        </CardContent>
      </Card>

    </div>
  );
}