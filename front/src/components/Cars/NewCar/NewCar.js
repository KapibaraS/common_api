import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';
import CarForm from '../CarForm';
import { CAR_PLACEHOLDER } from '../constants';
import { prepareParams } from '../../../helpers/FormHelper';

const NewCar = () => {
  const [car, setCar] = useState(CAR_PLACEHOLDER);

  const handleCarChange = (event) => {
    const { name, value } = event.target;

    event.preventDefault();
    setCar({ ...car, [name]: value });
  };

  const updateCar = (event) => {
    event.preventDefault();

    axios.post('http://localhost:8080/v1/create_car', prepareParams(car)).then(() => {
      useHistory().push('/');
    });
  }

  return (
    <div className="new-car">
      <CarForm
        car={car}
        onChange={handleCarChange}
        onSubmit={updateCar}
      />
    </div>
  );
};

export default NewCar;
