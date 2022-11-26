import React from 'react'
import { NavBar } from '../components/NavBar'
import { WeaponStatsForm } from '../components/WeaponStatsForm';
import { Void } from '../components/Void';

const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/build_space", title:"Build"},
    {url:"/weapon", title:"Weapon"}
];

export function YourWeapon() {
    const navBarTitle = "Your Weapon"
    return (
        <div>
            <Void/>
            <NavBar navBarTitle={navBarTitle}/>
            <p>Sorry we didn't start to develop this page yet</p>
        </div>
    )
}

