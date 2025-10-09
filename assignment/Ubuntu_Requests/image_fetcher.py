import requests
import os
from urllib.parse import urlparse
from PIL import Image

def main():
    print("Welcome to the Ubuntu inage fetcher\n")
    print("A tool for mindfully collecting images from the web\n")

    #Get URL from user
    url= input("Please enter the image url:")

    try:
        #Create directory
        os.makedirs("Fetched_Images", exist_ok= True)

        #Fetch the image
        response = requests.get(url, timeout= 10)
        response.raise_for_status() #Error excetion for bad status_codes

        #Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename= os.path.basename(parsed_url.path)

        if not filename:
            filename = "downloaded_image.jpg"

        #Save the image
        filepath = os.path.join("Fetched_Images", filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"SUCCESSFULLY FETCHED: {filename}")
        print(f"Image saved to {filepath}")

    #Dealing with errors
    except requests.exceptions.RequestException as e:
        print(f"CONNECTION ERROR: {e}")
    except Exception as e:
        print(f"AN ERROR OCCURED: {e}")

if __name__ == "__main__":
    main()
    