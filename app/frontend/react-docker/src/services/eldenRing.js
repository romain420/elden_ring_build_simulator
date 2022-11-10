import axios from "axios";

export async function firstRequest(url) {
    return await axios.get(url).then((response) => {
        return response.data;
    });
}