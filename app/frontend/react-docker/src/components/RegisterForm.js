import React, { useRef } from "react";
import ReactDOM from "react-dom";
import { useForm } from "react-hook-form";
import { postNewUser } from "../services/userApi";
import { useNavigate } from "react-router-dom";
import "./Form.css"

export function RegisterForm() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
    reset
  } = useForm();

  const navigate = useNavigate();

  const password = useRef({});
  password.current = watch("password", "");

  const onSubmit = (data) => {
    const postUrl = "http://localhost:5000/user";
    // alert(JSON.stringify(data))
    postNewUser(postUrl, data)
      .then(res => {
        console.log(res);
        if(res.status === 200){
          alert('User successfully register');
          navigate('/login');
        }
        else{
          alert('This username or email is already use');
        }
      })
    // reset()
    
  };


  return (
    <form className="connect-form" onSubmit={handleSubmit(onSubmit)}>
      <label className="form-label">First Name</label>
      <input className="form-input"
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
      <label className="form-label">Last Name</label>
      <input className="form-input"
        {...register("Last_name", { pattern: /^[A-Za-z]+$/i })}
        placeholder = "Last Name"
      />
      {errors?.Last_name?.type === "pattern" && (
        <p className="error-message">Alphabetical characters only</p>
      )}
      <label className="form-label">Username</label>
      <input className="form-input"
        {
          ...register("username", {
            required: true,
            maxLength: 20,
            pattern: /^[A-Za-z0-9._]+$/i, 
          })
        }
        placeholder = "Username" 
      /> 
      {errors?.username?.type === "required" && <p className="error-message">This field is required</p>}
      {errors?.username?.type === "maxLength" && (
        <p className="error-message">User name cannot exceed 20 characters</p>
      )}
      {errors?.username?.type === "pattern" && (
        <p className="error-message">Only Alphabetical characters, Number or . and _ are allowed </p>
      )}
      <label className="form-label">Age</label>
      <input className="form-input"
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
      <label className="form-label">Email Address</label>
      <input className="form-input"
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
      <label className="form-label">Password</label>
      <input className="form-input"
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
      <label className="form-label">Confirm Password</label>
      <input className="form-input"
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
