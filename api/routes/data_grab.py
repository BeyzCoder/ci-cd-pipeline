from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from api.models.collect_model import GrabParams
from api.db.dynamo import get_item

router = APIRouter()


@router.get("/v1/grab-statement/")
async def grab_statement(grab: GrabParams) -> JSONResponse:
    response = get_item(grab.__dict__)
    if response["status"] == "FAILED":
        raise HTTPException(status_code=500, detail=response["error"])
    return JSONResponse(content=response, status_code=status.HTTP_200_OK, media_type="application/json")
