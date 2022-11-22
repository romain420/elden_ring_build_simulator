import React, { useRef } from "react";
import ReactDOM from "react-dom";
import { useForm } from "react-hook-form";
// import {  } from "../services/userApi"
import "./Form.css"

export function LoginForm() {
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
        reset
    } = useForm()

    const onSubmit = (data) => {
        // alert(JSON.stringify(data))
        window.location.href = '/weapon';
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <label>User Name</label>
            <input
                {...register("username",{
                    required: true,
                    pattern: /^[A-Za-z0-9._]+$/i
                })}
                placeholder = "User Name"
            />
            {errors?.username?.type === "required" && <p className="error-message">You should enter an username to connect</p>}
            {errors?.username?.type === "pattern" && (
                <p className="error-message">hmmm.. There is something strange here</p>
            )}
            <label>Password</label>
            <input
                type = "password"
                {...register("password",{
                    required: true,
                })}
                placeholder = "Password"
            />
            {errors?.password?.type === "required" && <p className="error-message">You should enter your password to connect</p>}
            <button type="submit">Log In</button>
        </form>
    );
}