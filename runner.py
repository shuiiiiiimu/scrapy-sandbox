import logging
from scrapybox.spiders.itjuzi import ItjuziSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapybox.models.utils import db_connect
from scrapybox.models.utils import create_table
from scrapybox.models.investevent import InvestEventRule
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    settings = get_project_settings()
    configure_logging(settings)
    engine = db_connect()
    # TODO
    create_table(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rules = session.query(InvestEventRule).filter(InvestEventRule.enable == 1).all()
    session.close()
    runner = CrawlerRunner(settings)

    for rule in rules:
        # stop reactor when spider closes
        # runner.signals.connect(spider_closing, signal=signals.spider_closed)
        runner.crawl(ItjuziSpider, rule=rule)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()
    logging.info('all finished.')
