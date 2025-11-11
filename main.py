from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from datetime import datetime

from response.usage_history.allusage.true.voice.true_voice_postpaid_7 import TRUE_VOICE_POSTPAID_7 
from response.usage_history.allusage.true.voice.true_voice_postpaid_8 import TRUE_VOICE_POSTPAID_8
from response.usage_history.allusage.true.voice.true_voice_postpaid_9 import TRUE_VOICE_POSTPAID_9
from response.usage_history.allusage.true.voice.true_voice_postpaid_10 import TRUE_VOICE_POSTPAID_10
from response.usage_history.allusage.true.voice.true_voice_postpaid_11 import TRUE_VOICE_POSTPAID_11

from response.usage_history.allusage.true.message.true_message_postpaid_7 import TRUE_MESSAGE_POSTPAID_7
from response.usage_history.allusage.true.message.true_message_postpaid_8 import TRUE_MESSAGE_POSTPAID_8
from response.usage_history.allusage.true.message.true_message_postpaid_9 import TRUE_MESSAGE_POSTPAID_9
from response.usage_history.allusage.true.message.true_message_postpaid_10 import TRUE_MESSAGE_POSTPAID_10
from response.usage_history.allusage.true.message.true_message_postpaid_11 import TRUE_MESSAGE_POSTPAID_11

from response.usage_history.allusage.true.vas.true_vas_postpaid_7 import TRUE_VAS_POSTPAID_7
from response.usage_history.allusage.true.vas.true_vas_postpaid_8 import TRUE_VAS_POSTPAID_8
from response.usage_history.allusage.true.vas.true_vas_postpaid_9 import TRUE_VAS_POSTPAID_9
from response.usage_history.allusage.true.vas.true_vas_postpaid_10 import TRUE_VAS_POSTPAID_10
from response.usage_history.allusage.true.vas.true_vas_postpaid_11 import TRUE_VAS_POSTPAID_11

from response.usage_history.allusage.true.vas.true_vas_prepaid_7 import TRUE_VAS_PREPAID_7
from response.usage_history.allusage.true.vas.true_vas_prepaid_8 import TRUE_VAS_PREPAID_8
from response.usage_history.allusage.true.vas.true_vas_prepaid_9 import TRUE_VAS_PREPAID_9
from response.usage_history.allusage.true.vas.true_vas_prepaid_10 import TRUE_VAS_PREPAID_10
from response.usage_history.allusage.true.vas.true_vas_prepaid_11 import TRUE_VAS_PREPAID_11

from response.usage_history.allusage.dtac.data.dtac_postpaid_data_7 import DTAC_DATA_POSTPAID_7
from response.usage_history.allusage.dtac.data.dtac_postpaid_data_8 import DTAC_DATA_POSTPAID_8  
from response.usage_history.allusage.dtac.data.dtac_postpaid_data_9 import DTAC_DATA_POSTPAID_9
from response.usage_history.allusage.dtac.data.dtac_postpaid_data_10 import DTAC_DATA_POSTPAID_10
from response.usage_history.allusage.dtac.data.dtac_postpaid_data_11 import DTAC_DATA_POSTPAID_11

from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_7 import DTAC_VOICE_POSTPAID_7
from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_8 import DTAC_VOICE_POSTPAID_8
from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_9 import DTAC_VOICE_POSTPAID_9
from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_10 import DTAC_VOICE_POSTPAID_10
from response.usage_history.allusage.dtac.voice.dtac_voice_postpaid_11 import DTAC_VOICE_POSTPAID_11

from response.usage_history.allusage.dtac.message.dtac_message_postpaid_7 import DTAC_MESSAGE_POSTPAID_7
from response.usage_history.allusage.dtac.message.dtac_message_postpaid_8 import DTAC_MESSAGE_POSTPAID_8
from response.usage_history.allusage.dtac.message.dtac_message_postpaid_9 import DTAC_MESSAGE_POSTPAID_9
from response.usage_history.allusage.dtac.message.dtac_message_postpaid_10 import DTAC_MESSAGE_POSTPAID_10
from response.usage_history.allusage.dtac.message.dtac_message_postpaid_11 import DTAC_MESSAGE_POSTPAID_11


from response.usage_history.summary.dtac.summary_dtac_prepaid_6 import SUMMARY_DTAC_PREPAID_6
from response.usage_history.summary.dtac.summary_dtac_prepaid_7 import SUMMARY_DTAC_PREPAID_7
from response.usage_history.summary.dtac.summary_dtac_prepaid_8 import SUMMARY_DTAC_PREPAID_8
from response.usage_history.summary.dtac.summary_dtac_prepaid_9 import SUMMARY_DTAC_PREPAID_9
from response.usage_history.summary.dtac.summary_dtac_prepaid_10 import SUMMARY_DTAC_PREPAID_10
from response.usage_history.summary.dtac.summary_dtac_prepaid_11 import SUMMARY_DTAC_PREPAID_11

from response.usage_history.summary.dtac.summary_dtac_postpaid_6 import SUMMARY_DTAC_POSTPAID_6
from response.usage_history.summary.dtac.summary_dtac_postpaid_7 import SUMMARY_DTAC_POSTPAID_7
from response.usage_history.summary.dtac.summary_dtac_postpaid_8 import SUMMARY_DTAC_POSTPAID_8
from response.usage_history.summary.dtac.summary_dtac_postpaid_9 import SUMMARY_DTAC_POSTPAID_9
from response.usage_history.summary.dtac.summary_dtac_postpaid_10 import SUMMARY_DTAC_POSTPAID_10
from response.usage_history.summary.dtac.summary_dtac_postpaid_11 import SUMMARY_DTAC_POSTPAID_11


from response.usage_history.summary.true.summary_true_postpaid import SUMMARY_TRUE_DATA_POSTPAID
from response.usage_history.summary.true.summry_true_prepaid import SUMMARY_TRUE_DATA_PREPAID
from response.qryBalance import QRY_BALANCE
from response.usage_history.invoice.invoiceDtailDtac import INVOICE_DETAIL_DTAC
from response.usage_history.invoice.invoiceDtailTrue import INVOICE_DETAIL_TRUE

from response.usage_history.allusage.dtac.data.dtac_prepaid_data_7 import DTAC_DATA_PREPAID_7
from response.usage_history.allusage.dtac.data.dtac_prepaid_data_8 import DTAC_DATA_PREPAID_8
from response.usage_history.allusage.dtac.data.dtac_prepaid_data_9 import DTAC_DATA_PREPAID_9
from response.usage_history.allusage.dtac.data.dtac_prepaid_data_10 import DTAC_DATA_PREPAID_10
from response.usage_history.allusage.dtac.data.dtac_prepaid_data_11 import DTAC_DATA_PREPAID_11

from response.usage_history.allusage.dtac.voice.dtac_voice_prepaid_7 import DTAC_VOICE_PREPAID_7
from response.usage_history.allusage.dtac.voice.dtac_voice_prepaid_8 import DTAC_VOICE_PREPAID_8
from response.usage_history.allusage.dtac.voice.dtac_voice_prepaid_9 import DTAC_VOICE_PREPAID_9
from response.usage_history.allusage.dtac.voice.dtac_voice_prepaid_10 import DTAC_VOICE_PREPAID_10
from response.usage_history.allusage.dtac.voice.dtac_voice_prepaid_11 import DTAC_VOICE_PREPAID_11

from response.usage_history.allusage.dtac.message.dtac_message_prepaid_7 import DTAC_MESSAGE_PREPAID_7
from response.usage_history.allusage.dtac.message.dtac_message_prepaid_8 import DTAC_MESSAGE_PREPAID_8
from response.usage_history.allusage.dtac.message.dtac_message_prepaid_9 import DTAC_MESSAGE_PREPAID_9
from response.usage_history.allusage.dtac.message.dtac_message_prepaid_10 import DTAC_MESSAGE_PREPAID_10
from response.usage_history.allusage.dtac.message.dtac_message_prepaid_11 import DTAC_MESSAGE_PREPAID_11

app = FastAPI(
    title="Mock Response From APIGW",
    version="1.0.0",
    description="Mock Response From APIGWI",
)

def get_id_from_usage(u):
    for item in u.get("dcbCharacteristic", []):
        if item.get("name", "").strip().lower() == "id":
            return str(item.get("value"))
    return None

def paginate_usage(base_resp, limit, next_offset):
    usages = list(base_resp.get("usage", []))
    total = len(usages)

    start_index = 0

    if next_offset:
        for i, u in enumerate(usages):
            if get_id_from_usage(u) == next_offset:
                start_index = i + 1
                break

    limit = int(limit) if limit else 1
    page_data = usages[start_index:start_index + limit]

    has_more = (start_index + limit) < total
    next_id = get_id_from_usage(page_data[-1]) if has_more else ""

    result = {**base_resp, "usage": page_data}
    return result, total, has_more, next_id


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
            elif usgeStart =="20251100":
                return SUMMARY_DTAC_PREPAID_11
            
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
            elif byCycle =="20251111":
                return SUMMARY_DTAC_POSTPAID_11    
            
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
    startDateTime = query_dict.get("startDateTime")
    limit = query_dict.get("limit")
    nextOffset = query_dict.get("dcb.nextOffset")
    relatedPartyType = query_dict.get("relatedParty.type")
    pageNumber = query_dict.get("pageNumber")

    if channel == "True": 
        if serviceType == "CALLING":
            response.headers["X-Total-Count"] = "10"
            if pageNumber == "4":
                return JSONResponse(
                    status_code=400,
                    content={"code": "400.198.3001", "description": "", "timestamp": ""}
                )
            else:
                if cycleInstanse == "7":
                    return TRUE_VOICE_POSTPAID_7
                if cycleInstanse == "8":
                    return TRUE_VOICE_POSTPAID_8
                if cycleInstanse == "9":
                    return TRUE_VOICE_POSTPAID_9
                if cycleInstanse == "10":
                    return TRUE_VOICE_POSTPAID_10
                if cycleInstanse == "11":
                    return TRUE_VOICE_POSTPAID_11
            
        elif serviceType == "SMS":
            response.headers["X-Total-Count"] = "11"
            if cycleInstanse == "7":
                return TRUE_MESSAGE_POSTPAID_7
            if cycleInstanse == "8":
                return TRUE_MESSAGE_POSTPAID_8
            if cycleInstanse == "9":
                return TRUE_MESSAGE_POSTPAID_9
            if cycleInstanse == "10":
                return TRUE_MESSAGE_POSTPAID_10
            if cycleInstanse == "11":
                return TRUE_MESSAGE_POSTPAID_11
        
        elif serviceType == "DCB":
            limit = query_dict.get("limit")
            nextOffset = query_dict.get("dcb.nextOffset")
            dt = datetime.fromisoformat(startDateTime)
            month = dt.month
            if relatedPartyType == "1":
                base_resp = (
                    TRUE_VAS_POSTPAID_7 if month == 7 else
                    TRUE_VAS_POSTPAID_8 if month == 8 else
                    TRUE_VAS_POSTPAID_9 if month == 9 else
                    TRUE_VAS_POSTPAID_10 if month == 10 else
                    TRUE_VAS_POSTPAID_11
                )
            elif relatedPartyType == "0":
                base_resp = (
                    TRUE_VAS_PREPAID_7 if month == 7 else
                    TRUE_VAS_PREPAID_8 if month == 8 else
                    TRUE_VAS_PREPAID_9 if month == 9 else
                    TRUE_VAS_PREPAID_10 if month == 10 else
                    TRUE_VAS_PREPAID_11
                )
            paged, total, has_more, next_id = paginate_usage(base_resp, limit, nextOffset)
            response.headers["X-Total-Count"] = str(total)
            response.headers["X-Limit"] = str(limit or 1)
            response.headers["X-Has-More"] = "true" if has_more else "false"
            response.headers["X-Next-Offset"] = next_id
            return paged
        
    else:
        response.headers["X-Total-Count"] = "3"
        if usageDate == None:
            dt = datetime.fromisoformat(startDateTime)
            if usageType=="7":
                if dt.month == 7:
                    return DTAC_VOICE_PREPAID_7
                elif dt.month == 8:
                    return DTAC_VOICE_PREPAID_8
                elif dt.month == 9:
                    return DTAC_VOICE_PREPAID_9
                elif dt.month == 10:
                    return DTAC_VOICE_PREPAID_10
                elif dt.month == 11:
                    return DTAC_VOICE_PREPAID_11
                
            elif usageType=="2":
                if dt.month == 7:
                    return DTAC_DATA_PREPAID_7
                elif dt.month == 8:
                    return DTAC_DATA_PREPAID_8
                elif dt.month == 9:
                    return DTAC_DATA_PREPAID_9
                elif dt.month == 10:
                    return DTAC_DATA_PREPAID_10
                elif dt.month == 11:
                    return DTAC_DATA_PREPAID_11    
                
            elif usageType=="5,9":
                if dt.month == 7:
                    return DTAC_MESSAGE_PREPAID_7
                elif dt.month == 8:
                    return DTAC_MESSAGE_PREPAID_8
                elif dt.month == 9:
                    return DTAC_MESSAGE_PREPAID_9
                elif dt.month == 10:
                    return DTAC_MESSAGE_PREPAID_10
                elif dt.month == 11:
                    return DTAC_MESSAGE_PREPAID_11
                
        else:
            if usageType=="7":
                if usageDate == "20250711":
                    return DTAC_VOICE_POSTPAID_7
                elif usageDate == "20250811":
                    return DTAC_VOICE_POSTPAID_8
                elif usageDate == "20250911":
                    return DTAC_VOICE_POSTPAID_9
                elif usageDate == "20251011":
                    return DTAC_VOICE_POSTPAID_10
                elif usageDate == "20251111":
                    return DTAC_VOICE_POSTPAID_11
            
            elif usageType=="2":
                if usageDate == "20250711":
                    return DTAC_DATA_POSTPAID_7
                elif usageDate == "20250811":
                    return DTAC_DATA_POSTPAID_8
                elif usageDate == "20250911":
                    return DTAC_DATA_POSTPAID_9
                elif usageDate == "20251011":
                    return DTAC_DATA_POSTPAID_10
                elif usageDate == "20251111":
                    return DTAC_DATA_POSTPAID_11
        
            elif usageType=="5,9":
                if usageDate == "20250711":
                    return DTAC_MESSAGE_POSTPAID_7
                elif usageDate == "20250811":
                    return DTAC_MESSAGE_POSTPAID_8
                elif usageDate == "20250911":
                    return DTAC_MESSAGE_POSTPAID_9
                elif usageDate == "20251011":
                    return DTAC_MESSAGE_POSTPAID_10
                elif usageDate == "20251111":
                    return DTAC_MESSAGE_POSTPAID_11
