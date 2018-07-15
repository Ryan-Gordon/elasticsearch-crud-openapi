from flask_injector import inject
from services.ElasticProvider import ElasticProvider
import flask

from flask import request, Response

'''
Util operations

Heartbeat -- ensures the instance is still live
'''
@inject(data_provider=ElasticProvider)
def heartbeat(data_provider) -> str:
    return data_provider.heartbeat()

'''
ElasticSearch -- CRUD Operations 

insertDocument -- Attempts to index the provided document

getDocumentById -- Attempts to find a document with provided index,type and id

deleteDocumentById -- Attempts to delete a document with provided index,type and id

updateDocumentById -- Attempts to find a document with provided index,type and id and then updates it with the contents of body
'''
@inject(data_provider=ElasticProvider)
def insertDocument(data_provider,index, type, body,id=None) -> str:
    return data_provider.insertDocument(index, type, body,id)

@inject(data_provider=ElasticProvider)
def getDocumentById(data_provider,index, type, id) -> str:
    return data_provider.getDocumentById(index, type, id)

@inject(data_provider=ElasticProvider)
def deleteDocumentById(data_provider,index, type, id) -> str:
    return data_provider.deleteDocumentById(index, type, id)

@inject(data_provider=ElasticProvider)
def updateDocumentById(data_provider,index, type, id, body=None) -> str:
    return data_provider.updateDocumentById(index, type, id, body)





