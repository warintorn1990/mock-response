DO $$
DECLARE
    mock_url TEXT := 'http://localhost';
BEGIN
    UPDATE common_service_endpoint
    SET srv_endpoint_url = mock_url || '/usageConsumptionReport/{id}'
    WHERE srv_name = 'QueryUsageSummary';

    UPDATE common_service_endpoint
    SET srv_endpoint_url = mock_url || '/v3/qryBalance'
    WHERE srv_name = 'GetUsageConsumptionQueryBalance';

    UPDATE common_service_endpoint
    SET srv_endpoint_url = mock_url || '/usageManagement/v1/usage'
    WHERE srv_name = 'getCDROnline';

    UPDATE common_service_endpoint
    SET srv_endpoint_url = mock_url || '/v2/invoiceDetail'
    WHERE srv_name = 'InvoiceDetail';
END $$;
