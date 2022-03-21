import React from "react";
import styles from './CinemaItem.module.css'

export default function CinemaItem({ cinemas }) {
  const DisplayData = cinemas.map((cinema, i) => {
    return (
      <tr key={i}>
        <td>{cinema.name}</td>
        <td>{cinema.actors.join(', ')}</td>
      </tr>
    );
  });

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <th>Cinema Name</th>
          <th>Main actors</th>
        </tr>
      </thead>
      <tbody>
        {DisplayData}
      </tbody>
    </table>
  );
}