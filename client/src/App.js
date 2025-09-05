import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import PredictionResult from './components/PredictionResult';

function App() {
  const [form, setForm] = useState({
    title: '',
    description: '',
    requirements: ''
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    try {
      const res = await axios.post('http://localhost:4000/api/predict', form);
      setResult(res.data);
    } catch (error) {
      console.error(error);
      alert('Prediction failed. Make sure backend servers are running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Fake Job Detection</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="title"
          placeholder="Job Title"
          value={form.title}
          onChange={handleChange}
          required
        />
        <textarea
          name="description"
          placeholder="Description"
          value={form.description}
          onChange={handleChange}
          required
        />
        <textarea
          name="requirements"
          placeholder="Requirements"
          value={form.requirements}
          onChange={handleChange}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Predicting...' : 'Predict'}
        </button>
      </form>
      {result && <PredictionResult result={result} />}
    </div>
  );
}

export default App;
