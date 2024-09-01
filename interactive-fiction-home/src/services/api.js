import axios from 'axios';

const API_URL = 'http://localhost:8000/api/'; // Replace with your Django backend URL

// Fetch all stories from the API
export const fetchStories = async () => {
  try {
    const response = await axios.get(`${API_URL}stories/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching stories:", error);
    return [];
  }
};
