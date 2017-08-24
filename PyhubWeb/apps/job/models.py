# from django.db import models
from mongoengine import *
from PyhubWeb.settings import DBNAME

connect(DBNAME)

class Jobs(Document):
    city = StringField()
    district = StringField()
    business_zones = ListField()
    job_address = StringField()
    company_id = IntField()
    company_full_name = StringField()
    company_short_name = StringField()
    company_logo = URLField()
    company_label = ListField()
    company_size = StringField()
    pub_time = DateTimeField()
    finance_stage = StringField()
    industry_field = StringField()
    industry_labels = ListField()
    job_nature = StringField()
    position_advantage = StringField()
    position_id = IntField()
    position_labels = StringField()
    position_name = StringField()
    salary = StringField()
    job_type = StringField()
    work_year = StringField()
    education = StringField()
    is_school_job = IntField()
    job_detail = StringField()
    company_link = URLField()
    source = StringField()

    meta = {'collection': 'jobs'}  # 指明连接数据库的哪张表

# for i in Jobs.objects[:10]:  # 测试是否连接成功
#     print(i.position_name)