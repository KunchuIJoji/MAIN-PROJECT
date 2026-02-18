import api from './configs/axiosConfig'

export const ResumeParser = async (file) => {
  const formData = new FormData();
  formData.append('file', file); 

  const res = await api.post('/resume-parser', formData);
  return res.data;
}

export const PredictStudent = async (data) => {
  // FIX: Don't return 'res.data' yet. Let the component handle it.
  const res = await api.post('/predict-student-placement', data);
  return res; 
}

export const RecommendSkills = async (data) => {
  const res = await api.post('/recommendSkills', data);
  return res.data;
}