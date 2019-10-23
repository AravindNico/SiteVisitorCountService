import os
import json
import numpy as np
import pandas as pd
import datetime

# capturedMetrics => Dataframe to store all logged metrics from different services
capturedMetrics = pd.DataFrame()

'''****************************************************************
Function    : sumMetrics()
Arguments   : serviceName, timeInMinutes
Description : Provides the sum of active users for the 
                last "n" hours/minutes for the requested service
*****************************************************************'''


def sumMetrics(key, setTime):
    try:
        global capturedMetrics
        # convert the timestamp column to pandas datetime datatype
        capturedMetrics['timeStamp'] = pd.to_datetime(
            capturedMetrics['timeStamp'])
        # get the last "n" hr/min ago timestamp (if delta needed in terms of hour - replace "minutes" with "hours")
        timeDifference = str(datetime.datetime.now() -
                             datetime.timedelta(minutes=float(setTime)))
        # filter the dataframe for requested service and time duration
        filterByService = capturedMetrics.loc[((capturedMetrics['service'] == key) & (
            capturedMetrics['timeStamp'] >= timeDifference))]

        sumOfActiveUsers = filterByService.groupby('service')['count'].sum()
        print(sumOfActiveUsers)
        return {"status": "Success", "value": sumOfActiveUsers.to_dict()[key]}
    except Exception as e:
        print(e)
        return {"status": "Failure"}


'''****************************************************************
Function    : postMetrics()
Arguments   : serviceName
Description : Logs the active users count for a service
*****************************************************************'''


def postMetrics(metrics):
    try:
        global capturedMetrics
        # appends the metrics to the global dataframe
        capturedMetrics = capturedMetrics.append(metrics, ignore_index=True)
        return {"status": "Success"}
    except Exception as e:
        return {"status": "Failure"}
