
/*require('dotenv').config();
const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/predict', async (req, res) => {
  try {
    const flaskRes = await axios.post(
      `${process.env.FLASK_URL}/predict`,
      req.body
    );
    res.json(flaskRes.data);
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Prediction failed' });
  }
});

app.listen(process.env.PORT, () => {
  console.log(`Server listening on port ${process.env.PORT}`);
});*/



require('dotenv').config();
const express = require('express');
const cors = require('cors');
const axios = require('axios');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());

// === API route for predictions ===
app.post('/api/predict', async (req, res) => {
  try {
    const flaskRes = await axios.post(
      `${process.env.FLASK_URL}/predict`,
      req.body
    );
    res.json(flaskRes.data);
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Prediction failed' });
  }
});

// === Serve React frontend from server/public ===
app.use(express.static(path.join(__dirname, 'public')));

// Catch-all route for React Router (Express 5 fix: use regex instead of "*")
app.get(/.*/, (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 10000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});


