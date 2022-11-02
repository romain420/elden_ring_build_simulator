import React from 'react'
import { NavBar } from '../components/NavBar'

const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/build_space", title:"Build"},
    {url:"/weapon", title:"Weapon"}
];

export function YourWeapon() {
    const navBarTitle = "Your Weapon"
    return (
        <NavBar navBarLinks={navBarLinks} navBarTitle={navBarTitle}/>
    )
}

