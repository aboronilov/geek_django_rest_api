import React from 'react'
import UserItem from './UserItem/UserItem'
import { fetchUsers } from '../../store/userReducer';
import {useDispatch, useSelector} from "react-redux";
import styles from './UserList.module.css'

export default function UserList(props) {
  const users = useSelector(state => state.userReducer.users)
  const dispatch = useDispatch()  

  return (
    <div>
      { users.length
        ? <UserItem users={users} />
        : <button className={[styles.button]} onClick={() => dispatch(fetchUsers())}>ПОЛУЧИТЬ ЮЗЕРОВ</button>
      }
    </div>    
  )
}
