from pydantic import BaseModel
from typing import Optional
from enum import Enum


class FinanceWebsite(str, Enum):
    macrotrend = "macrotrend"


class ScrapeParams(BaseModel):
    """Model for requesting website."""
    symbol: str
    website: Optional[FinanceWebsite]


class GrabParams(BaseModel):
    """Model for requesting website."""
    symbol: str
