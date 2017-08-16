import json
import requests
from lxml import etree


class LagouSpider():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '26',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'user_trace_token=20170330125354-119edf4114b443a5a6c9b82f2c1dd8ea; LGUID=20170330125355-e0a7006a-1504-11e7-a7f3-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFD8344ACD02F5498F2575326BC8BABB14; _gid=GA1.2.2054137210.1502553258; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500386692,1502026759,1502120687,1502553258; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1502553258; _ga=GA1.2.505722839.1490849635; LGSID=20170812235418-7ffece52-7f76-11e7-a66d-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20170812235418-7ffed07d-7f76-11e7-a66d-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=dbc1a5a76d284ef5aa12c00cfd4432aa',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        # 'X-Anit-Forge-Code': '0',
        # 'X-Anit-Forge-Token': 'None',
        # 'X-Requested-With': 'XMLHttpRequest'
    }
    kds = ['python', 'django', '爬虫', '自然语言处理']

    def request(self):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
        res = requests.post(url, headers=self.headers, data={'first': 'true', 'pn': str(1), 'kd': 'python'})
        print(res.text)
        print(res.cookies)
        return res.json

    def request_get(self):
        url = 'https://www.lagou.com/jobs/3167076.html'
        res = requests.get(url, headers=self.headers)
        print(res.text)
        doc = etree.HTML(res.text)
        title = doc.xpath('//h3[@class="description"]')
        print(title)


if __name__ == '__main__':
    lagou = LagouSpider()
    # data = lagou.request()
    lagou.request_get()
