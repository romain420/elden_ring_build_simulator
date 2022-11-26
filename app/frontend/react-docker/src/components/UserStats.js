import React from 'react'
import { GiSwordman } from "react-icons/gi";
import './UserStats.css'

export function UserStats(props) {
    // const userStats = JSON.parse(localStorage.getItem('stats'))
    

    return (
        <div className='character-stat'>
            <GiSwordman/> Character Status
            <div className='stat-ligne'>
                <p className='stat-name'>Rune Level</p>
                <p className='stat-num'>{props.runeLevel}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>HP</p>
                <p className='stat-num'>{props.HP}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>FP</p>
                <p className='stat-num'>{props.FP}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Stamina</p>
                <p className='stat-num'>{props.stamina}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Equipement Load</p>
                <p className='stat-num'>{props.equipLoad}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Physical Defence</p>
                <p className='stat-num'>{props.physicalDefense}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Magic Defence</p>
                <p className='stat-num'>{props.magicDefense}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Fire Defense</p>
                <p className='stat-num'>{props.fireDefense}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Lightning Defense</p>
                <p className='stat-num'>{props.lightningDefense}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Holy Defense</p>
                <p className='stat-num'>{props.holyDefense}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Immunity</p>
                <p className='stat-num'>{props.immunity}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Robustness</p>
                <p className='stat-num'>{props.robustness}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Focus</p>
                <p className='stat-num'>{props.focus}</p>
            </div>
            <div className='stat-ligne'>
                <p className='stat-name'>Vitality</p>
                <p className='stat-num'>{props.vitality}</p>
            </div>
        </div>
    )
}