import React from 'react'

import "./Slider.css"

export const Slider = ({imageSrc, title, subtitle, flipped}) => {
    

    const rendContent = () => {
        if(!flipped){
            return <>
                <img src={imageSrc} alt="build-pic" className='slider-image'/>
                <div className='slider-content'>
                    <h1 className='slider-titel'>{title}</h1>
                    <p>{subtitle}</p>
                </div>
            </>;
        }
        else{
            return <>
                <div className='slider-content'>
                    <h1 className='slider-titel'>{title}</h1>
                    <p>{subtitle}</p>
                </div>
                <img src={imageSrc} alt="build-pic" className='slider-image'/>
            </>;
        }
    };
    return (
        <div className='slider'>{rendContent()}</div>
    )
}
