from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Body mass index (BMI) is a measurement of a person's weight in relation to their height. It offers an inexpensive and simple method of categorising people according to their BMI value so that we can screen people’s weight category and indicate their potential risk for health conditions.",
        "height": "In Meters eg: 1.5",
        "weight": "In Kg",
        "underweight": "BMI less than 18.5",
        "normal_healthy_weight": "BMI between 18.5 and 24.9",
        "overweight": "BMI between 25.0 and 29.9",
        "obese": "BMI between 30.0 and 39.9",
        "morbidly_obese": "BMI 40.0 and above"
    }


@app.get("/api/bmicalculator/")
async def bmicalculator(height: float, weight: float, age: Optional[int] = None):

    if age is None:
        age = 0

    bmi = round(weight / (height * height), 2)
    if bmi < 18.5:
        return JSONResponse(
            content={
                "result": "Underweight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age
            },
            status_code=200)
    elif bmi >= 18.5 and bmi < 24.9:
        return JSONResponse(
            content={
                "result": "Normal weight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
    elif bmi >= 25.0 and bmi < 29.9:
        return JSONResponse(
            content={
                "result": "Overweight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
    elif bmi >= 30.0 and bmi < 39.9:
        return JSONResponse(
            content={
                "result": "Obese",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
    elif bmi >= 40.0:
        return JSONResponse(
            content={
                "result": "Morbidly Obese",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
