from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1.0/predict")
def predict(a: float = 0, b: float = 0):
    total = a + b
    prediction = 1 if total > 5.8 else 0
    return {
        "prediction": prediction,
        "features": {
            "a": a,
            "b": b,
            "sum": total
        }
    }
