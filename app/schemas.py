# Pydantic schemas are stored here to declutter the main app
from pydantic import BaseModel


class ConversionData(BaseModel):
    from_currency: str
    to_currency: str
    original_amount: float
    converted_amount: float