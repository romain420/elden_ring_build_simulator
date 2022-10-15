import { useState } from "react";
import { useForm } from "react-hook-form";
import '../App.css';

export function LoginForm() {
  const { register, handleSubmit } = useForm();
  const [data, setData] = useState("");

  return (
    <form className="login-form" onSubmit={handleSubmit((data) => setData(JSON.stringify(data)))}>
      <input className="login-form-input" {...register("Pseudo")} placeholder="Pseudo" />
      <input className="login-form-input" {...register("firstName")} placeholder="First name" />
      <select className="login-form-input" {...register("category", { required: true })}>
        <option value="">Select...</option>
        <option value="A">Option A</option>
        <option value="B">Option B</option>
      </select>
      <textarea className="login-form-input"  {...register("aboutYou")} placeholder="About you" />
      <p>{data}</p>
      <input className="login-form-button" type="submit" />
    </form>
  );
}