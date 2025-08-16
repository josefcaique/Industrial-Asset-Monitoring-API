from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    machine_id: str
    temperature: float
    vibration: float
    energy: float

@app.post("/sensors/data")
async def recive_sensor_data(data: SensorData):
    print(data.model_dump())
    return {"status": "recived"}