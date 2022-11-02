import React from 'react'
import { NavBar } from '../components/NavBar'
import { useParams } from 'react-router-dom';
//import '../components/NavBar.css'

const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/build_space", title:"Build"},
    {url:"/weapon", title:"Weapon"}
];

export function YourSpace() {
    let { username } = useParams();
    const navBarTitle = "Your space";
    return (
        <div>
            <NavBar navBarLinks={navBarLinks} navBarTitle={navBarTitle}/>
            <div color='white'>bienveue dans ton espace {username}</div> 
        </div>
    )
}