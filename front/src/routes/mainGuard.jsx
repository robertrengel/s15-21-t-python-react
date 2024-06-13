import { useContext } from "react";
import { UserContext } from "../context/UserContext/UserContext";
import { Navigate } from "react-router-dom";

export function MainGuard(props) {
    const user = useContext(UserContext).user;
    const localUser = JSON.parse(localStorage.getItem("user"));

    // if (!localUser.user_id && !user.user_id) {
    //     return <Navigate to="/" replace />;
    // }

    return props.children;
}
