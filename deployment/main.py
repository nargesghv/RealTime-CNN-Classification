from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from model_loader import load_model, predict_image
import uvicorn

app = FastAPI()
model = load_model()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    prediction = predict_image(contents, model)
    return JSONResponse(content={"prediction": prediction})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
