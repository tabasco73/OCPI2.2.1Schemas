from objects.specialized.cDRsRootTypes import ChargingPeriod
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime
from typing import Optional, List
from objects.specialized.sessionsTypes import Session

"""Sender Interface - CPO Implements"""

# GET

class GetSessionsSenderRequest(BaseModel):
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    offset: Optional[int] = 0  # Default offset is 0
    limit: Optional[int] = 100  # Default limit is 100

class GetSessionsSenderResponse(BaseModel):
    Session: List[Session]  # Assuming Session is a custom class representing a session object


"""Receiver Interface - eMSP Implements"""

# GET

class GetSessionReceiverRequest(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    session_id: str = Field(..., max_length=36)

class GetSessionReceiverResponse(BaseModel):
    Session: Session

# PUT

class PutSessionReceiverRequestParams(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    session_id: str = Field(..., max_length=36)

class PutSessionReceiverRequestBody(BaseModel):
    Session: Session  # Assuming Session is a custom class representing a session object

class PutSessionReceiverResponse(BaseModel):
    """Not mentioned in OCPP 2.2.1, assuming success response"""
    success: bool

# PATCH

class PatchSessionReceiverRequestParams(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    session_id: str = Field(..., max_length=36)

class PatchSessionReceiverRequestBody(BaseModel):
    total_cost: Optional[dict] = None
    charging_periods: Optional[List[ChargingPeriod]] = None
    kwh: Optional[float] = None
    last_updated: datetime = Field(...)