#  my api key
api_key = "h7v4xvUDQMUcCBNKLZGhJ2OMvjzwedA0NafIP5Q6"

# to do web request through python, you have to do a web request

import requests 

# the url on which we have to do a web request 

url =" https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key="+ api_key 


# let's do a web request to this url

output = requests.get(url)

import json 
data = json.loads(output.text)
photos = data["latest_photos"]
img_src_list = []
for photo in photos:
  img_src_list.append(photo["img_src"])

print(img_src_list)
from PIL import Image
from io import BytesIO

for ur in img_src_list:

  # URL of the Image
  url = ur

  # Make a request to the URL and get the response object
  response = requests.get(url)

  # Open the image from the response object using PIL's Image module
  img = Image.open(BytesIO(response.content))

  # Show the image using PIL's Image module
  img.show()

