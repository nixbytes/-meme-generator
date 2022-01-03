"""Abstract base class for the IngestInterface abstraction"""

from typing import List
from .IngestorInterface import IngestInterface
from .IngestorInterface import Text_Ingestor
from .QuoteModel import QuoteModel


class Ingestor(IngestInterface):
    """Abstract base class for an ingestor."""

    file_ingestors = [Text_Ingestor] 

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod depending on the files."""
        for file_ingested in cls.file_ingestors:
            if file_ingested.can_ingest(path):
                return file_ingested.parse(path)
