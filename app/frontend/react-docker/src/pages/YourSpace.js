import React from 'react'
import axios from "axios";
import { NavBar } from '../components/NavBar';
import { useParams } from 'react-router-dom';
import { firstRequest } from '../services/eldenRing';
import { Card } from '../components/YourSpace/Card';
import './YourSpace.css';


//import '../components/NavBar.css'

const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/build_space", title:"Build"},
    {url:"/weapon", title:"Weapon"}
];

// premier lien de call api utilisé
const baseURL = "https://eldenring.fanapis.com/api/items?limit=2"

export function YourSpace() {
    let { username } = useParams();
    const navBarTitle = "Your space";
    let [itemDatas, setItemleDatas] = React.useState([]);

    React.useEffect(() => {
        firstRequest(baseURL).then(res => {
            setItemleDatas(res.data);
        })
    }, []);
    console.log(itemDatas[0]?.image)
    // React.useEffect(() => {
    //     axios.get(baseURL).then((response) => {
    //         setItemleDatas(response.data);
    //     });
    // }, []);

    console.log("this itemdata :",itemDatas)

    return (
        <div>
            <NavBar navBarLinks={navBarLinks} navBarTitle={navBarTitle}/>
            <div className='your-space-body'>
                <Card/>
                <Card/>
                <Card/>
                <Card/>
            </div> 
            {/* <div className='request'>{itemDatas[0]?.name}</div> */}
            

        </div>
       
    )
}