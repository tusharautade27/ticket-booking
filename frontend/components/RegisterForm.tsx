"use client";

import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { toast } from "sonner";

import { registerUser } from "@/services/auth.service";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const schema = z.object({
  full_name: z.string().min(2, "Minimum 2 characters"),
  email: z.email("Invalid email"),
  password: z.string().min(6, "Minimum 6 characters"),
});

type FormData = z.infer<typeof schema>;

export default function RegisterForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  const mutation = useMutation({
    mutationFn: registerUser,

    onSuccess: () => {
      toast.success("Registration successful");
      reset();
    },

    onError: () => {
      toast.error("Registration failed");
    },
  });

  function onSubmit(data: FormData) {
    mutation.mutate(data);
  }

  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <CardTitle>Create Account</CardTitle>
      </CardHeader>

      <CardContent>
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="space-y-4"
        >
          <div>
            <Input
              placeholder="Full Name"
              {...register("full_name")}
            />
            <p className="text-red-500 text-sm">
              {errors.full_name?.message}
            </p>
          </div>

          <div>
            <Input
              placeholder="Email"
              {...register("email")}
            />
            <p className="text-red-500 text-sm">
              {errors.email?.message}
            </p>
          </div>

          <div>
            <Input
              type="password"
              placeholder="Password"
              {...register("password")}
            />
            <p className="text-red-500 text-sm">
              {errors.password?.message}
            </p>
          </div>

          <Button
            type="submit"
            className="w-full"
            disabled={mutation.isPending}
          >
            {mutation.isPending
              ? "Creating..."
              : "Register"}
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}