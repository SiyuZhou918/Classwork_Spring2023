from tkinter import filedialog
import base64
import requests

# Select image to upload
def select_image():
    filename = filedialog.askopenfilename(initialdir="/Users/emtzhou/Desktop/image")
    return filename


# Convert image file to base64 string
def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


# Upload base64 string to server

# Download watermarked image
def save_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    with open("/Users/emtzhou/Desktop/image/new-img.jpg", "wb") as out_file:
        out_file.write(image_bytes)
    return

def main():
    filename = select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base64_string(filename)
    print(b64_image)

    server = "http://vcm-21170.vm.duke.edu"

    image = {"image": b64_image, "net_id": "sz274", "id_no": 1}
    r = requests.post(server + "/add_image", json=image)
    print(r.status_code)
    print(r.text)

    r = requests.get(server + "/get_image/sz274/1")
    print(r.status_code)
    print(r.text)
    print(type(r))

    save_b64_image(r.text)

if __name__ == '__main__':
    main()