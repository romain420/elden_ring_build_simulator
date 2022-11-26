import axios from "axios";


//-------------------GET REQUEST-------------------//
//method to get the first user in database
export async function getUsers(url) {
    return await axios.get(url).then((response) => {
        return response;
    });
}

//method to check user cred and GET his usefull information
export async function confirmUser(url){
    // console.log("this is userCred :", url)
    return await axios.get(url)
        .then((response) => {
            if(response.data === "Wrong password, please check your informations"){
                // console.log(response.data)
                alert(response.data);
                // return response.data
            }
            else if(response.data === "This user does not exist") alert(response.data)
            else return response.data
        })
        .catch(function (error) {
            alert("⚠ Sorry We have some issues with server.. Please try again later");
        })
}

//method to calcul basic stat with naked player spec
export async function calculBasicStats(url){
    return await axios.get(url)
        .then((response) => {
            // console.log(response.data);
            return response.data;
        })
        .catch((error) =>{
            alert("⚠ Sorry We have some issues with server.. Please try again later")
        })
}
//------------------------------------------------//


//-------------------POST REQUEST-------------------//
//POST/create user by register all his informations 
export async function postNewUser(url, data) {
    // const userData = JSON.parse(JSON.stringify(data));
    // // console.log("this is userData :",userData)
    // const type = "";
    // const message = "";
    return await axios.post(url, data)
        .then(response => {
            return response;
        })
        .catch((error) =>{
            return error.status;
        });
}
//--------------------------------------------------//

// const data_response = {
//     "username": "eadnoth",
//     "First_name": "",
//     "Last_name": "",
//     "date_of_birth": "2022-11-18T18:36:19.959Z",
//     "email": "romain@dreuilh.et",
//     "password": "azertyuiop",
//     "created_at": "2022-11-18T18:36:19.960Z",
//     "last_visit": "2022-11-18T18:36:19.960Z",
//     "nb_builds": 0,
//     "builds": [
//       "string"
//     ]
//   }