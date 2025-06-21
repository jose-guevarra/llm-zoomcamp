


es:
	docker run -it \
		--rm \
		--name elasticsearch \
		-m 4GB \
		-p 9200:9200 \
		-p 9300:9300 \
		-e "discovery.type=single-node" \
		-e "xpack.security.enabled=false" \
		docker.elastic.co/elasticsearch/elasticsearch:8.4.3


qdrant:
	docker pull qdrant/qdrant
	docker run -p 6333:6333 -p 6334:6334 \
	-v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
	qdrant/qdrant