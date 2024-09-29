import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if not os.path.exists('mars_photos'):
        os.makedirs('mars_photos')

    for i, photo in enumerate(photos[:5]):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content

        filename = f'mars_photos/mars_photo{i + 1}.jpg'
        with open(filename, 'wb') as img_file:
            img_file.write(img_data)
            print(f"Saved: {filename}")

else:
    print(f"Couldn't get data. Status code: {response.status_code}")
