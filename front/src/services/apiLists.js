import { fetchApi } from "../helpers/api";

export async function getCountriesList() {
    const url = "catalogs/countries/";

    const response = await fetchApi(url, "GET");

    return response;
}
