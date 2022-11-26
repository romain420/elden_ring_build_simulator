import axios from "axios";


//-------------------GET REQUEST-------------------//
export async function getUsers(url) {
    return await axios.get(url).then((response) => {
        return response;
    });
}

export async function confirmUser(url){
    // console.log("this is userCred :", url)
    return await axios.get(url)
        .then((response) => {
            if(response.data !== "This user does not exist" || response.data !== "Wrong password, please check your informations"){
                // alert(response.data)
                return response.data
            }
            else alert(response.data)
        })
        .catch(function (error) {
            alert("⚠ Sorry We have some issues with server.. Please try again later")
        })
}
//------------------------------------------------//


//-------------------POST REQUEST-------------------//
export async function postNewUser(url, data) {
    // const userData = JSON.parse(JSON.stringify(data));
    // // console.log("this is userData :",userData)
    // const type = "";
    // const message = "";
    const result = await axios.post(url, data)
        .then(function (response) {
            alert("Your account has been successfully registered !");
        })
        .catch(function (error) {
            alert("⚠ Error : Your 'User Name' or 'Email' is already use");
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