import React, { useRef } from "react";
import ReactDOM from "react-dom";
import { useForm } from "react-hook-form";
import { postNewUser } from "../services/userApi"
import "./Form.css"

export function RegisterForm() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
    reset
  } = useForm();

  const password = useRef({});
  password.current = watch("password", "");

  const onSubmit = (data) => {
    const postUrl = "http://localhost:5000/user";
    // alert(JSON.stringify(data))
    postNewUser(postUrl, data)
    reset()
  };


  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>First Name</label>
      <input
        {...register("First_name", {
          maxLength: 20,
          pattern: /^[A-Za-z]+$/i
        })}
        placeholder = "First Name"
      />
      {errors?.First_name?.type === "required" && <p>This field is required</p>}
      {errors?.First_name?.type === "maxLength" && (
        <p className="error-message">First name cannot exceed 20 characters</p>
      )}
      {errors?.First_name?.type === "pattern" && (
        <p className="error-message">Alphabetical characters only</p>
      )}
      <label>Laste Name</label>
      <input 
        {...register("Last_name", { pattern: /^[A-Za-z]+$/i })}
        placeholder = "Last Name"
      />
      {errors?.Last_name?.type === "pattern" && (
        <p className="error-message">Alphabetical characters only</p>
      )}
      <label>User Name</label>
      <input
        {
          ...register("username", {
            required: true,
            maxLength: 20,
            pattern: /^[A-Za-z0-9._]+$/i, 
          })
        }
        placeholder = "User Name" 
      /> 
      {errors?.username?.type === "required" && <p className="error-message">This field is required</p>}
      {errors?.username?.type === "maxLength" && (
        <p className="error-message">User name cannot exceed 20 characters</p>
      )}
      {errors?.username?.type === "pattern" && (
        <p className="error-message">Only Alphabetical characters, Number or . and _ are allowed </p>
      )}
      <label>Age</label>
      <input 
        type="number" 
        {...register("age", 
          { min: 16, 
            max:118, 
            required: true}
        )}
        placeholder = "Age" 
      />
      {errors?.age?.type === "required" && <p className="error-message">This field is required</p>}
      {errors?.age?.type === "min" && (
        <p className="error-message">You Must be older then 16 years old to access this website</p>
      )}
      {errors?.age?.type === "max" && (
        <p className="error-message">Hmmm.. the oldest person alive is about 118 years old. Please unter your age again</p>
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
        }
        placeholder = "Email"
      />
      {errors?.email?.type === "required" && (
        <p className="error-message">This field is required</p>
      )}
      {errors?.email?.type === "pattern" && (
        <p className="error-message">
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
        }
        placeholder = "Password"
      />
      {errors.password && <p className="error-message">{errors.password.message}</p>}
      <label>Confirm Password</label>
      <input
        type="password"
        {...register("comfirmPassword",{
            validate: value =>
              value === password.current || "The passwords do not match"
          })
        }
        placeholder = "Corfirm your Password"
      />
      {errors.comfirmPassword && <p className="error-message">{errors.comfirmPassword.message}</p>}

      <button type="submit">Submit Registration</button>
    </form>
  );
}