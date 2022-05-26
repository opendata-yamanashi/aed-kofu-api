from data import Yamanashi_AED
from fastapi import FastAPI

yA = Yamanashi_AED()
yA.create_df()

app = FastAPI()

@app.get("/")
def hello():
    return "Hello! Please access /docs"

@app.get("/list/")
def get_data():
    return yA.df.to_dict("records")

@app.get("/query/")
def do_query(q=None):
    return yA.query(q).to_dict("records")

@app.get("/version/")
def get_version():
    return {"version": yA.get_data_version()}

