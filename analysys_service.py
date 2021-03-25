import json
import xlrd
import pandas as pd

def convertFromExcelToPandas(file):
    try:
        if file:
            if ".xlsx" in file.filename:
                new_file = pd.read_excel(file)
            else:
                new_file = pd.read_csv(file)
            print(new_file)
            return json.dumps({'result' : 'Upload was successful'})
    except Exception as e:
        print(e)
        return json.dumps({'result' : 'Upload was unsuccessful because of error' + str(e)}), 500
