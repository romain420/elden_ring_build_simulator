import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; 


export function Void() {
    const navigate = useNavigate();
    const userName = localStorage.getItem("username")

    useEffect(() => {
        if(userName === null){
            navigate('/')
        }
    }, []);

    return (
        <div></div>
    )
}
