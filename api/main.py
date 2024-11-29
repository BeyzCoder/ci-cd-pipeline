from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from api.routes import data_collect, data_grab

# Create a asynchronous server gateway interface
app = FastAPI()

# Connect the routes
app.include_router(data_collect.router, prefix="/data-collect")
app.include_router(data_grab.router, prefix="/data-grab")


@app.get("/")
async def root() -> JSONResponse:
    resp: dict = {"state" : "Server up running!!"}
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")
