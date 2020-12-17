import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const CarForm = ({ car, onChange, onSubmit }) => (
  <div className="car-form">
    <div className="form-group">
      <label htmlFor="manufacturer">Manufacturer</label>
      <input name="manufacturer" value={car.manufacturer} onChange={onChange} />
    </div>

    <div className="form-group">
      <label htmlFor="name">Model</label>
      <input name="model" value={car.model} onChange={onChange} />
    </div>


    <div className="form-group">
      <label htmlFor="yearProduction">Year of Production</label>
      <input name="yearProduction" value={car.yearProduction} onChange={onChange} />
    </div>

    <div className="form-group">
      <label htmlFor="name">Color</label>
      <input name="color" value={car.color} onChange={onChange} />
    </div>

    <div className="form-group">
      <label htmlFor="vinCode">VIN Code</label>
      <input name="vinCode" value={car.vinCode} onChange={onChange} />
    </div>


    <div className="form-group">
      <Link to="/">Cancel</Link>
      <button type="submit" onClick={onSubmit}>Add</button>
    </div>
  </div>
);

CarForm.propTypes = {
  car: PropTypes.shape({
    manufacturer: PropTypes.string.isRequired,
    model: PropTypes.string.isRequired,
    yearProduction: PropTypes.string.isRequired,
    color: PropTypes.string.isRequired,
    vinCode: PropTypes.string.isRequired
  }).isRequired,
  onChange: PropTypes.func.isRequired,
  onSubmit: PropTypes.func.isRequired
};

export default CarForm;
