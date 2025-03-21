import React from 'react';

function TruckCard({ truck }) {
  return (
    <div style={{
      border: '1px solid #ccc',
      borderRadius: '8px',
      padding: '1rem',
      margin: '0.5rem',
      width: '200px'
    }}>
      <h4>Truck {truck.truck_id}</h4>
      <p>Status: {truck.status}</p>
      <p>Last Updated: {truck.last_updated}</p>
      <p>Prediction: {truck.prediction === 1 ? 'Alert' : 'Normal'}</p>
    </div>
  );
}

export default TruckCard;
