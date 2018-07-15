import os
import requests
import flask
import redis
import datetime
import json

from elasticsearch import Elasticsearch

class ElasticProvider(object):
    def __init__(self,host):
        self.conn = Elasticsearch([host])
        #self.conn = Elasticsearch(["http://localhost:9200"])
        

    def heartbeat(self) -> str:

        return "Success", 200

    def insertDocument(self, index, type, body,id):
        
        return self.conn.index(index=index, doc_type=type, body=body, id=id)
    def searchDocument(self, index, type, body):
        return self.conn.search(index=index, doc_type=type, body=body)