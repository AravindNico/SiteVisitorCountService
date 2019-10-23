# sumMetricsService
Metric logging and reporting service that sums metrics by time window for the most recent hour/minutes.

## Setup
    pip3 install -r requirements.txt

## Start Server
    python3 summetrics.py

## Test Data Posting(post)
    python3 test.py
    
## To check the metrics(get)
1.Open browser/postman and provice the get url

    http://localhost:3011/sitemetrics/v1/metrics/site1/sum?time=1
    
### Configurable Params
    http://<IP>:<PORT>/sitemetrics/v1/metrics/<SERVICE>/sum<URL QUERY PARAM>

1.IP
2.PORT 
3.SERVICE
4.URL PARAM - time parameter take in number of minutes (optional parameter).

If Url Param "time" is not passed , default value of 1 minute will be considered.
