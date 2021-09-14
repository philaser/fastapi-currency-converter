# main app with app initialization and routes
from fastapi import FastAPI, HTTPException

from app.helpers import convertCurrency
from app.schemas import ConversionData

app = FastAPI()


@app.get("/api/v1/convert", response_model= ConversionData, response_model_exclude_unset=True)
async def converter(from_currency: str, to_currency: str, amount: float):
    data = await convertCurrency(from_currency, to_currency, amount)
    if data['status'] == 'SUCCESS':
        return data
    else:
        raise HTTPException(status_code=500, detail=data['message'])