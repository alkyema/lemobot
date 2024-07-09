from fastapi import FastAPI, File, UploadFile
from bson import ObjectId
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from Data_Fetch_Option_1_Learn_About_Our_Product import Data_Fetch_Option_1_Learn_About_Our_Product
from Lead_Capture import Lead_Capture
from FAQs_Fetch import FAQs_Fetch
import shutil

# Create an instance of FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a route with a GET method
@app.get("/")
def read_root():
    return {"Server": "Ready"}

# Define a route with a GET method and a path parameter
@app.get("/Data_Fetch_Option_1")
def Data_Fetch_Option_1():
    return Data_Fetch_Option_1_Learn_About_Our_Product()

class LeadCaptureModel(BaseModel):
    Domain:str
    Name: str
    EmailID: str
    Contact: str
    Prefered_Mode_of_Contact: str
    Project_Domain: str
    Project_Description: str

@app.post("/Lead_Capture")
def Lead_Capture_API(lead: LeadCaptureModel):
    print(lead.Domain, lead.Name, lead.EmailID, lead.Contact, lead.Prefered_Mode_of_Contact, lead.Project_Domain, lead.Project_Description)
    return Lead_Capture(lead.Domain, lead.Name, lead.EmailID, lead.Contact, lead.Prefered_Mode_of_Contact, lead.Project_Domain, lead.Project_Description)

@app.get("/FAQs_Fetch")
def FAQs_Fetch_API():
    return FAQs_Fetch()