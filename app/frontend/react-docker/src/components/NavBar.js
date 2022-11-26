import React, { useState } from 'react'
import { FiMenu, FiX } from 'react-icons/fi'
import { useLocation, useNavigate } from 'react-router-dom';
import './NavBar.css'


export const NavBar = ({navBarLinks, navBarTitle}) => {
    const [menuClicked, setMenuClicked] = useState(false);
    const toggleMenuClick = () => {
        setMenuClicked(!menuClicked);
    }
    const isConnect = localStorage.getItem("username"); 
    const currentPage = useLocation();
    const navigate = useNavigate()

    function disconnect(){
        localStorage.removeItem('username');
        localStorage.removeItem('build');
        localStorage.removeItem('nbBuild');
        navigate('/');
    }

  return (
    <nav className='navbar'>
        <span className='navbar-logo'>Elden Ring {navBarTitle}</span>
        {menuClicked ? (
            <FiX size={25} className='navbar-menu' onClick={toggleMenuClick}/>
        ) : (
            <FiMenu size={25} className='navbar-menu' onClick={toggleMenuClick}/>
        )}
        <ul className={menuClicked ? "navbar-list" : "navbar-list navbar-list--active"}>
            {/* {navBarLinks.map(item =>{
                return (
                    <li className='navbar-item' key={item.title}>
                        <a className='navbar-link' href={item.url}>
                            {item.title}
                        </a>
                    </li>
                )
            })} */}
            <li className='navbar-item' style={{display: currentPage.pathname === '/' ? 'none' : 'block'}}>
                <a className='navbar-link' href='/'>
                    Home
                </a>
            </li>
            <li className='navbar-item' style={{display: isConnect !== null ? 'block' : 'none'}}>
                <a className='navbar-link' href={`/your_space/${isConnect}`}>
                    Build
                </a>
            </li>
            <li className='navbar-item' style={{display: isConnect !== null ? 'block' : 'none'}}>
                <a className='navbar-link' href={`/your_weapon/${isConnect}`}>
                    Weapon
                </a>
            </li>
            <li className='navbar-item' style={{display: isConnect === null ? 'block' : 'none'}}>
                <a className='navbar-link' href='/login'>
                    Login
                </a>
            </li>
            <li className='navbar-item' style={{display: isConnect === null ? 'block' : 'none'}}>
                <a className='navbar-link' href='/signin'>
                    Sign Up
                </a>
            </li>
            <li className='navbar-item' style={{display: isConnect !== null ? 'block' : 'none'}}>
                <a className='navbar-link' onClick={disconnect}>
                    Logout
                </a>
            </li>

        </ul>
    </nav>
  )
};
