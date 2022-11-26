import React, { useEffect, useState } from 'react'
import axios from "axios";
// import Col from 'react-bootstrap/Col';
import { NavBar } from '../components/NavBar';
import { useParams } from 'react-router-dom';
import { firstRequest } from '../services/eldenRing';
import { getUsers } from '../services/userApi';
// import { ItemCard } from '../components/YourSpace/ItemCard';
import { WeaponStatsForm } from '../components/WeaponStatsForm';
import { Void } from '../components/Void';
import { UserStats } from '../components/UserStats';
import './YourSpace.css';


//import '../components/NavBar.css'

const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/build_space", title:"Build"},
    {url:"/weapon", title:"Weapon"}
];

// premier lien de call api utilisé
const baseURL = "https://eldenring.fanapis.com/api/items?limit=4"
const getUsersURL = "http://localhost:5000/users"

export function YourSpace() {
    let { username } = useParams();
    const navBarTitle = "Your space";
    let existingStats = JSON.parse(localStorage.getItem('stats'));
    let [infoStats, setInfoStats] = useState(existingStats);

    // console.log("this itemdata :",itemDatas)

    return (
        <div>
            <Void/>
            <NavBar navBarTitle={navBarTitle}/>
            <div className='your-space-body'>
                {/* <p>{userDatas[0]?.username}</p> */}
                <div className='stats-form'>
                    <WeaponStatsForm setStatsInfo = {setInfoStats}/>
                </div>
                {infoStats && 
                <UserStats
                runeLevel={infoStats.runeLevel}
                HP={infoStats.HP}
                FP={infoStats.FP}
                stamina={infoStats.stamina}
                equipLoad={infoStats.equipLoad}
                physicalDefense={infoStats.physicalDefense}
                magicDefense={infoStats.magicDefense}
                fireDefense={infoStats.fireDefense}
                lightningDefense={infoStats.lightningDefense}
                holyDefense={infoStats.holyDefense}
                immunity={infoStats.immunity}
                robustness={infoStats.robustness}
                focus={infoStats.focus}
                vitality={infoStats.vitality}
            />
                }
                

            </div> 
            {/* <div className='request'>{itemDatas[0]?.name}</div> */}
            
            

        </div>
       
    )
}