import styles from './Input.module.scss';

export const Input = ({ label, type, placeholder, ...props }) => {
    return (
        <div className={styles.inputContainer}>
            <label className={styles.label}> { label } </label>
            {type !== 'textarea' ? (
                <input 
                    className={styles.input} 
                    placeholder={placeholder} 
                    type={type} 
                    id={label}
                    name={label}
                    {...props}
                />
            ) : (
                <textarea
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