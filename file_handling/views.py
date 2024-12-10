import os
from pathlib import Path

from django.shortcuts import render

# Create your views here.

def desktop_folder_contents(request, folder_name):
    # Get the user's home directory
    home_dir = Path.home()    
    folder_path = home_dir / f"{folder_name}"

    # Verify if the folder exists
    if folder_path.exists() and folder_path.is_dir():
        print(f"Folder Path --> {str(folder_path)}")
        return str(folder_path)
    else:
        print(f"No Desktop Folder found")
        return None  # Handle case where the folder does not exist
