import React from 'react'
import { useForm } from "react-hook-form";
import './WeaponForm.css'

export function WeaponStatsForm() {
    const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
        reset
      } = useForm();

    const onSubmit = (data) => {
        alert(JSON.stringify(data))
    }

    return (
        <div>
            <form className='stat-form' onSubmit={handleSubmit(onSubmit) }>
                {/* <div className='row-form'>
                    <label className='stat-label'>Weapon Name</label>
                    <input className='stat-input'
                        {...register("weaponName", {
                            required: true,
                            pattern: /^[A-Za-z._ ]+$/i
                        })}
                    />
                </div> */}
                {errors?.weaponName?.type === "required" && (<p className='error-message'>This field is required</p>)}
                {errors?.weaponName?.type === "pattern" && <p className='error-message'>This weapon does not exist pls check the name</p>}
                <div className='row-form'>
                    <label className='stat-label'>Vigor</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("vigor", 
                        { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.vigor?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.vigor?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.vigor?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <div className='row-form'>
                    <label className='stat-label'>Mind</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("mind", 
                          { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.mind?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.mind?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.mind?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <div className='row-form'>
                    <label className='stat-label'>Endurance</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("endurance", 
                        { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.endurance?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.endurance?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.endurance?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <div className='row-form'>
                    <label className='stat-label'>Strength</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("strength", 
                        { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.strength?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.strength?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.strength?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <div className='row-form'>
                    <label className='stat-label'>Dexterity</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("dexterity", 
                        { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.dexterity?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.dexterity?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.dexterity?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <div className='row-form'>
                    <label className='stat-label'>Intelligence</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("intelligence", 
                        { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.intelligence?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.intelligence?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.intelligence?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <div className='row-form'>
                    <label className='stat-label'>Faith</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("faith", 
                        { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.faith?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.faith?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.faith?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <div className='row-form'>
                    <label className='stat-label'>Arcane</label>
                    <input className='stat-input'
                        type="number" 
                        {...register("arcane", 
                        { min: 0, 
                            max:99, 
                            required: true}
                        )}
                    />
                </div>
                {errors?.arcane?.type === "min" && <p className='error-message'>You set this stat under 0</p>}
                {errors?.arcane?.type === "max" && <p className='error-message'>You set this stat over 99</p>}
                {errors?.arcane?.type === "required" && (<p className='error-message'>This field is required</p>)}
                <button type="submit">Confirm your stats</button>
            </form>
        </div>
    )
}


// Vigor : int 0 à 99 
// Mind : int 0 à 99 
// Endurance : int 0 à 99 
// Strength : int 0 à 99
// Dexterity : int 0 à 99
// Intelligence : int 0 à 99
// Faith : int 0 à 99
// Arcane : int 0 à 99