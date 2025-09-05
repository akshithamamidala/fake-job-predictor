
require('dotenv').config();
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
});

