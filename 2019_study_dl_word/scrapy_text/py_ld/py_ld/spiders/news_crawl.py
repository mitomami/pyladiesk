from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor


from py_ld.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = "news_crawl" #spiderの名前
    #クロール対象とするドメインのリスト
    allowed_domains = ["news.yahoo.co.jp"]
    #クロールを開始するURLのリスト 1要素のタプルは末尾にカンマをつける。
    start_urls = (
        'https://news.yahoo.co.jp/',
    )



    rules = (
        #トピックスのページへのリンクをたどり、レスポンスをparse_topics（）メソッドで処理する
            Rule(LinkExtractor(allow=r'/pickup/\d+$'),callback='parse_topics'),
    )

    def parse_topics(self,response):
        """
        トピックスのページからタイトルと本文を抜き出す。
        cssで抜き出す対象を特定し、extract_firstで文字列のリストにした後、最初の要素を取り出す。
        xpath('string()')はp,brタグなどが入っていると、全てを抜き出せない場合はXpathで文字だけ抜き出せます。
        """

        item = Headline()

        item['title'] = response.css('.tpcNews_title ::text').extract_first()  # タイトル
        item['body'] = response.css('.tpcNews_summary').xpath('string()').extract_first()  # 本文

        yield item