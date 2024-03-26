from .base import BaseSolr


class SolrQuery(BaseSolr):
    def add(self, data: list[dict]):
        self.solr_client.add(data)

    def re_index(self):
        pass

    def search(self):
        pass
