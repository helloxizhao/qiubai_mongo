# qiubai_mongo
本程序简单的编写了将糗事百科的数据爬取下来，然后存入到mongodb中去，在程序的编写的过程中
开始发现生成不了mongodb的collections,后来发现是setting的配置存在问题。
MONGODB_HOST = '192.168.248.131'
MONGODB_PORT= 27017
MONGODB_DBNAME= 'qiubai'
MONGODB_COLLECTION= 'qiubai2'
开始最后的参数写的是MONGODB_DOCNAME后来改为MONGODB_DOCNAME才能正常工作。
另外查看mongodb的可视化客户端利用的是mac端的Toad，此可视化工具需要断开在重新连接才能
展示新生成的collection。
mongo 客户端命令
show dbs (查看数据库)
use  dbname (选中数据库)
show collection(查看数据库中的collection)
