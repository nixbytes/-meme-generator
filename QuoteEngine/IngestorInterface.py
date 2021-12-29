from .QuoteModel import QuoteModel
from typing import List
import subprocess
import os

class IngestorInterface():
    """Class Ingestor."""
    
    def can_ingest(cls, path: str) -> bool:
        pass

    def parse(cls, path: str) -> List[QuoteModel]:
        pass

class Text_Ingestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        with open(path, "r") as text_file:
            quotes = []

            for line in text_file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) is not 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes

class PDF_Ingestor(IngestorInterface):
    pass 


class Docx_Ingestor(IngestorInterface):
    pass


class CSV_Ingestor(IngestorInterface):
    pass