import { createBrowserRouter } from "react-router-dom";
import { Home } from "../pages";
import { HistoriaClinica } from '../pages/HistoriaClinica/HistoriaClinica.jsx';

export const Routes = createBrowserRouter([
    { path: "/", element: <Home /> },
    { path: "/HistoriaClinica", element: <HistoriaClinica /> }
]);
