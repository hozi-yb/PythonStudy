import requests
import pandas as pd

"""  종관기상자료(ASOS)  일자료 받아오기.
"""

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params = {'serviceKey': 'j1BP7pVQ3vWfMhTNzePDluGdwtVIcmq08X8c7T5Ean/bPWph1EXT0T2R/qCF2E9/18IrWnV9AkzvcXon0ceXAw==',
          'pageNo': '1',  # 페이지 수
          'numOfRows': '10',  # 한 페이지당 표출 데이터 수
          'dataType': 'JSON',
          'dataCd': 'ASOS',
          'dateCd': 'DAY',
          'startDt': '20200101',  # 시작날짜
          'endDt': '20201231',  # 마지막날짜
          'stnIds': '108'  # 기상관측 지점 지역코드
          }

# 위도경도
latlon = {
    "속초": ["38.25085", "128.56473"],
    "북춘천": ["37.94738", "127.75443"],
    "": ["", ""],
}

response = requests.get(url, params=params)

data_json = response.json()
data_item = data_json["response"]["body"]["items"]["item"]

data_df = pd.DataFrame(data_item)

Gsr_data_df = data_df[["stnNm", "tm", "sumGsr"]]  # 컬럼 - 지점명, 날짜, 합계일사량

print(Gsr_data_df.to_string(index=False))

# print(response)
