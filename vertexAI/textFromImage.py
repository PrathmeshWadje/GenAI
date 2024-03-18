import os
import google.generativeai as genai
import PIL.Image

GOOGLE_API_KEY='AIzaSyDnPTmBOzc75EMYuWpmWjS90txNEK6SkuE'

genai.configure(api_key=GOOGLE_API_KEY)

def get_image_path():
  while True:
    image_path = input("Enter the path to the JPG image: ")
    if not os.path.exists(image_path):
      print("Invalid path. Please enter the correct path to the image in JPG format")
    else:
      return image_path
    
image_path = get_image_path()
# print(f"You entered: {image_path}")

img = PIL.Image.open(image_path)

model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')

response = model.generate_content(img)

response = model.generate_content([input("Enter a prompt: "), img])
response.resolve()

print(response.text)