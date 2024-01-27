import requests
import base64
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    
    image_url = "https://res.cloudinary.com/dgcwnjoh4/image/upload/v1706369585/mixing-potions_dxbqti.png"
    response = requests.get(image_url)
    
    if response.status_code == 200:
        image_data = base64.b64encode(response.content).decode('utf-8')
        return Response({
            "message": "Welcome to your better life! This is Mixing potions API!",
            "image_data": image_data
        })
    else:
        return Response({
            "message": "Failed to fetch the image from the URL."
        }, status=response.status_code)