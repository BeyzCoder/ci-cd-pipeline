from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api.models.collect_model import ScrapeParams
from api.services.scrape import scrape_statement

router = APIRouter()


@router.post("/v1/scrape-statement/")
async def collect(scrape: ScrapeParams) -> JSONResponse:
    statements = scrape_statement(**scrape.__dict__)
    # statements = scrape.__dict__
    return JSONResponse(content=statements, status_code=status.HTTP_200_OK, media_type="application/json")
