import time ,datetime
def lastMonth():
    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    return lastMonth.strftime("%B")
def lastMonth_num():
    lastMonth = int(datetime.datetime.now().strftime("%m")) - 1
    if lastMonth < 10:
        return "0" + str(lastMonth)
    else:
        return str(lastMonth)
def thisMonthNumber():
    thisM = datetime.datetime.now().strftime("%m")
    return thisM
def thisYear():
    thisY = datetime.datetime.now().strftime("%Y")
    return thisY

record_path = r"G:\"

#檔案路徑
url = 'https://www.census.gov/manufacturing/m3/prel/pdf/s-i-o.pdf',\
'https://www.census.gov/manufacturing/m3/adv/pdf/durgd.pdf',\
'https://www.census.gov/foreign-trade/Press-Release/current_press_release/ft900.pdf',\
'https://www.census.gov/econ/indicators/advance_report.pdf',\
'https://www.census.gov/wholesale/pdf/mwts/currentwhl.pdf',\
'https://www.bls.gov/news.release/pdf/empsit.pdf',\
'https://www.census.gov/retail/marts/www/marts_current.pdf',\
'https://www.census.gov/services/qss/qss-current.pdf',\
'https://www.census.gov/mtis/www/data/pdf/mtis_current.pdf',\
'https://www.census.gov/housing/hvs/files/currenthvspress.pdf',\
'https://www.census.gov/construction/nrs/pdf/newressales.pdf',\
'https://www.census.gov/construction/nrc/pdf/newresconst.pdf',\
'https://www.census.gov/construction/c30/pdf/release.pdf',\
'https://www.census.gov/econ/bfs/pdf/bfs_current.pdf',\
'https://www.census.gov/econ/qfr/mmws/current/qfr_mg.pdf',\
'https://www.bls.gov/news.release/pdf/cpi.pdf',\
'https://www.bls.gov/news.release/pdf/ximpim.pdf',\
'https://www.federalreserve.gov/releases/g17/current/g17.pdf',\
'https://www.federalreserve.gov/releases/g17/Current/g17_sup.pdf',\
'https://www.federalreserve.gov/releases/g19/current/g19.pdf',\
'https://www.bls.gov/news.release/pdf/eci.pdf',\
'https://www.bls.gov/news.release/pdf/ppi.pdf',\
'https://www.bls.gov/news.release/pdf/prod2.pdf',\
'https://www.bls.gov/news.release/pdf/realer.pdf',\
'https://www.census.gov/econ/qfr/retail/current/qfr_rt.pdf',\
'https://www.ismworld.org/globalassets/pub/research-and-surveys/rob/pmi/rob' + thisYear() + str(int(thisMonthNumber())-1) + 'pmi.pdf',\
'https://www.ismworld.org/globalassets/pub/research-and-surveys/rob/nmi/rob' + thisYear() + str(int(thisMonthNumber())-1) + 'svcs.pdf',\
'https://www.ismworld.org/globalassets/pub/research-and-surveys/rob/hospital/rob' + thisYear() + str(int(thisMonthNumber())-1) + 'hos.pdf',\
'https://www.bls.gov/news.release/pdf/jolts.pdf',\
'https://www.eia.gov/petroleum/supply/weekly/pdf/table1.pdf',\
'https://www.eia.gov/petroleum/supply/weekly/pdf/table3.pdf',\

#hash檔名
fn_hash = 'hashvalue.txt'

#儲存路徑
path = "G:\census\goods",\
"G:\census\Durable Goods MANUFACTURERS SHIPMENTS",\
"G:\goods and services",\
"G:\INTERNATIONAL TRADE DEFICIT",\
"G:\Census\WHOLESALE INVENTORIES",\
r"G:\bls\EMPLOYMENT",\
"G:\Census\\retail sale",\
"G:\Census\Quarterly Services",\
"G:\Census\Manufacturing and Trade Inventories and Sales",\
"G:\RESIDENTIAL VACANCIES AND HOMEOWNERSHIP",\
r"G:\new sales",\
"G:\\new construction",\
"G:\construction spending",\
"G:\\business formation",\
"G:\SP500\Manufacturing, Mining, Trade, and Selected Service Industries",\
"G:\cpi",\
"G:\import and export price",\
"G:\production index",\
"G:\production index sup",\
"G:\Consumer Credit",\
"G:\eci",\
"G:\ppi",\
"G:\PRODUCTIVITY AND COSTS",\
"G:\\realer",\
"G:\Census\\retail trade",\
"G:\ISM\manufacture",\
r"G:\ISM\service",\
r"G:\ISM\hospital",\
r"G:\bls\OPENINGS",\
r"G:\EIA\crude oil",\
r"G:\EIA\refinery",\

#nyfed
path_nyfed = r"G:\NYFED\snapshot"
url_nyfed = "https://www.newyorkfed.org/research/snapshot"

#adp
path_adp = r"G:\adp"
url_adp = "https://adpemploymentreport.com/"
