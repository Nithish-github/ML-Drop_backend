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

# Create your views here.

def index(reponse):
    return HttpResponse("IM Back")

def index_2(reponse):
    return HttpResponse("IM Back fucker")


class ExampleView(APIView):

    def get(self, request):

        data = {"message": "Hello from backend!"}

        # Path to your image
        image_path = "/home/nkumar/griffyn/ML-Drop/mypage/assests/gettyimages-490703338.jpg"
        
        # Open the image and encode it to Base64
        with open(image_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

        data = {
            "message": "Hello from backend!",
            "image_data": encoded_image
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



        '''
        if the filter is for code generation 
        '''
        


        

        # Response data
        response_data = {
            "message": "Data received and processed",
            "processed_image_base64": processed_image_base64
        }

        # Return a response with the processed image
        return Response(response_data, status=status.HTTP_201_CREATED)