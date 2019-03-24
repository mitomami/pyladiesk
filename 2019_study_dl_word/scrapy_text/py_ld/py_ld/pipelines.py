# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#
# class PyLdPipeline(object):
#     def process_item(self, item, spider):
#         return item


class ValidationPipeline(object):
    if not item['title']:
        # title フィールドが取得できていない場合は破棄する。
        #DropItem()の因数は破棄する理由を表すメッセージ

        raise DropItem('Missing title')

    return item #itemフィールドが正しく取得できている場合


# class MongoPipeline(object):
#     """
#     itemをMongoDBに保存するPipeline.
#     """
#
#     def open_spider(self, spider):
#         """
#         Spiderの開始時にMongoDBに接続する
#         """
#
#         self.client = MongoClient('localhost', 27017) #ホストとポートを指定してクライアントを作成
#         self.db = self.client['scraping-book'] #scraping-bookデータベースを取得する
#         self.collection = self.db['items'] #itemsコレクションを取得。
#
#     def close_spider(selfself, spider):
#         """
#         Spiderの終了時にMongoDbへの接続を切断する。
#         """
#
#         self.client.close()
#
#     def process_item(self, item, spider):
#         """
#         itemをコレクションに追加する
#         """
#
#         #insert_one()の引数は書き換えられるので、コピーしたdictを渡す
#         self.collection.insert_one(dict(item))
#         return item