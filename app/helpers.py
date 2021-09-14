import aiohttp
import logging

logger = logging.getLogger(__name__)
format = '[%(asctime)s]{%(name)s:%(lineno)d}%(levelname)s- %(message)s'
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S",
                        handlers=[logging.FileHandler("example1.log"),
                  logging.StreamHandler()])

ACCESS_KEY = '165850929f3969f2e866'
URL = 'https://free.currconv.com/api/v7/convert'


async def convertCurrency(from_currency, to_currency, amount):
    currencies = f'{from_currency}_{to_currency}'
    queries = f'q={currencies}&compact=ultra&apiKey={ACCESS_KEY}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{URL}?{queries}') as response:
                if response.status == 200 and await response.json():
                    data = await response.json()
                    conversion = amount * data[currencies]
                    result = {
                        'status': 'SUCCESS',
                        "from_currency": from_currency,
                        "to_currency": to_currency,
                        "original_amount": amount,
                        "converted_amount": conversion
                    }
                    return result
                else:
                    message = f"Conversion failed due to invalid inputs"
                    error = { 
                        'status': 'FAILURE',
                        'message': message
                    }
                    logger.exception(message)
                    return error
    except Exception as e:
        message = f"Conversion failed due to ERROR: {e}"
        error = {
                'status': 'FAILURE',
                'message': message
            }
        logger.exception(message)    
        return error
