import os
from injector import Binder
from flask_injector import FlaskInjector
from services.ElasticProvider import ElasticProvider
import connexion
from connexion.resolver import RestyResolver
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)
'''
Injector is used bind a instance of ElasticProvider 
We bind the injected ElasticProvider to this initialised ElasticPpovider which which holds the server url
'''
def configure(binder: Binder) -> Binder:
    binder.bind(
        ElasticProvider, to=ElasticProvider(host = os.environ.get('ELASTICSEARCH_URL',"http://localhost:9200"))
    )

#Redefine application as a connexion app. 
application = connexion.App(__name__, specification_dir='swagger/')

# Setip RestyResolver and the OpenAPI docs
application.add_api('elastic-crud-openapi.yaml', resolver=RestyResolver('api'), arguments={'title': 'ElasticSearch OpenAPI'})

#FlaskInjector Setup defined after configure
FlaskInjector(app=application.app, modules=[configure])

if __name__ == '__main__':
    
    #Start the flask server on either a predefined port from the host machine or 2025
    application.run(debug=False, \
        #server='tornado', 
        port=int(os.environ.get('PORT', 2025)))