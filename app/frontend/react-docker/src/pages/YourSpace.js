import React from 'react'
import axios from "axios";
import { NavBar } from '../components/NavBar';
import { useParams } from 'react-router-dom';
import { firstRequest } from '../services/eldenRing';
import { ItemCard } from '../components/YourSpace/ItemCard';
import Col from 'react-bootstrap/Col';
import './YourSpace.css';


//import '../components/NavBar.css'

const navBarLinks = [
    {url:"/", title:"Home"},
    {url:"/build_space", title:"Build"},
    {url:"/weapon", title:"Weapon"}
];

// premier lien de call api utilisé
const baseURL = "https://eldenring.fanapis.com/api/items?limit=4"

export function YourSpace() {
    let { username } = useParams();
    const navBarTitle = "Your space";
    let [itemDatas, setItemleDatas] = React.useState([]);

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

    console.log("this itemdata :",itemDatas)

    return (
        <div>
            <NavBar navBarLinks={navBarLinks} navBarTitle={navBarTitle}/>
            <div className='your-space-body'>
                <Col>
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
                </Col>
            </div> 
            {/* <div className='request'>{itemDatas[0]?.name}</div> */}
            

        </div>
       
    )
}