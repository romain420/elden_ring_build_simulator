import axios from "axios";


//-------------------GET REQUEST-------------------//
export async function getUsers(url) {
    return await axios.get(url).then((response) => {
        return response;
    });
}
//------------------------------------------------//


//-------------------POST REQUEST-------------------//

//--------------------------------------------------//