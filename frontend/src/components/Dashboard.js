import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TruckCard from './TruckCard';
import { Line } from 'react-chartjs-2';

function Dashboard() {
  const [trucks, setTrucks] = useState([]);

  useEffect(() => {
    // Fetch truck status from the backend API
    axios.get('http://localhost:5000/api/status')
      .then(response => setTrucks(response.data))
      .catch(error => console.error(error));
  }, []);

  // Example chart data for demonstration
  const chartData = {
    labels: ['00:00', '00:10', '00:20', '00:30', '00:40'],
    datasets: [{
      label: 'Temperature',
      data: [5, 4.8, 5.1, 4.9, 5],
      borderColor: 'rgba(75,192,192,1)',
      fill: false,
    }]
  };

  return (
    <div>
      <h2>Fleet Status</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {trucks.map((truck, index) => (
          <TruckCard key={index} truck={truck} />
        ))}
      </div>
      <div style={{ marginTop: '2rem' }}>
        <h3>Sensor Data Overview</h3>
        <Line data={chartData} />
      </div>
    </div>
  );
}

export default Dashboard;
