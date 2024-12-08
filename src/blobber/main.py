from rich.console import Console
console = Console()

import argparse

from blobber.ui.banner import get_banner
from blobber.modules.status import request
from blobber.modules.blobs import blob_handler

def initialize() -> None:
    """ Initiates Blobber """
    get_banner()

    parser = argparse.ArgumentParser(
        prog='Blobber',
        description='Attacking Azure Blob Storage Service'
    )
    
    parser.add_argument('-u', help="Specify the target URL to be used", required=True)
    parser.add_argument('-f', help="Filter by extension based on file name. Example: .pdf", required=False, default=None)
    args = parser.parse_args()

    url = args.u
    file_filter = args.f

    status(url, file_filter)

def status(url: str, file_filter: str) -> None:
    """Wrapper to check the status of the given URL."""

    response = request(url)
    if response:
        console.print(f"[[yellow]![/]] Enumerating blobs...\n", highlight=False)
        blob_handler(response.text, file_filter)
    else:
        pass


if __name__ == "__main__":
    initialize()