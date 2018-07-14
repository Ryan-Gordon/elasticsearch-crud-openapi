from flask_injector import inject
from services.ElasticProvider import ElasticProvider
import flask

from flask import request, Response


@inject(data_provider=ElasticProvider)
def heartbeat(data_provider) -> str:
    return data_provider.heartbeat()