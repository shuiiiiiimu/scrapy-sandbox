# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from scrapybox.models.investevent import InvestEvent
from scrapybox.models.utils import db_connect


@contextmanager
def session_scope(Session):
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class InvestEventPipeline(object):
    def __init__(self):
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        with session_scope(self.Session) as session:
            session.add(InvestEvent(company=item['company'],
                                    investfirm=item['investfirm'],
                                    round=item['round'],
                                    publish=item['publish']))
