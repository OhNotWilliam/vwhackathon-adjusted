from typing import List
from .DocumentLoadingBase import DocumentLoadingBase
from ..helpers.AzureFormRecognizerHelper import AzureFormRecognizerClient
from ..common.SourceDocument import SourceDocument
from typing import List
import re
from langchain.docstore.document import Document
from langchain.document_loaders.csv_loader import CSVLoader
from .DocumentLoadingBase import DocumentLoadingBase
from ..common.SourceDocument import SourceDocument


class CSVDocumentLoading(DocumentLoadingBase):
    def __init__(self) -> None:
        super().__init__()

    def load(self, document_url: str) -> List[SourceDocument]:
        documents: List[Document] = CSVLoader(document_url).load()
        for document in documents:
            if document.page_content == "":
                documents.remove(document)
        source_documents: List[SourceDocument] = [
            SourceDocument(
                content=document.page_content,
                source=document.metadata["source"],
            )
            for document in documents
        ]
        return source_documents
