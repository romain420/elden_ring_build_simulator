import '../App.css';
import * as React from 'react';

export function LoginButton(props) {
    const logInClick = () => {
         window.alert("JAAAAAAAAAAAAAAAAAAAAAAAAAAAJ");
    };
    return(<button type="button" className="login-button" onClick={logInClick}>
        Log-in
    </button>)
}



