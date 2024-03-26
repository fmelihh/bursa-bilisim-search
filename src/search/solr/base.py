from pysolr import Solr


class BaseSolr:
    CORE_NAME = "test"

    def __init__(self):
        self._solr_client = None

    @property
    def solr_client(self) -> Solr:
        if not self._solr_client:
            self._solr_client = Solr(
                f"http://0.0.0.0:8983/solr/{self.CORE_NAME}", always_commit=True
            )
        return self._solr_client
