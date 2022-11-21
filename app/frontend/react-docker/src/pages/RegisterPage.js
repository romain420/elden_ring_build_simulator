import React from 'react'
import { RegisterForm } from '../components/RegisterForm'
import { NavBar } from '../components/NavBar'
import './ConnexionPage.css'

export function RegisterPage() {
    const navBarLinks = [
        {url:"/", title:"Home"},
        {url:"/login", title:"LogIn"}    
    ];

    const navBarTitle = "Register page";

    return (
        <div>
            <NavBar navBarLinks={navBarLinks} navBarTitle={navBarTitle}/>
            <h2 className='form-title'>Register Form</h2>
            <RegisterForm/>
        </div>
    )
}