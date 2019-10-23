from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS
from flask import Blueprint
import time
import json
import os
import uuid
import sys
import datetime
sys.path.append('...')

# Custom modules
import importlib
import importlib.util


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


calculation = module_from_file("calculation", "metricscalculator.py")
loggers = module_from_file("loggers", "logger.py")

api = Blueprint('api', __name__, url_prefix='/sitemetrics/v1/metrics')

'''***************************************************
method      : post
function    : metricsLogging
description : log visitor count for any service 
***************************************************'''


@api.route('/<key>', methods=['POST'])
def metricsLogging(key):
    print(key)
    content = request.json
    metrics = {
        "service": key,
        "timeStamp": str(datetime.datetime.now()),
        "count": content["value"]
    }
    print(metrics)
    return jsonify(calculation.postMetrics(metrics))


'''***********************************************************
method      : get
function    : sumOfActiveVisitors
description : provides visitor count for the requested service 
************************************************************'''


@api.route('/<key>/sum', methods=['get'])
def sumOfActiveVisitors(key):
    print(key)
    if key != "":
        setTime = request.args.get("time", default=1, type=float)
        print(setTime)
        return jsonify(calculation.sumMetrics(key, setTime))
    else:
        return jsonify({"error": "Pass Valid Service ID to get Metrics"})
