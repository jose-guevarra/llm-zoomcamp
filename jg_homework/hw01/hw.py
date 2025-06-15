from elasticsearch import Elasticsearch

es_client = Elasticsearch('http://localhost:9200')
#es_client = Elasticsearch([{'host': 'localhost', 'port': 9200}])



if es_client.ping():
    print("Connected to Elasticsearch")
else:
    print("Failed to connect to Elasticsearch")