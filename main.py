import uvicorn

from src.search.api.app import backend_app

# SOLR_CONNECTION_URL = "http://solr_client:8983/solr/{core_name}"
# SOLR_ADMIN_CONNECTION_URL = "http://solr_client:8983/solr/admin/cores"

if __name__ == "__main__":
    print("test")
    uvicorn.run(backend_app, host="0.0.0.0", port=9001)
