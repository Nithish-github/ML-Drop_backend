from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import base64
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .image_processing import apply_filter
from .code_generation  import generate_code

# Create your views here.

class OpencvView(APIView):

    def get(self, request):

        data = {
            "message": "Hello from backend!",
            "image_data": ""
        }
        return Response(data, status=status.HTTP_200_OK)

    

    def post(self, request):
        # Access the data sent in the request
        received_data = request.data

        # Get base64-encoded image and filter type
        base64_image = received_data.get('image_base64')
        filter_type = received_data.get('filter_type')

        if not base64_image or not filter_type:
            return Response({"error": "Image and filter type are required."}, status=status.HTTP_400_BAD_REQUEST)


        try:
            # Use the external module to apply the filter
            processed_image_base64 = apply_filter(base64_image, filter_type)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
      

        # Response data
        response_data = {
            "message": "Data received and processed",
            "processed_image_base64": processed_image_base64
        }

        # Return a response with the processed image
        return Response(response_data, status=status.HTTP_201_CREATED)


class CodeGenerationView(APIView):

    def get(self, request):
        """
        GET request that returns a sample image encoded in Base64 and a message.
        """
        # Prepare the response
        data = {
            "code_ops": ""
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST request to apply a filter with intensity to an image.
        Expects three parameters: image_base64, filter_type, and intensity.
        """
        # Access the data sent in the request
        received_data = request.data

        # Extract parameters
        code_sequence = received_data.get('code_ops')

        # Validate the parameters
        if not code_sequence:
            return Response(
                {"error": "Error in sending the code sequence"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            #Call code generation script
            #tasks = ['input', 'threshold', 'findcontours', 'display']
            generated_code = generate_code(code_sequence)
            print(code_sequence)


        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare the response data
        response_data = {
            "code_ops": generated_code
        }

        return Response(response_data, status=status.HTTP_201_CREATED)