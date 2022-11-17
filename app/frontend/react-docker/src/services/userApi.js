import axios from "axios";

export async function getUsers(url) {
    return await axios.get(url).then((response) => {
        return response;
    });
}