import React, { useRef } from "react";
import ReactDOM from "react-dom";
import { useForm } from "react-hook-form";
import { confirmUser, postNewUser } from "../services/userApi";
import { useNavigate } from 'react-router-dom';
import "./Form.css"

export function LoginForm() {
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
        reset
    } = useForm()
    
    const navigate = useNavigate();

    const onSubmit = (data) => {
        const userName = data.username;
        const password = data.password;
        const url = `http://localhost:5000/check_mdp?username=${userName}&password=${password}`;

        confirmUser(url).then(res => {
            localStorage.setItem('username',res.username);
            localStorage.setItem('build', res.builds);
            localStorage.setItem('nbBuild', res.nb_builds);
            navigate('/build_space');
        })
        
    };

    return (
        <form className="connect-form" onSubmit={handleSubmit(onSubmit)} method="post"   >
            <label className="form-label">User Name</label>
            <input className="form-input"
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
            <label className="form-label">Password</label>
            <input className="form-input"
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