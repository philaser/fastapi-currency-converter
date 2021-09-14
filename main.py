from fastapi import FastAPI, HTTPException

from helpers import convertCurrency
from schemas import conversionData

app = FastAPI()


@app.get("/api/v1/convert", response_model= conversionData, response_model_exclude_unset=True)
async def status_handler(from_currency: str, to_currency: str, amount: float):
    data = await convertCurrency(from_currency, to_currency, amount)
    if data['status'] == 'SUCCESS':
        return data
    else:
        raise HTTPException(status_code=500, detail=data['message'])