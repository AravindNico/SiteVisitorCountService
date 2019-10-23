import requests
import time
import random as r

'''
For Demo purpose , two active user count metrics for "site1","site2" is generated.
Provide the count for number of messages to be sent to sumMetrics server.
'''
site1url = "http://localhost:3011/sitemetrics/v1/metrics/site1"
site2url = "http://localhost:3011/sitemetrics/v1/metrics/site2"

headers = {
    'Content-Type': "application/json"
}


def testSiteVisitorCount(count):
    for i in range(0, count):
        site1payload = "{\n \"value\": "+str(r.randint(1, 20))+"\n}"
        site2payload = "{\n \"value\": "+str(r.randint(1, 10))+"\n}"
        site1response = requests.request(
            "POST", site1url, data=site1payload, headers=headers)
        print(site1response.text)
        site2response = requests.request(
            "POST", site2url, data=site2payload, headers=headers)
        print(site2response.text)
        time.sleep(1)


if __name__ == '__main__':
    testSiteVisitorCount(1000)
