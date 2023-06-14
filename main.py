from phishDetect import PhishRes, phishDetect, Features
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from fastapi import Query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PhisherInput(BaseModel):
    url: str


class PhisherRespose(BaseModel):
    res: PhishRes
    features: Features

class ReportInput(BaseModel):
    reportUrl: str

class URLType(str, Enum):
    FAKE = "fake"
    REAL = "real"

@app.post("/check_url")
async def check_url(input: PhisherInput, response_model=PhisherRespose):
    url: str = input.url
    pd = phishDetect(url)
    res = pd.get_res()
    features = pd.get_features()
    return {"res": res, "features": features}

@app.post("/add_url")
async def add_url(input: ReportInput, type: URLType = Query(..., description="Type of URL: 'fake' or 'real'")):
    url: str = input.reportUrl
    filename = "fake.txt" if type == URLType.FAKE else "real.txt"
    with open(filename, "a") as file:
        file.write(url + "\n")
    return {"message": "URL added successfully"}