from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
import pymysql
from django.views.decorators.csrf import csrf_exempt
import akshare as ak
import pandas as pd

@csrf_exempt
def UDdistribution(request):
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    record = [0,0,0,0,0,0,0,0,0,0]
    UpDown = stock_zh_a_spot_em_df.loc[:, ["涨跌幅"]]
    for row in UpDown.iterrows():
        if float(row[1]) < -8:
            record[0] = record[0] + 1
        elif float(row[1]) < -6:
            record[1] = record[1] + 1
        elif float(row[1]) < -4:
            record[2] = record[2] + 1
        elif float(row[1]) < -2:
            record[3] = record[3] + 1
        elif float(row[1]) < 0:
            record[4] = record[4] + 1
        elif float(row[1]) < 2:
            record[5] = record[5] + 1
        elif float(row[1]) < 4:
            record[6] = record[6] + 1
        elif float(row[1]) < 6:
            record[7] = record[7] + 1
        elif float(row[1]) < 8:
            record[8] = record[8] + 1
        elif float(row[1]) >=8:
            record[9] = record[9] + 1
    jsonArr = json.dumps(record, ensure_ascii=False)
    return HttpResponse(jsonArr) # 登录成功

