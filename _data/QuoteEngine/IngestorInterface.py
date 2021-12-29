from .QuoteModel import QuoteModel

class IngestorInterface():
    """Class Ingestor."""
    
    def can_ingest(cls, path: str) -> bool:
        pass
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

