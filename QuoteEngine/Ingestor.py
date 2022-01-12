"""Abstract base class for the IngestInterface abstraction"""

from typing import List
from .IngestorInterface import IngestorInterface
from .IngestorInterface import Text_Ingestor
from .IngestorInterface import CSV_Ingestor
from .IngestorInterface import Docx_Ingestor
from .IngestorInterface import PDF_Ingestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Abstract base class for an ingestor."""

    file_ingestors = [Text_Ingestor, CSV_Ingestor, Docx_Ingestor, PDF_Ingestor] 

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod depending on the files."""
        for file_ingested in cls.file_ingestors:
            if file_ingested.can_ingest(path):
                return file_ingested.parse(path)
