package com.example.backend.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.beans.factory.annotation.Value;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class PredictController {

    private final RestTemplate restTemplate = new RestTemplate();
    //private final String fastApiUrl = "http://localhost:8080/predict"; // your FastAPI endpoint

    @Value("${FASTAPI_URL:http://localhost:8080}")
    private String fastApiUrl;

    @PostMapping("/predict")
    public ResponseEntity<Map> predict(@RequestBody Map<String, String> requestBody) {
        String url = fastApiUrl + "/predict";
        Map response = restTemplate.postForObject(url, requestBody, Map.class);
        return ResponseEntity.ok(response);
    }
}
