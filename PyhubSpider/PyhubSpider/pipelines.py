from pymongo import MongoClient
from PyhubSpider.items import QuestionItem, ArticleItem, JobItem


class PyhubPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['pyhub']
        self.questions = db['questions']
        self.articles = db['articles']
        self.jobs = db['jobs']

    def process_item(self, item, spider):
        if isinstance(item, QuestionItem):
            self.questions.find_one_and_update(
                {'url': item['url']},
                {'$set': {'title': item['title'], 'content': item['content'], 'answers': item['answers'],
                          'answer_count': item['answer_count'], 'view_count': item['view_count'],
                          'vote_count': item['vote_count'], 'is_solved':item['is_solved'], 'url':item['url'],
                          'tags': item['tags'], 'source': item['source']
                         }
                 },
                upsert=True
            )
        elif isinstance(item, ArticleItem):
            self.articles.find_one_and_update(
                {'url': item['url']},
                {'$set': {'title': item['title'], 'content': item['content'], 'url': item['url'],
                          'tags': item['tags'], 'source': item['source'], 'pub_date': item['pub_date']}
                 },
                upsert=True
            )

        elif isinstance(item, JobItem):
            # self.articles.find_one_and_update(
            #     {'position_id': item['position_id']},
            #     {'$set': {'title': item['title'], 'content': item['content'], 'url': item['url'],
            #               'tags': item['tags'], 'source': item['source'], 'pub_date': item['pub_date']}
            #      },
            #     upsert=True
            # )
            self.jobs.update({'position_id': item['position_id']}, item, True)

        return item