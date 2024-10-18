import requests
from requests import Response

def main():
    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=5481753E-52AF-40DA-9A8A-9E192B245E13'
    res:Response=requests.request("get",url)
    if res.status_code == 200:
        print("下載成功")
        res.encoding = "utf-8"
        content:str = res.text
        print(content)
        with open('A1.csv',"w",encoding="utf8",newline="") as file:
            print(type(file))
            file.write(content)
    else:
        print("下載失敗")

if __name__ == '__main__':
    main()