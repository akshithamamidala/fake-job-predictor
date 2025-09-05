import React from 'react';
import './PredictionResult.css';

function PredictionResult({ result }) {
  const isFake = result.prediction === 1;

  return (
    <div
      className="result"
      style={{
        border: `2px solid ${isFake ? '#dc3545' : '#28a745'}`
      }}
    >
      <h2>
        This job posting is likely:
      </h2>
      <div
        className={`badge ${isFake ? 'badge-fake' : 'badge-real'}`}
      >
        {isFake ? 'FAKE / SCAM' : 'REAL / LEGITIMATE'}
      </div>
      <div className="confidence">
        Confidence:
        <br />
        Real: {(result.probability[0] * 100).toFixed(2)}% <br />
        Fake: {(result.probability[1] * 100).toFixed(2)}%
      </div>
    </div>
  );
}

export default PredictionResult;
