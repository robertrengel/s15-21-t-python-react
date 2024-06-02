import style from './InputCmp.module.css'

const Imput = ({ label ,id, type ,variant='field'}) => {
  return (
    <div className={style[variant]}>
      <label className={style.label} htmlFor={id}>{label}</label>
      {type !== 'textarea' ? (
        <input 
          className={style.input} 
          type={type} 
          id={id} 
          name={label} 
        />
      ) : (
        <textarea 
          className={style.textarea} 
          placeholder="Escriba su mensaje aquí..." 
          id={id} 
          name={label}
        ></textarea>
      )}
    </div>
  
  )
}

export default Imput;