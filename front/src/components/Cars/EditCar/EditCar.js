import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useHistory, useParams } from 'react-router-dom';
import CarForm from '../CarForm';
import { CAR_PLACEHOLDER } from '../constants';
import { prepareParams } from '../../../helpers/FormHelper';

const EditCar = () => {
  const [car, setCar] = useState(CAR_PLACEHOLDER);

  useEffect(() => {
    const { id } = useParams();

    axios.get(`/v1/get_car/${id}`).then((response) => {
      setCar(response.car)
    });
  }, []);

  const handleCarChange = (event) => {
    const { name, value } = event.target;

    event.preventDefault();
    setCar({ ...car, [name]: value });
  };

  const createCar = (event) => {
    event.preventDefault();

    axios.put('http://localhost:8080/v1/update_car', prepareParams(car)).then(() => {
      useHistory().push('/');
    });
  }

  return (
    <div className="new-car">
      <CarForm
        car={car}
        onChange={handleCarChange}
        onSubmit={createCar}
      />
    </div>
  );
};

export default EditCar;
