from pydantic import BaseModel
from typing import Optional
from enum import Enum


class FinanceWebsite(str, Enum):
    yahoo = "yahoo"
    macrotrend = "macrotrend"


class ScrapeParams(BaseModel):
    """Model for requesting website."""
    symbol: str
    website: Optional[FinanceWebsite]
