from .QuoteModel import QuoteModel
from typing import List
from abc import ABC, abstractmethod
import subprocess
import os
import docx
import pandas
import random


class IngestorInterface(ABC):
    """Class Ingestor."""
    file_extensions = list()
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if quote file can be ingested using file_extensions"""
        extension = path.split('.')[-1]
        return extension in cls.file_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstracmethod is the main Class"""
        pass

class Text_Ingestor(IngestorInterface):
    """The class that ingests info from text files."""
    file_extensions = ['txt']

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
    """The class that ingests info from pdf files."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./content/{random.randint(0,100000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        with open(tmp, "r") as file:
            quotes = []

            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        os.remove(tmp)
        return quotes


class Docx_Ingestor(IngestorInterface):
    """The class that ingests info from docx files."""
    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        try:
            quotes = []
            doc_file = docx.Ddocument(path)

            for listing in doc_file.paragraphs:
                if listing.text != "":
                    parse = listing.text.replace('\"', '').split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        except Exception as e:
            raise Exception("cannot parse docx file")

        return quotes


class CSV_Ingestor(IngestorInterface):
    """The class that ingests info from csv files."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest csv file')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes