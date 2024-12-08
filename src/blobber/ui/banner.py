from rich.console import Console
console = Console()

ASCII_ART = """
                             
 _____ _     _   _           
| __  | |___| |_| |_ ___ ___ 
| __ -| | . | . | . | -_|  _|
|_____|_|___|___|___|___|_|
        1.0.0 - @opps3c                      
"""

def get_banner() -> str:
    """ Returns Blobber's banner ascii art """
    console.print(f'[cyan]{ASCII_ART}[/]', highlight=False)