# %%
import requests
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO

# %%
load_dotenv()

API_KEY = os.environ["CLIPDROP_API_KEY"]

sample_no = 1
image_path = f"samples/sample_{sample_no}.jpeg"
output_path = f"output/{os.path.basename(image_path)}"

# %%
with open(image_path, 'rb') as image_file:
    res = requests.post('https://clipdrop-api.co/replace-background/v1',
        files= {'image_file': (image_path, image_file, 'image/jpeg')},
        data = {'prompt': 'shiny day, in beach and blue water in the background'},
        headers = {'x-api-key': API_KEY}
    )
    print(f"Status: {res.status_code} | Remaining Credits: {res.headers.get('x-remaining-credits')}")

# %%
if res.ok:
    image_bytes = res.content
    image_stream = BytesIO(image_bytes)
    img = Image.open(image_stream)
    img.save(output_path)
else:
    res.raise_for_status

# %%
