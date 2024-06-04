import styles from "./Input.module.scss";

export const Input = ({ label, type, placeholder, ...props }) => {
  return (
    <div className={styles.inputContainer}>
      <label className={styles.label}> {label} </label>
      {type !== "textarea" ? (
        <input
          width={341} height={142}
          className={styles.input}
          placeholder={placeholder}
          type={type}
          id={label}
          name={label}
          {...props}
        />
      ) : (
        <textarea
          rows={10} 
          width={341} height={142}
          className={styles.textarea}
          placeholder={placeholder}
          id={label}
          name={label}
          {...props}
        ></textarea>
      )}
    </div>
  );
};
