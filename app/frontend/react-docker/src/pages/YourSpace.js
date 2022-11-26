import React from 'react'
import axios from "axios";
// import Col from 'react-bootstrap/Col';
import { NavBar } from '../components/NavBar';
import { useParams } from 'react-router-dom';
import { firstRequest } from '../services/eldenRing';
import { getUsers } from '../services/userApi';
// import { ItemCard } from '../components/YourSpace/ItemCard';
import { WeaponStatsForm } from '../components/WeaponStatsForm';
import { Void } from '../components/Void';
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
    let [itemDatas, setItemleDatas] = React.useState([]);
    let [userDatas, setUserDatas] = React.useState([]);

    //**********item api**********//
    React.useEffect(() => {
        firstRequest(baseURL).then(res => {
            setItemleDatas(res.data);
        })
    }, []);
    console.log(itemDatas[0])
    // React.useEffect(() => {
    //     axios.get(baseURL).then((response) => {
    //         setItemleDatas(response.data);
    //     });
    // }, []);
    //***************************//

    //**********user api**********//
    React.useEffect(() => {
        getUsers(getUsersURL).then(res => {
            setUserDatas(res.data);
        })
    }, []);
    console.log("This is users datas: ", userDatas)
    //***************************//

    console.log("this itemdata :",itemDatas)

    return (
        <div>
            <Void/>
            <NavBar navBarTitle={navBarTitle}/>
            <div className='your-space-body'>
                {/* <p>{userDatas[0]?.username}</p> */}
                <WeaponStatsForm/>
                {/* <Col>
                    <ItemCard ItemName={itemDatas[0]?.name} 
                            ItemImg={itemDatas[0]?.image} 
                            ItemText={itemDatas[0]?.description}/>
                    <ItemCard ItemName={itemDatas[1]?.name} 
                            ItemImg={itemDatas[1]?.image} 
                            ItemText={itemDatas[1]?.description}/>
                    <ItemCard ItemName={itemDatas[2]?.name} 
                            ItemImg={itemDatas[2]?.image} 
                            ItemText={itemDatas[2]?.description}/>
                    <ItemCard ItemName={itemDatas[3]?.name} 
                            ItemImg={itemDatas[3]?.image} 
                            ItemText={itemDatas[3]?.description}/>
                    <ItemCard/>
                </Col> */}
            </div> 
            {/* <div className='request'>{itemDatas[0]?.name}</div> */}
            
            

        </div>
       
    )
}