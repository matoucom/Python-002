# -*- coding: utf-8 -*-

# 安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
cookie = '__mta=50221593.1595494887043.1595494887043.1595497086353.2; uuid_n_v=v1; uuid=161BC870CCC311EA9DCC5DD453C9604E3E40326FE62D4B948818425CF525891F; _csrf=1863dba3df1c82f9c414c308ce99bedac4b63fe82f8aea72f44e840c825c1377; _lxsdk_cuid=1737ae7ed9bc8-0e2d21e998a24d-39647b08-1fa400-1737ae7ed9bc8; _lxsdk=161BC870CCC311EA9DCC5DD453C9604E3E40326FE62D4B948818425CF525891F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595494887; mojo-uuid=64e19b1d874f43cb48d95bab68ae2bba; mojo-session-id={"id":"f2a9f8290722f0bbe5d90f337cb92a4b","time":1595503892848}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595503893; __mta=50221593.1595494887043.1595497086353.1595503893121.3; mojo-trace-id=2; _lxsdk_s=1737b715224-352-c05-8a3%7C%7C3'
header = {'user-agent': user_agent, 'Cookie': cookie}

myurl = "https://maoyan.com/films?showType=3"

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')

# print(response.text)

film_list = []
i = 0
for tag in bs_info.find_all('div', attrs={'class':'movie-hover-info'}):
    if i < 10:
        child_tag = tag.find_all('div', attrs={'class':'movie-hover-title'})
        # film_name = child_tag[0].find('span', attrs={'class':'name'}).text
        film_name = child_tag[0].text.strip().split('\n')[0]
        # film_score = child_tag[0].text.strip().split('\n')[-1]
        # film_type = child_tag[1].text.replace('\n', '').split(':')[1].strip()
        # print('1', film_type)
        # film_type = child_tag[1].text.replace('\n', '').split(':')[1]
        # print('2', film_type)
        # film_type = child_tag[1].text.replace('\n', '').split(':')
        # print('3', film_type)
        # film_type = child_tag[1].text.replace('\n', '')
        # print('4', film_type)
        # film_type = child_tag[1].text
        # print('5', film_type)
        # film_type = child_tag[1]
        # print('6', film_type)
        # film_type = child_tag
        # print('7', film_type)
        film_type = child_tag[1].text.replace('\n', '').split(':')[1].strip()
        # film_starring = child_tag[2].text.replace('\n', '').split(':')[1].strip()
        film_time = child_tag[3].text.replace('\n', '').split(':')[1].strip()
        film_list.append({
            "电影名称": film_name,
            # "评分": film_score,
            "类型": film_type,
            # "主演": film_starring,
            "上映时间": film_time,
        })
        i = i + 1
    else:
        break
df_result = pd.DataFrame(data = film_list)
df_result.to_csv('./movie1.csv', encoding='utf-8', index=True, header=True)
# df_result.head()
# print(film_list)




# for child in bs_info.find_all("div",class_='movie-hover-title'):
#     child.span.decompose()
#     print(child.text)
#
# film_name = []
# rating = []
#
# for tag in bs_info.find_all('div', attrs={'class':'movie-hover-info'}):
#     # print(tag.text.replace('\n', '').replace('              ', ' '))
#     for atag in tag.find_all('span', attrs={'class':'name'}):
#         # print(atag.text)
#         film_name.append(atag.text)
#     for itag in tag.find_all('i', attrs={'class':'integer'}):
#         for fratag in tag.find_all('i', attrs={'class':'fraction'}):
#             # print(itag.text + fratag.text)
#             rating.append(itag.text + fratag.text)
#
# print(film_name, rating)