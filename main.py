from fastapi import FastAPI, Request, Response
from datetime import datetime

from response.usage_history.allusage.true.voice.true_voice_postpaid_7 import TRUE_VOICE_POSTPAID_7 
from response.usage_history.allusage.true.voice.true_voice_postpaid_8 import TRUE_VOICE_POSTPAID_8
from response.usage_history.allusage.true.voice.true_voice_postpaid_9 import TRUE_VOICE_POSTPAID_9
from response.usage_history.allusage.true.voice.true_voice_postpaid_10 import TRUE_VOICE_POSTPAID_10

from response.usage_history.allusage.true.message.true_message_postpaid_7 import TRUE_MESSAGE_POSTPAID_7
from response.usage_history.allusage.true.message.true_message_postpaid_8 import TRUE_MESSAGE_POSTPAID_8
from response.usage_history.allusage.true.message.true_message_postpaid_9 import TRUE_MESSAGE_POSTPAID_9
from response.usage_history.allusage.true.message.true_message_postpaid_10 import TRUE_MESSAGE_POSTPAID_10

from response.usage_history.allusage.true.vas.true_vas_postpaid_7 import TRUE_VAS_POSTPAID_7
from response.usage_history.allusage.true.vas.true_vas_postpaid_8 import TRUE_VAS_POSTPAID_8
from response.usage_history.allusage.true.vas.true_vas_postpaid_9 import TRUE_VAS_POSTPAID_9
from response.usage_history.allusage.true.vas.true_vas_postpaid_10 import TRUE_VAS_POSTPAID_10

from response.usage_history.allusage.dtac.data.dtac_postpaid_data_7 import DTAC_DATA_POSTPAID_7
from response.usage_history.allusage.dtac.data.dtac_postpaid_data_8 import DTAC_DATA_POSTPAID_8  
from response.usage_history.allusage.dtac.data.dtac_postpaid_data_9 import DTAC_DATA_POSTPAID_9
from response.usage_history.allusage.dtac.data.dtac_postpaid_data_10 import DTAC_DATA_POSTPAID_10

from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_7 import DTAC_VOICE_POSTPAID_7
from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_8 import DTAC_VOICE_POSTPAID_8
from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_9 import DTAC_VOICE_POSTPAID_9
from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_10 import DTAC_VOICE_POSTPAID_10

from response.usage_history.allusage.dtac.message.dtac_message_postpaid_7 import DTAC_MESSAGE_POSTPAID_7
from response.usage_history.allusage.dtac.message.dtac_message_postpaid_8 import DTAC_MESSAGE_POSTPAID_8
from response.usage_history.allusage.dtac.message.dtac_message_postpaid_9 import DTAC_MESSAGE_POSTPAID_9
from response.usage_history.allusage.dtac.message.dtac_message_postpaid_10 import DTAC_MESSAGE_POSTPAID_10

from response.usage_history.summary.dtac.summary_dtac_prepaid_6 import SUMMARY_DTAC_PREPAID_6
from response.usage_history.summary.dtac.summary_dtac_prepaid_7 import SUMMARY_DTAC_PREPAID_7
from response.usage_history.summary.dtac.summary_dtac_prepaid_8 import SUMMARY_DTAC_PREPAID_8
from response.usage_history.summary.dtac.summary_dtac_prepaid_9 import SUMMARY_DTAC_PREPAID_9
from response.usage_history.summary.dtac.summary_dtac_prepaid_10 import SUMMARY_DTAC_PREPAID_10

from response.usage_history.summary.dtac.summary_dtac_postpaid_6 import SUMMARY_DTAC_POSTPAID_6
from response.usage_history.summary.dtac.summary_dtac_postpaid_7 import SUMMARY_DTAC_POSTPAID_7
from response.usage_history.summary.dtac.summary_dtac_postpaid_8 import SUMMARY_DTAC_POSTPAID_8
from response.usage_history.summary.dtac.summary_dtac_postpaid_9 import SUMMARY_DTAC_POSTPAID_9
from response.usage_history.summary.dtac.summary_dtac_postpaid_10 import SUMMARY_DTAC_POSTPAID_10

from response.usage_history.summary.true.summary_true_postpaid import SUMMARY_TRUE_DATA_POSTPAID
from response.usage_history.summary.true.summry_true_prepaid import SUMMARY_TRUE_DATA_PREPAID
from response.qryBalance import QRY_BALANCE
from response.usage_history.invoice.invoiceDtailDtac import INVOICE_DETAIL_DTAC
from response.usage_history.invoice.invoiceDtailTrue import INVOICE_DETAIL_TRUE

app = FastAPI(
    title="Mock Response From APIGW",
    version="1.0.0",
    description="Mock Response From APIGWI",
)

@app.post("/v3/qryBalance")
async def qryBalance(request: Request, response: Response):
    return QRY_BALANCE

@app.post("/v2/invoiceDetail")
async def invoiceDetail(request: Request, response: Response):
    body = await request.json()         
    channel = body.get("channel") 
    if channel == "dtac":
        return INVOICE_DETAIL_DTAC
    else:
        return INVOICE_DETAIL_TRUE

@app.get("/usageConsumptionReport/{id}")
async def list_summary(id: str, request: Request, response: Response):
    query_params = request.query_params 
    query_dict = dict(query_params)
    paymentMethod = query_dict.get("paymentMethod")
    usgeStart = query_dict.get("usgeStart")
    byCycle = query_dict.get("byCycle")
    channel = query_dict.get("relatedResource.channel")

    if channel != "true":
        if paymentMethod =="0":
            if usgeStart =="20250700":
                return SUMMARY_DTAC_PREPAID_7
            elif usgeStart =="20250800":
                return SUMMARY_DTAC_PREPAID_8
            elif usgeStart =="20250900":
                return SUMMARY_DTAC_PREPAID_9
            elif usgeStart =="20251000":
                return SUMMARY_DTAC_PREPAID_10
            
        elif paymentMethod =="2":
            if byCycle =="20250611":
                return SUMMARY_DTAC_POSTPAID_6
            elif byCycle =="20250711":
                return SUMMARY_DTAC_POSTPAID_7
            elif byCycle =="20250811":
                return SUMMARY_DTAC_POSTPAID_8
            elif byCycle =="20250911":
                return SUMMARY_DTAC_POSTPAID_9
            elif byCycle =="20251011":
                return SUMMARY_DTAC_POSTPAID_10
            

    else:
        if paymentMethod =="0":
            return SUMMARY_TRUE_DATA_PREPAID
        else:
            return SUMMARY_TRUE_DATA_POSTPAID
        

@app.get("/usageManagement/v1/usage")
async def list_allusage(request: Request, response: Response):
    query_params = request.query_params 
    query_dict = dict(query_params)
    channel = query_dict.get("channel")
    usageDate = query_dict.get("usageDate")
    cycleInstanse = query_dict.get("cycleInstanse")
    usageType = query_dict.get("usageType")
    serviceType = query_dict.get("serviceType")

    if channel == "True": 
        if serviceType == "CALLING":
            response.headers["X-Total-Count"] = "10"
            if cycleInstanse == "7":
                return TRUE_VOICE_POSTPAID_7
            if cycleInstanse == "8":
                return TRUE_VOICE_POSTPAID_8
            if cycleInstanse == "9":
                return TRUE_VOICE_POSTPAID_9
            if cycleInstanse == "10":
                return TRUE_VOICE_POSTPAID_10
            
        elif serviceType == "SMS":
            response.headers["X-Total-Count"] = "10"
            if cycleInstanse == "7":
                return TRUE_MESSAGE_POSTPAID_7
            if cycleInstanse == "8":
                return TRUE_MESSAGE_POSTPAID_8
            if cycleInstanse == "9":
                return TRUE_MESSAGE_POSTPAID_9
            if cycleInstanse == "10":
                return TRUE_MESSAGE_POSTPAID_10
        
        elif serviceType == "DCB":
            startDateTime = query_dict.get("startDateTime")
            dt = datetime.fromisoformat(startDateTime)
            month = dt.month
            response.headers["X-Total-Count"] = "3"
            if month == 7:
                return TRUE_VAS_POSTPAID_7
            if month == 8:
                return TRUE_VAS_POSTPAID_8
            if month == 9:
                return TRUE_VAS_POSTPAID_9
            if month == 10:
                return TRUE_VAS_POSTPAID_10
        
    else:
        response.headers["X-Total-Count"] = "3"
        if usageType=="7":
            if usageDate == "20250711":
                return DTAC_VOICE_POSTPAID_7
            elif usageDate == "20250811":
                return DTAC_VOICE_POSTPAID_8
            elif usageDate == "20250911":
                return DTAC_VOICE_POSTPAID_9
            elif usageDate == "20251011":
                return DTAC_VOICE_POSTPAID_10
            
        elif usageType=="2":
            if usageDate == "20250711":
                return DTAC_DATA_POSTPAID_7
            elif usageDate == "20250811":
                return DTAC_DATA_POSTPAID_8
            elif usageDate == "20250911":
                return DTAC_DATA_POSTPAID_9
            elif usageDate == "20251011":
                return DTAC_DATA_POSTPAID_10
        
        elif usageType=="5,9":
            if usageDate == "20250711":
                return DTAC_MESSAGE_POSTPAID_7
            elif usageDate == "20250811":
                return DTAC_MESSAGE_POSTPAID_8
            elif usageDate == "20250911":
                return DTAC_MESSAGE_POSTPAID_9
            elif usageDate == "20251011":
                return DTAC_MESSAGE_POSTPAID_10