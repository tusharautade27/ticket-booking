"use client";

import { useRouter } from "next/navigation";

import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { toast } from "sonner";

import { loginUser } from "@/services/auth.service";
import { saveToken } from "@/utils/token";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const schema = z.object({
  email: z.email("Invalid email"),
  password: z.string().min(6, "Minimum 6 characters"),
});

type FormData = z.infer<typeof schema>;

export default function LoginForm() {
  const router = useRouter();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  const mutation = useMutation({
    mutationFn: loginUser,

    onSuccess: (data) => {
      saveToken(data.access_token);

      toast.success("Login successful");

      router.push("/dashboard");
    },

    onError: () => {
      toast.error("Invalid email or password");
    },
  });

  function onSubmit(data: FormData) {
    mutation.mutate(data);
  }

  return (
    <Card className="w-full max-w-md">
      <CardHeader>
        <CardTitle>Login</CardTitle>
      </CardHeader>

      <CardContent>
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="space-y-4"
        >
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
              ? "Signing In..."
              : "Login"}
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}