# from django.db import models
from mongoengine import *
from PyhubWeb.settings import DBNAME

connect(DBNAME)

class Articles(Document):
    # _id = StringField(primary_key=True)
    url = URLField()
    title = StringField()
    content = StringField()
    tags = ListField()
    source = URLField()
    pub_date = DateTimeField()

    meta = {'collection': 'articles'}  # 指明连接数据库的哪张表

# for i in Articles.objects[:10]:  # 测试是否连接成功
#     print(i.title)