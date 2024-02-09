Created a test cluster in Qdrant Cloud 
Then ran the following command in Postman to create 4 shards so the script could return something

PUT collections/test_collection
    { 
        "vectors": {
          "size": 300,
          "distance": "Cosine"  
        },
        "shard_number": 4
    }

Verified that shards were created succesfully in the Cloud Dashboard and also via another HTTP request

GET collections/test_collection/cluster

Which returned info about the clusters shards that I used to craft the python script 
Example Return Truncated:

{
  "result": {
    "peer_id": 7372175007760011,
    "shard_count": 4,
    "local_shards": [
      {
        "shard_id": 0,
        "points_count": 0,
        "state": "Active"
      },

