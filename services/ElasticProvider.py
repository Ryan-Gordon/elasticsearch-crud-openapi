import os
import requests
import flask
import redis
import datetime
import json

class ElasticProvider(object):

    def heartbeat(self) -> str:

        return "Success", 200