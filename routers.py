from fastapi import APIRouter

router = APIRouter()

@router.get('/converter/{from_currency}')
def converter(from_currency: str, to_currencies: str, value: float):
    return "Converter works!!!"