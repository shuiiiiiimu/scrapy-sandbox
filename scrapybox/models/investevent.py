# -*- encoding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from scrapybox.models.utils import Base


class InvestEventRule(Base):
    __tablename__ = 'investevent_rules'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    allow_domains = Column(String(100))
    start_urls = Column(String(100))  # 开始URL列表，逗号隔开
    next_page = Column(String(100))
    extract_content = Column(String(100))  # 提取区域，比如选择 ul , xpath 则相对 ul 下是 li
    company_xpath = Column(String(100))
    investfirm_xpath = Column(String(100))
    round_xpath = Column(String(100))
    publish_xpath = Column(String(100))
    enable = Column(Integer)  # 规则是否生效


class InvestEvent(Base):
    __tablename__ = 'investevents'

    id = Column(Integer, primary_key=True)
    company = Column(String(100))
    investfirm = Column(String(100))
    round = Column(String(100))
    publish = Column(String(100))
