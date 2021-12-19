class QuoteModel:
    """Class Quote: Base class for a quote."""

    def __init__(self, body: str, author: str) -> None:
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """return string of the data (body text - author)"""
        return f"{self.body} {self.author}"
