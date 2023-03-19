import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")
image_resp = openai.Image.create(prompt="2 sky lanterns stuck together", n=4, size="512x512")
print(image_resp)

# ref : https://pypi.org/project/openai/
