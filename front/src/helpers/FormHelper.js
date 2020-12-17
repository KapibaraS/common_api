import snakeCase from 'lodash.snakeCase';

export const prepareParams = (formData) => {
  const params = {};

  Object.keys(formData).forEach((attribute) => {
    params[snakeCase(attribute)] = formData[attribute];
  })

  return params;
}
