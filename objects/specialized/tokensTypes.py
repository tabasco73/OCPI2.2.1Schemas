from objects.general.generalTypes import DisplayText
from objects.specialized.sessionsTypes import ProfileType
from objects.general.tokenRootTypes import TokenType
from pydantic import BaseModel, Field # type: ignore
from typing import Optional
from datetime import datetime
from enum import Enum

class EnergyContract(BaseModel):
    supplier_name: Optional[str] = Field(None, max_length=64)
    contract_id: Optional[str] = Field(None, max_length=64)

class WhitelistType(str, Enum):
    ALWAYS = "ALWAYS"
    ALLOWED = "ALLOWED"
    ALLOWED_OFFLINE = "ALLOWED_OFFLINE"
    NEVER = "NEVER"

class Token(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    uid: str = Field(..., max_length=36)
    type: TokenType
    contract_id: Optional[str] = Field(None, max_length=36)
    visual_number: Optional[str] = Field(None, max_length=64)
    issuer: Optional[str] = Field(None, max_length=64)
    group_id: Optional[str] = Field(None, max_length=36)
    valid: bool
    whitelist: Optional[WhitelistType] = None
    language: Optional[str] = Field(None, max_length=2)
    default_profile_type: Optional[ProfileType] = None  # Assuming ProfileType is a custom enum
    energy_contract: Optional[EnergyContract] = None  # Assuming EnergyContract is a custom class
    last_updated: datetime