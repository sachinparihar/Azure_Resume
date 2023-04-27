import os
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Get the path to the requested file
    file_name = req.route_params.get('file_name', 'index.html')
    file_path = os.path.join(os.getcwd(),'Azure-Blog-Website','Content', file_name)


    try:
        # Open the requested file and read its contents
        with open(file_path, 'r') as f:
            file_contents = f.read()
        
        # Return the contents of the file as the HTTP response body
        return func.HttpResponse(file_contents, mimetype='text/html')
    
    except FileNotFoundError:
        # If the requested file does not exist, return a 404 error
        return func.HttpResponse("File not found", status_code=404)
