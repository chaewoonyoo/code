import requests
import pandas as pd
import xml.etree.ElementTree as ET
from google.colab import userdata

API_KEY = userdata.get("KEY")

url = "http://www.kopis.or.kr/openApi/restful/prfstsCate"

params = {
    "service": API_KEY,
    "stdate": "20230601",
    "eddate": "20230630",
}

response = requests.get(url, params=params)

root = ET.fromstring(response.text)

row_dict = {'cate': [], 'amount': [], 'nmrs': [], 'prfdtcnt': [], 'nmrsshr': [], 'prfprocnt': [], 'amountshr': []}

for item in root.findall("./prfst"):
    for child in item:
        if child.tag in row_dict:
            row_dict[child.tag].append(child.text)

df = pd.DataFrame(row_dict)

df.head()
