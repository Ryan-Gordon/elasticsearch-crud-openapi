from flask_injector import inject
from services.ElasticProvider import ElasticProvider
import flask

from flask import request, Response


@inject(data_provider=ElasticProvider)
def heartbeat(data_provider) -> str:
    return data_provider.heartbeat()

@inject(data_provider=ElasticProvider)
def insertDocument(data_provider,index, type, body,id=None) -> str:
    return data_provider.insertDocument(index, type, body,id)

@inject(data_provider=ElasticProvider)
def searchDocument(data_provider,index, type, body) -> str:
    return data_provider.searchDocument(index, type, body)