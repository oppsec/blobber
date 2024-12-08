"""
This module checks the status from the Azure Container passed
"""

from rich.console import Console
console = Console()
from requests import get
from urllib3 import disable_warnings
disable_warnings()

from blobber.modules.errors import error_handler

def request(url: str) -> tuple:
    """
    Perform a GET request to the given URL, handle errors, and retry if necessary.
    """

    url = f"{url}/?restype=container&comp=list"

    try:
        response = get(url, verify=False, timeout=10)
        if response.ok:
            console.print(f"[[green]+[/]] Connected successfully to [green]{url}[/]")
            return response

        # Handle errors
        error_handler_response = error_handler(url, response)
        if error_handler_response:
            return error_handler_response

        console.print(f"[[yellow]![/]] Request to [green]{url}[/] failed with status {response.status_code}", highlight=False)
        return None

    except Exception as error:
        console.print(f"[[red]![/]] Error trying to connect to [green]{url}[/]: {error}")
        return None
