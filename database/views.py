import os
from django.conf import settings
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from datetime import datetime

from database.models import Rule
from database.models import Request

# Create your views here.
def get_table_structure(request, table_name):
    try:
        # Use Django's database introspection to get table structure
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
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


def archive_table_structure(request, table_name):
    try:

        # Use Django's database introspection to get table structure
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()

        # File path to save the table structure
        file_path = os.path.join(settings.BASE_DIR, f"{table_name}_structure.txt")

        # Write table structure to the file
        with open(file_path, "w") as file:
            file.write(f"Table: {table_name}\n")
            file.write("=" * 120 + "\n")
            file.write(f"{'Field':<20}{'Type':<20}{'Null':<10}{'Key':<10}{'Default':<25}{'Extra':<25}\n")
            file.write("=" * 120 + "\n")
            for column in columns:
                file.write(
                    f"{column[0]:<20}{column[1]:<20}{column[2]:<10}{column[3]:<10}{str(column[4]):<25}{column[5]:<25}\n"
                )

        current_time = datetime.now()
        # Open the file and prepare it for download
        with open(file_path, "rb") as file:
            response = HttpResponse(file.read(), content_type="text/plain")
            response["Content-Disposition"] = f"attachment; filename={table_name}_structure_{current_time}.txt"
            return response

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def write_table_data_to_file(request, table_name):
    try:
        # Use raw SQL to fetch all data from the specified table
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        # File path to save the table data
        file_path = os.path.join(settings.BASE_DIR, f"{table_name}_data.txt")

        # Write table data to the file
        with open(file_path, "w") as file:
            # Write header
            file.write(f"Data from table: {table_name}\n")
            file.write("=" * 100 + "\n")
            file.write("\t".join(column_names) + "\n")
            file.write("=" * 100 + "\n")
            
            # Write each row
            for row in rows:
                file.write("\t".join(str(value) if value is not None else "NULL" for value in row) + "\n")

        current_time = datetime.now()
        # Open the file and prepare it for download
        with open(file_path, "rb") as file:
            response = HttpResponse(file.read(), content_type="text/plain")
            response["Content-Disposition"] = f"attachment; filename={table_name}_data_{current_time}.txt"
            return response

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)