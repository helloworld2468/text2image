import requests

def generate_image():
    while True:
        # Get the text to generate an image from the user
        text = input(">> ")

        # Make the POST request to the Deepai API
        r = requests.post(
            "https://api.deepai.org/api/text2img",
            data={"text": text},
            headers={"api-key": "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"},
        )

        # Print the response from the API
        print(r.json())

if __name__ == "__main__":
    generate_image()