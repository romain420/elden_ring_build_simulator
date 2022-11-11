import React from 'react';
import './Card.css';

export function Card() {
  return (
    <div className='card'>
        <div className='stat-card'>
            <h2>Item name</h2>
            <p>ligne1</p>
            <p>ligne1</p>
            <p>ligne1</p>
        </div>
        <div className='picture-card'>
            <img src='https://eldenring.fanapis.com/images/items/17f69e47912l0i1z0lip3kamll88h.png' alt='item-image'/>
        </div>
    </div>
  )
}

