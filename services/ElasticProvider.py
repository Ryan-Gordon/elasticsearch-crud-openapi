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

    def getDocumentById(self, index, type, id):
        return self.conn.get(index=index, doc_type=type, id=id)
    
    def deleteDocumentById(self, index, type, id):
        return self.conn.delete(index=index, doc_type=type, id=id)

    def updateDocumentById(self, index, type,id, body):
        return self.conn.update(index=index, doc_type=type, id=id, body={"doc":body})

    
    '''
    Query Operations 
    Includes :
    search -- Allows a user to search using a query
    deleteByQuery -- allows a user to delete documents by specifying a query rather than an ID
    '''

    def searchDocument(self, index, type, body):
        return self.conn.search(index=index, doc_type=type, body=body)

    def deleteByQuery(self, index, type, query):
        return self.conn.delete_by_query(index=index, doc_type=type, body=query)

