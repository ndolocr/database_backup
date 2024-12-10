import os
from pathlib import Path

from django.shortcuts import render

# Create your views here.

def desktop_folder_contents(request):
    # Get the user's home directory
    home_dir = Path.home()
    # Append the "Desktop" folder to the home directory
    desktop_folder = home_dir / "Desktop"

    # Verify if the Desktop folder exists
    if desktop_folder.exists() and desktop_folder.is_dir():
        print(f"Desktop Folder --> {desktop_folder}")
        return str(desktop_folder)
    else:
        print(f"No Desktop Folder found")
        return None  # Handle case where the folder does not exist
