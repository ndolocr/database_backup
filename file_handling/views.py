import os
from pathlib import Path

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def desktop_folder_contents(request, folder_name):
    # Get the user's home directory
    home_dir = Path.home()    
    folder_path = home_dir / f"{folder_name}"

    # Verify if the folder exists
    if folder_path.exists() and folder_path.is_dir():
        print(f"Folder Path --> {str(folder_path)}")
        # Get folder contents
        folder_contents = os.listdir(folder_path)
        
        items = {}
        item_num = 0
        for item_name in folder_contents:
            items[item_num] = item_name
            item_num+=1

        return JsonResponse({"object": items})
    else:
        return JsonResponse({"object": "Folder Not Found!"})  # Handle case where the folder does not exist
