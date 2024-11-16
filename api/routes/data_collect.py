from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from api.models.collect_model import ScrapeParams
from api.services.scrape import scrape_statement
from api.db.dynamo import put_item

router = APIRouter()


@router.post("/v1/scrape-statement/")
async def collect_statement(scrape: ScrapeParams) -> JSONResponse:
    statements = scrape_statement(**scrape.__dict__)
    response = put_item(statements, scrape.symbol)
    if response["status"] == "FAILED":
        raise HTTPException(status_code=500, detail=response["error"])
    return JSONResponse(content=response, status_code=status.HTTP_200_OK, media_type="application/json")
