import "./App.css";
import { Home } from "./pages/Home";
import { YourSpace } from "./pages/YourSpace";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { YourWeapon } from "./pages/YourWeapon";
import { ErrorPage } from "./pages/ErrorPage";


export default function App() {
  return (
    
    <Router>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/build_space" element={<YourSpace/>} />
        <Route path="/weapon" element={<YourWeapon/>} />
        <Route path="*" element={<ErrorPage/>} />
      </Routes>
    </Router>
  );
}


//<Route path="/build_space/:username" element={<YourSpace/>} />
/*<div className="App">
      <NavBar navBarLinks={navBarLinks}/>
      <Hero/>
      <Slider imageSrc={"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.wccftech.com%2Fwp-content%2Fuploads%2F2021%2F06%2FER_KEY-ART-scaled-e1623411764381-2048x1052.jpg&f=1&nofb=1&ipt=cca417bfb3c279ac47510eb50b9ec92276ccdc72c54ab276a23ae78e0dc76af4&ipo=images"}
        title={"Create your own build"} 
        subtitle={"Access to all stuff and weapon from Elden Ring"} 
      />
      <Slider imageSrc={"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F2.bp.blogspot.com%2F-JRnRaJbPr5s%2FXR40yngbZRI%2FAAAAAAAAIGc%2Fov_uzsKz5tobj4ZAC6ItTHXTBOWwvjJkACKgBGAs%2Fw4096-h2304-p-k-no-nu%2Felden-ring-poster-uhdpaper.com-4K-4.jpg&f=1&nofb=1&ipt=52de80ab4a1cdb41b867836a6484ded64bd65f8219ac96a20f675174f0b9df14&ipo=images"}
        title={"Choose the Perfect Weapon"} 
        subtitle={"Scale your weapon to get the most surgeon build for PvE and PvP"} 
        flipped={true}
      />
    </div>*/
//<Hero imageSrc={'./assets/image1.jpeg'}/>
