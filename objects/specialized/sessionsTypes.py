from typing import List, Optional, Union
from pydantic import BaseModel, Field, HttpUrl # type: ignore
from datetime import datetime
from enum import Enum

from objects.general.generalTypes import Price
from objects.specialized.cDRsRootTypes import AuthMethod, CdrToken, ChargingPeriod
""" Sessions """        

class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    INVALID = "INVALID"
    PENDING = "PENDING"
    RESERVATION = "RESERVATION"

class Session(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    id: str = Field(..., max_length=36)
    start_date_time: datetime
    end_date_time: Optional[datetime] = None
    kwh: float
    cdr_token: CdrToken
    auth_method: Optional[AuthMethod] = None  # This should be an Enum if defined
    authorization_reference: Optional[str] = Field(None, max_length=36)
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    connector_id: Optional[str] = Field(None, max_length=36)
    meter_id: Optional[str] = Field(None, max_length=255)
    currency: str = Field(..., max_length=3)
    charging_periods: Optional[List[ChargingPeriod]] = Field(default_factory=list)
    total_cost: Optional[Price] = None
    status: Optional[SessionStatus] = None
    last_updated: datetime

""" Charging Preferences """

class ProfileType(str, Enum):
    CHEAP = "CHEAP"
    FAST = "FAST"
    GREEN = "GREEN"
    REGULAR = "REGULAR"