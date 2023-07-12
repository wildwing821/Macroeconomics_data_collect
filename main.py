# download census data
import json,random
import hashlib,pdb,bs4
import time ,datetime ,os ,requests
import traceback,pdb
import file_url_list

#header
my_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3;zh-tw',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Host':None
}


#pdb.set_trace()
#ADP 每年一月要抓
def delay_job():
        num = random.randint(1, 5)
        time.sleep(num)

def dl_record(text):
    os.chdir(file_url_list.record_path)
    if os.path.exists(file_url_list.record_path):
        with open("dl_record.txt", 'a', encoding="utf8") as f:
            f.write(str(datetime.date.today()))
            f.write(text)            # 寫入檔案至pdf
            f.write('\n')
            f.close()
    else:
        with open("dl_record.txt", 'w', encoding="utf8") as f:
            f.write(str(datetime.date.today()))
            f.write(text)            # 寫入檔案至pdf
            f.write('\n')
            f.close()
def getSoup(url,header):
        html = requests.get(url,headers = header,timeout=5)
        if html.status_code != 200:
            print('invalid url:', html.url)
            print(html.status)
        objSoup = bs4.BeautifulSoup(html.text, 'lxml')         # 取得HTML
        return objSoup

def save_newaqi(aqijsons):
    '''儲存'''
    with open(fn + '.pdf', 'wb') as f:
        f.write(aqijsons.content)            # 寫入檔案至pdf
        f.close()
def save_hashvalue(newhash):
    '''儲存哈希值至hashvalue.txt'''
    with open(file_url_list.fn_hash, 'w') as fileobj:
        fileobj.write(newhash)                  # 寫入哈希值至hashvalue.txt
        fileobj.close()
def cal_hashvalue(aqijsons):
    ''' 計算hash value'''
    data = hashlib.md5()
    data.update(aqijsons.text.encode('utf-8'))
    hashdata = data.hexdigest()
    return hashdata                             # 傳回哈希值


 # 檔案名稱
fn = time.strftime("%Y%m%d")

def download_check(url,path):
    os.chdir(path)
    try:
        aqijsons = requests.get(url,headers = my_header)                # 將檔案下載至aqijsons
        #print(aqijsons.status_code)
        if aqijsons.status_code == 200:
            if os.path.exists(file_url_list.fn_hash):                     # 如果hashvalue.txt存在
                newhash = cal_hashvalue(aqijsons)                   # 計算新的哈希值hashvalue
                # 開啟hashvalue.txt檔案
                with open(file_url_list.fn_hash, 'r') as fnObj:           # 讀取舊的哈希值
                    oldhash =  fnObj.read()
                    if newhash == oldhash:                      # 比對新舊哈希值
                        #print(path[i])
                        fnObj.close()
                    else:
                        print('資料已經更新')
                        save_newaqi(aqijsons)                           # 儲存pdf
                        save_hashvalue(newhash)                        # 儲存哈希值至hashvalue.txt
                        fnObj.close()
                        dl_record(path)
                        print(path)
            else:                                           # 如果hashvalue.txt不存在
                newhash = cal_hashvalue(aqijsons)
                print('第一次啟動此程式')
                print('哈希值 = ', newhash)
                save_hashvalue(newhash)                            # 儲存哈希值至hashvalue.txt
                save_newaqi(aqijsons)                               # 儲存pdf
                dl_record(path)
        else:
            print("request error:",url)
    except Exception as err:
        print('下載失敗')
        print(path)
        traceback.print_exc()

for i in range(len(file_url_list.path)):
    download_check(file_url_list.url[i],file_url_list.path[i])
    delay_job()


#nyfed
all_links = getSoup(file_url_list.url_nyfed,my_header).find_all('a')

for link in all_links:
    #print(datetime.datetime.now().strftime("%B").lower())
    compare_str = link.get("href")
    if compare_str is None:
        #print("none")
        pass
    elif file_url_list.thisYear() in compare_str and "snapshot" in compare_str and datetime.datetime.now().strftime("%B") in compare_str :
        download_link = 'https://www.newyorkfed.org' + link.get("href")  
        download_check(download_link,file_url_list.path_nyfed)
        break
delay_job()

#pdb.set_trace()


all_links = getSoup(file_url_list.url_adp,my_header).find_all('a')
for link in all_links:
    compare_str = link.get("href")
    if compare_str is None:
        pass
    elif file_url_list.thisYear() in compare_str and "pdf" and "EMPLOYMENT_REPORT" in compare_str :
        download_link = link.get("href") 
        download_check(download_link,file_url_list.path_adp)
        break


#input('Press Enter to continue...')
