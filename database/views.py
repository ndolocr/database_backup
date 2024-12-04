from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_table_structure(request, table_name):
    try:
        # Use Django's database introspection to get table structure
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {rules}")
        columns = cursor.fetchall()

        # Format the response
        table_structure = []
        for column in columns:
            table_structure.append({
                "Field": column[0],  # Column name
                "Type": column[1],   # Data type
                "Null": column[2],   # Whether NULL is allowed
                "Key": column[3],    # Key type (e.g., PRIMARY, UNIQUE)
                "Default": column[4], # Default value
                "Extra": column[5],   # Extra information (e.g., auto_increment)
            })

            for row in table_structure:
                print(f"------------------------------------------------------------")
                print(f"{row}")
                print(f"------------------------------------------------------------")

        return JsonResponse({"table_structure": table_structure})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)