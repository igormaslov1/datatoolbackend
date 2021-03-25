import json
import xlrd
import pandas as pd

def convertFromExcelToPandas(file):
    try:
        if file:
            csv = pd.read_csv(file)
            print(csv)
            return json.dumps({'result' : 'Upload was successful'})
    except Exception as e:
        print(e)
        return json.dumps({'result' : 'Upload was unsuccessful because of error' + str(e)}), 500
