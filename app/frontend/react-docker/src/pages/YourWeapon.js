import React from 'react'
import { NavBar } from '../components/NavBar'
import { WeaponStatsForm } from '../components/WeaponStatsForm';

const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/build_space", title:"Build"},
    {url:"/weapon", title:"Weapon"}
];

export function YourWeapon() {
    const navBarTitle = "Your Weapon"
    return (
        <div>
            <NavBar navBarLinks={navBarLinks} navBarTitle={navBarTitle}/>
            <WeaponStatsForm/>
        </div>
    )
}

