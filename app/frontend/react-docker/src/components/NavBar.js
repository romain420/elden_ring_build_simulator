import React from 'react'
import { FiMenu, FiX } from 'react-icons/fi'
import './NavBar.css'

/*const navBarLinks = [
    {url:"/home", title:"Home"}
];*/

export const NavBar = ({navBarLinks}) => {
  return (
    <nav className='navbar'>
        <span className='navbar-logo'>build</span>
        <ul className='navbar-list'>
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
