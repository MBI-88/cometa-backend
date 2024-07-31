from fastapi import APIRouter, HTTPException, status, Response
from app.services.beer_services import  get_beers 
from app.services.order_services import get_order
from app.domain.repositories.repo import Beer, List, OrderItem
from app.domain.models.models import *
from app.domain.validators.schema import *
import json



router = APIRouter()

@router.get("/beers", response_model=List[Beer])
async def get_beers_route():
    result = get_beers()
    return Response(content=json.dumps(result), media_type="application/json",status_code=status.HTTP_200_OK)


@router.get("/order", response_model=OrderSchema)
async def get_order_route():
    result =  get_order()
    return Response(content=json.dumps(result), media_type="application/json", status_code=status.HTTP_200_OK)
