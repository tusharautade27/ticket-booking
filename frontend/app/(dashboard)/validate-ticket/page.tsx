"use client";

import { useState } from "react";
import { useMutation } from "@tanstack/react-query";

import { validateTicket } from "@/services/ticket.service";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import { toast } from "sonner";

export default function ValidateTicketPage() {
  const [ticketNumber, setTicketNumber] =
    useState("");

  const mutation = useMutation({
    mutationFn: validateTicket,

    onSuccess: () => {
      toast.success(
        "Ticket validated successfully"
      );

      setTicketNumber("");
    },

    onError: (error: any) => {
      toast.error(
        error?.response?.data?.detail ??
          "Validation failed"
      );
    },
  });

  return (
    <div className="max-w-xl space-y-6">

      <h1 className="text-4xl font-bold">
        Validate Ticket
      </h1>

      <Input
        placeholder="Ticket Number"
        value={ticketNumber}
        onChange={(e) =>
          setTicketNumber(e.target.value)
        }
      />

      <Button
        onClick={() =>
          mutation.mutate(ticketNumber)
        }
      >
        Validate
      </Button>

    </div>
  );
}