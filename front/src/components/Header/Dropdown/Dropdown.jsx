 import styles from "./Dropdown.module.scss"
 import { useNavigate } from "react-router-dom";
 export const Dropdown=({options})=>{
    const navigate = useNavigate();
    return(
        <div className={styles.dropdown}>
              <ul>
              {options.map((option, index) => (
          <li key={index} onClick={() => navigate(option.path)}>
            {option.label}
          </li>
        ))}
              </ul>
        </div>
    )
 }