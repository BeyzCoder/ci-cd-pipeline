from pydantic import BaseModel


class RequestComponent(BaseModel):
    """Model for requesting website."""
    url: str
    headers: dict
    params: dict
