import requests

BASE_URL = 'http://127.0.0.1:8080'

image_path = r'C:\Users\Andrii\Downloads\bgr.jpg'

with open(image_path, 'rb') as img:
    files = {'image': img}
    response = requests.post(f'{BASE_URL}/upload', files=files)

if response.status_code == 201:
    print('Image uploaded successfully.')
    image_url = response.json().get('image_url')
    print('URL image:', image_url)
else:
    print('Error when uploading:', response.json())

filename = image_url.split('/')[-1]
response = requests.get(f'{BASE_URL}/image/{filename}', headers={'Content-Type': 'text'})

if response.status_code == 200:
    print('Image URL:', response.json().get('image_url'))
else:
    print('Error when getting image UTL:', response.json())

response = requests.delete(f'{BASE_URL}/delete/{filename}')

if response.status_code == 200:
    print('Image deleted:', response.json().get('message'))
else:
    print('Error when deleting', response.json())
