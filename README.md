
# ElasticSearch CRUD OpenAPI
The repo lets you visually send HTTP requests to your ElasticSearch Datastore using its REST API.

Alternatively you can use it to relay requets from your ElasticSearch as a Gateway

#### Supported Functions
##### CRUD
Create, Read, Update, Delete --> All 4 are supported. Most of these require an index,doc_type and ID.

Query Functions:
Search --> search the elastic db for documents which match your provided query
DeleteByQuery --> delete documents in the elastic db using a search query rather than specifying an ID 
## Installation
You have two options in how you want to run this application. Standalone with python 3 or through a Docker container

### Setting up with Docker:
The repo comes with a Dockerfile which is a great way to get set up quickly with a container you can destroy when done.

To build an image from Dockerfile  
`docker build -t ryangordon/elasticsearch-crud-api . `  
Then run your image :  
`docker run -p 2025:2025 -e ELASTICSEARCH_URL="<YOUR_ES_URL>"  ryangordon/elasticsearch-crud-api`  

*NOTE* If you are running your ES instance on localhost you may need to do one of the steps in the Notes section.

### Setting up with just python

If you are running with python by itself, you may need to specify the location of the Elasticsearch instance. The default is `http://localhost:9200` which is also the default used by Elastic. Not specifying will mean the API will try to use this.
To set a different a different instance run this in terminal :  

```bash
export ELASTICSEARCH_URL="<YOUR_ES_URL>"
```


### Notes:
If you are connecting to an Elasticsearch instance on your `localhost` and using docker you may need to do one of the following:

+ Connect to your machines IP instead of localhost -> this involves connecting to some IP like `192.168.1.X`. You can find your IP with `ifconfig`
+ Use the arguement `--net="host"` in your docker run command. Then [your docker container will point to your docker host.](https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach)
+ Connect to the special DNS name `host.docker.internal` which should point to your machines localhost. You still need to specify port