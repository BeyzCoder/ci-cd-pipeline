from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

# Create a asynchronous server gateway interface
app = FastAPI()


@app.get("/")
async def root() -> JSONResponse:
    resp: dict = {"state" : "Server up running!"}
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")
