import re
import math
import json
import scrapy
from urllib.parse import urljoin
from scrapy.http import Request
from scrapy.selector import Selector
from PyhubSpider.items import JobItem


class LagouSpider(scrapy.Spider):
    name = "lagou"
    # allowed_domains = ["lagou.com"]

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '26',  # 加上这个总是302，不知怎么回事
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        # 'X-Anit-Forge-Code': '0',
        # 'X-Anit-Forge-Token': 'None',
        # 'X-Requested-With': 'XMLHttpRequest'
    }
    kds = ['python', 'django', '爬虫', '自然语言处理']
    pages = 1

    def start_requests(self):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
        for page in range(1, self.pages+1):
            yield scrapy.FormRequest(
                url,
                headers=self.headers,
                formdata={'first': 'true', 'pn': str(page), 'kd': 'python'},
                callback=self.parse_index
            )


    def parse_index(self, response):
        print(response.text)
        result = json.loads(response.text)
        jobs = result['content']['positionResult']
        job_num = jobs['totalCount']
        self.pages = math.ceil(job_num/15)
        jobs = jobs['result']
        for job in jobs:
            item = JobItem()
            item['city'] = job['city']
            item['business_zones'] = job['businessZones']
            item['district'] = job['district']
            item['company_id'] = job['companyId']
            item['company_full_name'] = job['companyFullName']
            item['company_short_name'] = job['companyShortName']
            item['company_logo'] = 'https://static.lagou.com/thumbnail_120x120/'+job['companyLogo'] if job['companyLogo'] else ''
            item['company_label'] = job['companyLabelList']
            item['company_size'] = job['companySize']
            item['pub_time'] = job['createTime']
            item['finance_stage'] = job['financeStage']
            item['industry_field'] = job['industryField']
            item['industry_labels'] = job['industryLables']
            item['job_nature'] = job['jobNature']
            item['position_advantage'] = job['positionAdvantage']
            item['position_id'] = job['positionId']
            item['position_labels'] = job['positionLables']
            item['position_name'] = job['positionName']
            item['salary'] = job['salary']
            item['job_type'] = [job.get('firstType', '')]+[job.get('secondType', '')]
            item['work_year'] = job['workYear']
            item['education'] = job['education']
            item['is_school_job'] = job['isSchoolJob']
            item['source'] = 'lagou'
            # yield item
            yield Request(
                url='https://www.lagou.com/jobs/{}.html'.format(item['position_id']),
                headers=self.headers,
                meta={'item': item},
                callback=self.parse_detail
            )


    def parse_detail(self, response):
        selector = Selector(response)
        print(response.url)
        # print(response.text)
        item = response.meta['item']
        item['job_detail'] = selector.xpath('//dd[@class="job_bt"]//*').extract()
        job_address = selector.xpath('//div[@class="work_addr"]//text()').extract()
        job_address = [a.strip() for a in job_address if a.strip()]
        job_address = ''.join(job_address).strip().strip('查看地图')
        item['job_address'] = job_address
        item['company_link'] = selector.xpath('//i[@class="icon-glyph-home"]/following-sibling::a[1]/text()').extract_first()
        yield item
