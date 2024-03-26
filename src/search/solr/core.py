import docker
from loguru import logger
from fastapi.exceptions import HTTPException

from .base import BaseSolr


class SolrCore(BaseSolr):
    def create_collection(self):
        is_core_exists = self._ping_core()
        if is_core_exists is True:
            self._delete_core()

        self._create_core()

    def _ping_core(self) -> bool:
        try:
            self.solr_client.ping()
            return True
        except Exception as e:
            logger.exception(f"An error occurred while pinging solr core {str(e)}")
            return False

    def _create_core(self):
        status = (
            docker.from_env()
            .containers.get("solr_client")
            .exec_run(f"solr create -c {self.CORE_NAME}")
        )
        if status.exit_code != 0:
            raise HTTPException(status_code=500, detail="Could not create solr core.")

    def _delete_core(self) -> bool:
        status = (
            docker.from_env()
            .containers.get("solr_client")
            .exec_run(f"solr delete -c {self.CORE_NAME}")
        )
        if status.exit_code != 0:
            raise HTTPException(status_code=500, detail="Could not delete solr core.")
