const express = require('express');
const fetch = require('node-fetch');
const app = express();
app.use(express.json());

const SPRING_BACKEND_URL = 'http://localhost:8081/api/predict'; // Spring Boot endpoint

app.post('/predict', async (req, res) => {
    const response = await fetch(SPRING_BACKEND_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(req.body)
    });
    const data = await response.json();
    res.json(data);
});

app.listen(3000, () => console.log("Frontend proxy running on http://localhost:3000"));
