import os
from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
import connexion
from services.ElasticProvider import ElasticProvider

# Connexion can only receive 2 params
#application = connexion.App(__name__, specification_dir='swagger/')

#Setup with Swagger and RestyResolver

def configure(binder: Binder) -> Binder:
    binder.bind(
        ElasticProvider
    )


if __name__ == '__main__':
    
    #Redefine application as a connexion app. 
    application = connexion.App(__name__, specification_dir='swagger/')

    application.add_api('elastic-crud-openapi.yaml', resolver=RestyResolver('api'))

    #FlaskInjector Setup defined after configure
    FlaskInjector(app=application.app, modules=[configure])
    #Start the flask server on either a predefined port from the host machine or 2025
    application.run(debug=True, \
        #server='tornado', 
        port=int(os.environ.get('PORT', 2025)))