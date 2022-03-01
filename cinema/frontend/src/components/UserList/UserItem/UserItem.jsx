import React from "react";
import styles from './UserItem.module.css'

export default function UserItem({ users }) {
  const DisplayData = users.map((user) => {
    return (
      <tr>
        <td>{user.firstname}</td>
        <td>{user.lastname}</td>
        <td>{user.username}</td>
      </tr>
    );
  });

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>User Name</th>
        </tr>
      </thead>
      <tbody>
        {DisplayData}
      </tbody>
    </table>
  );
}
