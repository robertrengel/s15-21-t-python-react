import styles from "./Header.module.scss";
import { useNavigate } from "react-router-dom";
import { Icons } from "../Icons/Icons";
import { Button } from "../Button/Button";

export const Header = ({
  name = "Melania Palomino",
  isEditable = false,
  hasSearch = false,
  ...props
}) => {

    const view= useNavigate();
  function getInitials(names) {
    return names
      .split(" ")
      .map((word) => word.charAt(0).toUpperCase())
      .join("");
  }

  return (
    <header className={styles.header}>
      <div className={styles.user_actions}>
        <div className={styles.user_info}>
          <div className={styles.user_initials}>
            {getInitials(name)}
            {isEditable && (
              <div className={styles.edit_icon}>
                <Icons icon="edit" size={24} color="#222121" />
              </div>
            )}
          </div>
          <span>{name}</span>
        </div>
      </div>
      {hasSearch ? (
        <div className={styles.search_bar}>
          <input
            className={styles.search}
            type="text"
            placeholder="Buscar..."
          />
          <div className={styles.icon}>
            <Icons icon="search" size={24} color="#222121" />
          </div>
        </div>
      ) : (
        <Button variant="text" width={66} height={57} onClick={() => (view("/"))}>
          <Icons icon="setting" size={43.75} color="#222121" />
        </Button>
      )}
    </header>
  );
};
