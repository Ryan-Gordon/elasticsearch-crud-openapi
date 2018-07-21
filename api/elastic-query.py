from flask_injector import inject
from services.ElasticProvider import ElasticProvider
import flask

from flask import request, Response

'''
ElasticSearch -- Query Operations 

searchDocument -- Searches the instance looking for documents that match the provided query and RETURNS them

deleteByQuery -- Searches the instance looking for documents that match the provided query and DELETES them

Note: The default 'required' arguements such as body/query must come before those which are not required such as index or type
'''

@inject(data_provider=ElasticProvider)
def searchDocument(data_provider, body, index=None, type=None) -> str:
    return data_provider.searchDocument(index, type, body)

@inject(data_provider=ElasticProvider)
def deleteByQuery(data_provider, query, index=None, type=None) -> str:
    return data_provider.deleteByQuery(index, type, query)