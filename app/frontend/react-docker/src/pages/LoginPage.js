import React from 'react'
import { LoginForm } from '../components/LoginForm'
import { NavBar } from '../components/NavBar';
import './ConnexionPage.css'

export function LoginPage() {
  const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/signin", title:"SignIn"}    
  ];

  const navBarTitle = "Login page";

  return (
    <div>
      {/* <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffree4kwallpapers.com%2Fuploads%2Foriginals%2F2019%2F06%2F18%2Felden-ring-wallpaper.jpg&f=1&nofb=1&ipt=b334dbe7490a1674017050b05d10342c52aaf915637d1700fc70ff194fd39e83&ipo=images" alt="first-img" className="connect-image"/> */}
      <NavBar navBarTitle={navBarTitle}/>
      <h2 className='form-title'>Login Form</h2>
      <LoginForm/>
      <div className='register'>
        <a href='/signup' className='register-link'>Register Page →</a>
      </div>
    </div>
    
  )
}
