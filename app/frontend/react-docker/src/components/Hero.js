import React from 'react'
import "./Hero.css";

export const Hero = ({imageSrc}) => {
  return (
    <div className='hero'>
        <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffree4kwallpapers.com%2Fuploads%2Foriginals%2F2019%2F06%2F18%2Felden-ring-wallpaper.jpg&f=1&nofb=1&ipt=b334dbe7490a1674017050b05d10342c52aaf915637d1700fc70ff194fd39e83&ipo=images" alt="first-img" className="hero-image"/>
        <h2 className="hero-title">
            Elden Ring build creator
        </h2>        
    </div>
  );
}


