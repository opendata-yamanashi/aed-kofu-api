from pydantic import BaseModel, Field

class AED_Data(BaseModel):
    facility: str = Field(None, alias="設置施設")
    facility_detail: str = Field(None, alias="設置箇所(詳細に)")
    address: str = Field(None, alias="住所")
    control: str = Field(None, alias="所管")
