export const API_URL = 'http://localhost:8000/api/users/';
export const ROI_API = 'http://localhost:8000/api/ROI/';

export const regionDivided = (id, number, srid) => {
  fetch(`${ROI_API}/${id}/${number}/${srid}`);
};