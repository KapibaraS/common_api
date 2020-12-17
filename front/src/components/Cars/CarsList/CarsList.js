import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const CarsList = () => {
  const [cars, setCars] = useState([]);

  return (
    <>
      <div>
        Header
        <Link to="cars/new">+ Add Car</Link>
      </div>

      <table>
        <thead>
          <tr>
            <th>Manufacturer</th>
            <th>Model</th>
            <th>Year of Production</th>
            <th>Color</th>
            <th>VIN Code</th>
            <th />
          </tr>
        </thead>
        <tbody>
          {cars.map((car) => (
            <tr key={car.car_id}>
              <td>{car.manufacturer}</td>
              <td>{car.model}</td>
              <td>{car.year_production}</td>
              <td>{car.color}</td>
              <td>{car.vin_code}</td>
              <td>
                <Link to={`/car_edit/${car.car_id}`}>Edit</Link>
                <a onClick={() => {}}>Delete</a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default CarsList;
