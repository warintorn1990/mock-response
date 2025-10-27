UPDATE common_service_endpoint
SET srv_endpoint_url = 'https://test-apigw.dtac.co.th/customer/v2/usageConsumptionReport/{id}'
WHERE srv_name = 'QueryUsageSummary';

UPDATE common_service_endpoint
SET srv_endpoint_url = 'https://test-apigw.dtac.co.th/usageConsumption/v3/qryBalance'
WHERE srv_name = 'GetUsageConsumptionQueryBalance';

UPDATE common_service_endpoint
SET srv_endpoint_url = 'https://test-apigw.dtac.co.th/usageManagement/v1/usage'
WHERE srv_name = 'getCDROnline';

UPDATE common_service_endpoint
SET srv_endpoint_url = 'https://test-apigw.dtac.co.th/customerBillManagementB2B/v2/invoiceDetail'
WHERE srv_name = 'InvoiceDetail';
