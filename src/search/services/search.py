import io
import pandas as pd

from ..solr import SolrCore


class SearchService:
    def __init__(self):
        self._solr_core = None

    @property
    def solr_core(self) -> SolrCore:
        if not self._solr_core:
            self._solr_core = SolrCore()

        return self._solr_core

    def upload(self, file_content: bytes):
        file_io = io.StringIO(file_content.decode("utf-8"))
        df = pd.read_csv(file_io, sep=",")
        del df["Unnamed: 0"]

        self.solr_core.create_collection()
