import gspread
import json


def teamlist():
    gc = gspread.service_account(filename='credentials.json')
    sh = gc.open_by_key('1N7wnIRWJRbULKychJU-EOyisuZBX1rgXwdW91Keki4M')

    worksheet = sh.sheet1

    res = worksheet.col_values(1)
    res2 = worksheet.col_values(2)

    #res4 = worksheet.get_all_values()
    #print({z[0]:list(z[1:]) for z in zip(*res4)})

    res3 = dict(zip(res, res2))
    return res3