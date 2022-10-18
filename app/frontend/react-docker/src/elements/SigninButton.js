import '../App.css';
import * as React from 'react';

export function SigninButton(props) {
    const signInClick = () => {
         window.alert("Pas JAAAAAAAAAAAAAAAAAAAAAAAAAAAJ");
    };
    return(<button type="button" className="signin-button" onClick={signInClick}>
        Sign in
    </button>)
}
