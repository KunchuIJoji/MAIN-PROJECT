import api from './configs/axiosConfig';

export const PredictCampusPlacements = async (excelFile) => {
    // 1. Create a new FormData object
    const formData = new FormData();
    
    // 2. Append the file to it. 
    // We use 'file' as the key because Flask usually looks for request.files['file']
    formData.append('file', excelFile); 

    // 3. Send the formData instead of the raw file
    const response = await api.post('/predict-campus-placements', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });

    return response.data;
};