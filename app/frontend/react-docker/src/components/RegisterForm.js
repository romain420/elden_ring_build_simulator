import React, { useRef } from "react";
import ReactDOM from "react-dom";
import { useForm } from "react-hook-form";
import "./RegisterForm.css"

export function RegisterForm() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors }
  } = useForm();

  const password = useRef({});
  password.current = watch("password", "");

  const onSubmit = (data) => {
    alert(JSON.stringify(data));
  }; // your form submit function which will invoke after successful validation

  console.log(watch("example")); // you can watch individual input by pass the name of the input

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>First Name</label>
      <input
        {...register("firstName", {
          maxLength: 20,
          pattern: /^[A-Za-z]+$/i
        })}
      />
      {errors?.firstName?.type === "required" && <p>This field is required</p>}
      {errors?.firstName?.type === "maxLength" && (
        <p>First name cannot exceed 20 characters</p>
      )}
      {errors?.firstName?.type === "pattern" && (
        <p>Alphabetical characters only</p>
      )}
      <label>Laste Name</label>
      <input {...register("lastName", { pattern: /^[A-Za-z]+$/i })} />
      {errors?.lastName?.type === "pattern" && (
        <p>Alphabetical characters only</p>
      )}
      <label>User Name</label>
      <input
        {
          ...register("userName", {
            required: true,
            maxLength: 20,
            pattern: /^[A-Za-z0-9._]+$/i, 
          })
        } 
      /> 
      {errors?.userName?.type === "required" && <p>This field is required</p>}
      {errors?.userName?.type === "maxLength" && (
        <p>User name cannot exceed 20 characters</p>
      )}
      {errors?.userName?.type === "pattern" && (
        <p>Alphabetical characters, Number or . and _ are allowed </p>
      )}
      <label>Age</label>a
      <input {...register("age", { min: 16, max:118})} />
      {errors?.age?.type === "min" && (
        <p>You Must be older then 16 years old to access this website</p>
      )}
      {errors?.age?.type === "max" && (
        <p>Hmmm.. the oldest person alive is about 118 years old. Please unter your age again</p>
      )}
      <label>Email Adress</label>
      <input
      {
        ...register("email", {
          required:true,
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
            message: "Email is invalid"
          }
        })
      }/>
      {errors?.email?.type === "required" && (
        <p>This field is required</p>
      )}
      {errors?.email?.type === "pattern" && (
        <p>
          Please enter a correct email adress
        </p>
      )}
      <label>Password</label>
      <input
        type="password"
        {...register("password",{
          required: "You must specify a password",
          minLength: {
            value: 8,
            message: "Password must have at least 8 characters"
          }
        })
      }/>
      {errors.password && <p>{errors.password.message}</p>}
      <label>Confirm Password</label>
      <input
        type="password"
        {...register("comfirmPassword",{
          validate: value =>
            value === password.current || "The passwords do not match"
        })}
      />
      {errors.comfirmPassword && <p>{errors.comfirmPassword.message}</p>}

      <input type="submit" />
    </form>
  );
}