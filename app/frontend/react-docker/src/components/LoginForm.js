import React, { useRef } from "react";
import ReactDOM from "react-dom";
import { useForm } from "react-hook-form";
import { confirmUser } from "../services/userApi"
import "./Form.css"

export function LoginForm() {
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
        reset
    } = useForm()

    let [userConnect, setUserConnect] = React.useState([]);

    const onSubmit = (data) => {
        const userName = data.username;
        const password = data.password;
        const url = "http://localhost:5000/check_mdp?username=" + userName + "&password=" + password;
        // alert(url)
        confirmUser(url).them(function(res) {
            console.log("this is user info :" + res.data)
        })
        // React.useEffect(() => {
        //     confirmUser(url).then(res => {
        //         setUserConnect(res.data);
        //     })
        // }, []);
        // console.log(userConnect[0])
        // window.location.href = '/weapon';
    };

    return (
        <form className="connect-form" onSubmit={handleSubmit(onSubmit)}>
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