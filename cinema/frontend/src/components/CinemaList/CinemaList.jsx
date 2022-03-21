import React from 'react'
import CinemaItem from './CinemaItem/CinemaItem'
import { fetchCinemas } from '../../store/cinemaReducer';
import {useDispatch, useSelector} from "react-redux";
import styles from './CinemaList.module.css'

export default function CinemaList(props) {
  const cinemas = useSelector(state => state.cinemaReducer.cinemas)
  const dispatch = useDispatch()  

  return (
    <div>
      { cinemas.length
        ? <CinemaItem cinemas={cinemas} />
        : <button className={[styles.button]} onClick={() => dispatch(fetchCinemas())}>ПОЛУЧИТЬ ФИЛЬМЫ</button>
      }
    </div>    
  )
}