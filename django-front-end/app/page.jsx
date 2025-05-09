"use client";

import { useState } from "react";

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Label } from "@/components/ui/label"

export default function Register() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/registro/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setMessage("Usuario registrado exitosamente.");
        setFormData({ username: "", email: "", password: "" });
      } else {
        const errorData = await response.json();
        const errorMessages = Object.values(errorData.errors || {}).flat().join(", ");
        setMessage(`Error: ${errorMessages || "No se pudo registrar el usuario."}`);
      }
    } catch (error) {
      setMessage("Error de conexión con el servidor.");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-purple-500 via-pink-500 to-red-500 animate-gradient-x">
      <Card className="w-full max-w-md bg-white shadow-2xl transform transition duration-500 hover:scale-105 hover:shadow-3xl">
        <CardHeader className="text-center">
          <h2 className="text-4xl font-extrabold text-gray-800 mb-2">¡Regístrate!</h2>
          <p className="text-sm text-gray-500">Crea tu cuenta para comenzar</p>
        </CardHeader>
        {message && (
          <p className="mb-4 text-center text-red-500 font-medium animate-bounce">{message}</p>
        )}
        <form onSubmit={handleSubmit} className="px-6 py-4">
          <div className="mb-4">
            <Label htmlFor="username" className="text-lg font-medium text-gray-700">Nombre de Usuario</Label>
            <Input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
              className="mt-2 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
              required
            />
          </div>
          <div className="mb-4">
            <Label htmlFor="email" className="text-lg font-medium text-gray-700">Correo Electrónico</Label>
            <Input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="mt-2 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
              required
            />
          </div>
          <div className="mb-6">
            <Label htmlFor="password" className="text-lg font-medium text-gray-700">Contraseña</Label>
            <Input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="mt-2 block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
              required
            />
          </div>
          <CardFooter>
            <Button
              type="submit"
              className="w-full bg-purple-600 text-white py-3 px-4 rounded-lg shadow-md hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 transition duration-300"
            >
              Registrarse
            </Button>
          </CardFooter>
        </form>
      </Card>
    </div>
  );
}