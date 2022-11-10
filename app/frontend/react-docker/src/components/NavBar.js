import React, { useState } from 'react'
import { FiMenu, FiX } from 'react-icons/fi'
import './NavBar.css'


export const NavBar = ({navBarLinks, navBarTitle}) => {
    const [menuClicked, setMenuClicked] = useState(false);
    const toggleMenuClick = () => {
        setMenuClicked(!menuClicked);
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
            {navBarLinks.map(item =>{
                return (
                    <li className='navbar-item' key={item.title}>
                        <a className='navbar-link' href={item.url}>
                            {item.title}
                        </a>
                    </li>
                )
            })}
        </ul>
    </nav>
  )
};
