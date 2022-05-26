from data import Yamanashi_AED
from fastapi import FastAPI

from model import AED_Data
from pydantic import BaseModel, Field
from typing import List
import os

yA = Yamanashi_AED()
yA.create_df()

root_path = os.getenv("ROOT_PATH", "")
app = FastAPI(
    title="AED設置施設一覧(甲府市施設) API",
    root_path=root_path
)

@app.get("/")
def hello():
    return "Hello! Please access /docs"

@app.get("/list/", response_model=List[AED_Data])
def get_data():
    return yA.df.to_dict("records")

@app.get("/query/", response_model=List[AED_Data])
def do_query(q=None):
    return yA.query(q).to_dict("records")

class VersionEndpointResponse(BaseModel):
    version: str = Field(None, alias="version")

@app.get("/version/", response_model=VersionEndpointResponse)
def get_version():
    return {"version": yA.get_data_version()}

