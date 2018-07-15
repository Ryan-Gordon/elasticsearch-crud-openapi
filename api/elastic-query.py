from flask_injector import inject
from services.ElasticProvider import ElasticProvider
import flask

from flask import request, Response

'''
ElasticSearch -- Query Operations 

searchDocument -- Searches the instance looking for documents that match the provided query and RETURNS them

deleteByQuery -- Searches the instance looking for documents that match the provided query and DELETES them
'''

@inject(data_provider=ElasticProvider)
def searchDocument(data_provider,index, type, body) -> str:
    return data_provider.searchDocument(index, type, body)

@inject(data_provider=ElasticProvider)
def deleteByQuery(data_provider,index, type, query) -> str:
    return data_provider.deleteByQuery(index, type, query)