import requests
from PIL import Image
from io import BytesIO
import time
from datetime import datetime
import os

# Initialize an empty dictionary
cameraList = {}

# Open the text file for reading
with open('Camera_Links.txt', 'r', encoding='utf-8') as file:
    # Loop through each line in the file
    for line in file:
        # Split the line into two terms using the tab character as a delimiter
        terms = line.strip().split('\t')
        # Check if there are exactly two terms on the line
        if len(terms) == 2:
            # Assign the terms to the dictionary
            cameraList[terms[0]] = terms[1]

while True:
    for link, name in cameraList.items():

        # Directory to save images
        current_Date = datetime.now().strftime("%Y-%m-%d")
        save_directory = f"Pictures/{current_Date}/{name}"

        # Check if the directory exists
        if not os.path.exists(save_directory):
            # If it doesn't exist, create it
            os.makedirs(save_directory)

        try:
            # Send a GET request to the URL to fetch the image
            response = requests.get(link)

            # Check if the request was successful (HTTP status code 200)
            if response.status_code == 200:
                # Open the image using PIL
                image = Image.open(BytesIO(response.content))

                # Generate a filename with date and time information
                current_dateTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                current_time = datetime.now().strftime("T%H%M")
                filename = f"{current_time}_{name}.jpg"
                save_path = f"{save_directory}/{filename}"

                # Save the image to the specified directory
                image.save(save_path)

                #print(f"Image saved as {save_path}")

            else:
                pass


        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Wait for 5 minute before downloading the next image
    print(f'Saved {current_dateTime}')
    time.sleep(300)