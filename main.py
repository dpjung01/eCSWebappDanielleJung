from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from bgpview import *
from test import *

from argparse import ArgumentParser

import json
import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory = "templates")
class  asnRequest(BaseModel):
    ip: str

@app.get("/")
def home(request: Request):
    """
    show ASNs in a table
    """
    #return {"ASNDashboard": "Home"}
    return templates.TemplateResponse("home.html", {
        "request": request,
        "ipaddr": "1.2.3.47"
    })

@app.get("/asn")
def form_post(request: Request):
    # result is data you will display to the user
    #result = "ASN data from bgpview"
    result = ""

    # result is from the user input; see form.html or dashboard.html
    return templates.TemplateResponse('home.html', context={'request': request, 'result': result})


#@app.post("/asn")
#async def requst_asn(asn_request: asnRequest, background_tasks: BackgroundTasks):
   # background_tasks.add_task()
    #return{
     #   "ipaddr": "ipaddress",
    #  "message": "ip address"
    #}

@app.post("/asn")
# Expecting an ip address from user called asn_reques
#def form_post(asn_request: asnRequest):
# define ip in the html form tags under home.html
async def form_post(request: Request, ip: str= Form(...)):
   """
   get ASN prefixes for an IP
   uses JSON format for body of post request
   """
   result = ip
   cat = "catnip"
   #result = testString()
   #result = testList()
   info = get_asninfo(ip)
   info = json.loads(info)

   rows = []
   dict_list = info["ipv4_prefixes"]
   for data in dict_list:
       current_row = []
       for key in data:
           if key == "parent":
               for parent_key in data["parent"]:
                   current_row.append(data["parent"][parent_key])
           else:
               current_row.append(data[key])
       rows.append(current_row)
   table = pd.DataFrame(rows, columns=['Prefix', 'IP', 'CIDR', 'ROA_Status', 'Name', 'Description', 'Country', 'Parent Prefix', 'Parent IP', 'Parent CIDR', 'Parent RIR Name', 'Parent Allocation Status'])

   return templates.TemplateResponse('home.html', context={'request': request, 'result': result, 'cat': cat, 'info': table})
