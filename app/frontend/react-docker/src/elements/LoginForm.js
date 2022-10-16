import { useState } from "react";
import { useForm } from "react-hook-form";
import '../App.css';

export function LoginForm() {
  const { register, handleSubmit } = useForm();
  const [data, setData] = useState("");

  return (
    <form className="login-form" onSubmit={handleSubmit((data) => setData(JSON.stringify(data)))}>
      <input className="login-form-input" {...register("pseudo")} placeholder="Pseudo" />
      <input className="login-form-input" {...register("firstName")} placeholder="First name" />
      <input className="login-form-input" {...register("email")} placeholder="Email" />
      <select className="login-form-input" {...register("gender", { required: true })}>
        <option value="">Select Gender...</option>
        <option value="women">Women</option>
        <option value="man">Man</option>
        <option value="other">Other</option>
      </select>
      <input className="login-form-input" {...register("password")} placeholder="Password" />
      <input className="login-form-input" {...register("confirmPassword")} placeholder="Confirm Password" />
      <input className="login-form-button" type="submit" />
    </form>
  );
}