import axios from "axios";


//-------------------GET REQUEST-------------------//
export async function getUsers(url) {
    return await axios.get(url).then((response) => {
        return response;
    });
}
//------------------------------------------------//


//-------------------POST REQUEST-------------------//
// export async function postNewUser(url, data) {
//     const userData = JSON.stringify(data);
//     const result = await axios.post(url, userData);

//     alert(result.data.headers['Content-Type']);
// }
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