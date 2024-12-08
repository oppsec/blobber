""" 
This module aims to enumerate and get Name, Last-Modified, Content-Length and Content-Typpe blob value.
"""

from lxml import etree
from rich.console import Console
console = Console()

def blob_handler(content: str, file_filter: str) -> None:
    try:
        content_bytes = content.encode('utf-8')
        root = etree.fromstring(content_bytes)
        
        blobs = root.xpath(".//Blob")
        if not blobs:
            console.print("[[yellow]![/]] Nenhum blob encontrado.")
            return
        
        for blob in blobs:
            url_element = blob.find("Url")
            url = url_element.text.strip() if url_element is not None else "N/A"

            file_name = blob.findtext(".//Name", default="N/A").strip()
            last_modified = blob.findtext(".//Last-Modified", default="N/A").strip()
            content_length = blob.findtext(".//Content-Length", default="N/A").strip()
            content_type = blob.findtext(".//Content-Type", default="N/A").strip()

            if file_filter == None:
                console.print(f"[[green]+[/]] URL: {url}\n  \\_ Name: {file_name}\n  \\_ Last Modified: {last_modified}\n  \\_ Content-Length: {content_length}\n  \\_ Content-Type: {content_type}", highlight=False)
                console.print("-" * 50, "\n")

            if not file_filter == None:
                if file_name.endswith(file_filter):
                    console.print(f"[[green]+[/]] URL: {url}\n  \\_ Name: {file_name}\n  \\_ Last Modified: {last_modified}\n  \\_ Content-Length: {content_length}\n  \\_ Content-Type: {content_type}", highlight=False)
                    console.print("-" * 50, "\n")
                else:
                    pass

    except Exception as error:
        console.print(f"[[red]![/]] Erro ao processar blobs: {error}")


