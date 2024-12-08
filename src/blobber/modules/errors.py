"""
This module handle the common errors when interacting with Azure Blobs
"""

from rich.console import Console
console = Console()
from requests import get
from urllib3 import disable_warnings
disable_warnings()

errors_list = {
    "InvalidQueryParameterValue": "Value for one of the query parameters specified in the request URI is invalid.",
    "FeatureVersionMismatch": "Trying to add 'x-ms-version: 2020-04-08' header on the request.",
    "ResourceNotFound": "Invalid container or blob file specified in the URL.",
    "AccountIsDisabled": "The specified account is disabled."
}

def error_handler(url: str, response) -> tuple:
    """
    Handles errors in Azure Blob responses and retries if specific errors occur.
    """
    
    try:
        if isinstance(response, str):
            response_text = response
        else:
            response_text = response.text if hasattr(response, 'text') else ""

        for key, value in errors_list.items():
            if key in response_text:
                #console.print(f"[[yellow]![/yellow]] [red]{key}[/]: {value}")
                
                if key == "FeatureVersionMismatch":
                    headers = {"x-ms-version": "2020-04-08"}
                    retry_response = get(url, verify=False, timeout=10, headers=headers)
                    
                    if retry_response.ok:
                        console.print(f"[[green]+[/]] Retried with x-ms-version header and succeeded!")
                        return retry_response 
                    else:
                        console.print(f"[[red]![/]] Retried but failed with status {retry_response.status_code}")
                        return retry_response
                
                if key == "InvalidQueryParameterValue":
                    console.print(f"[[red]![/]] {value}")
                    return False
                
                if key == "ResourceNotFound":
                    console.print(f"[[red]![/]] Invalid container or blob file specified in the URL.")
                    return False

                if key == "AccountIsDisabled":
                    console.print(f"[[red]![/]] {value}")
                    return False

        if not isinstance(response, str) and not response.ok:
            console.print(f"[[yellow]![/]] Bad request to [green]{url}[/]")
        return None

    except Exception as error:
        console.print(f"[[red]![/]] Unexpected error in error_handler: {error}")
        return None