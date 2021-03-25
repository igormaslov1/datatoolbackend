

def convertFromExcelToPandas(file):
    try:
        if file:
            if type(file) == str:
                import xlrd
                workbook = xlrd.open_workbook(file)
            else:
                import xlrd
                workbook = xlrd.open_workbook(file_contents=file.read())
            console.log(workbook)
            print(workbook)
            return json.dumps({'result' : 'Upload was successful'})
    except Exception as e:
        print(e)
        return json.dumps({'result' : 'Upload was unsuccessful because of error' + str(e)}), 500
