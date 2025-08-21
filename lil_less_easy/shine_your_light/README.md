# Shine Your Light
## Forensics

There are two shadowy doorways, and a sign between the two. It’s too dark to read what it says… is there a way to see this image better? You try to shine your flashlight on it.. can you make the background white?

- Write a script to change black pixels to white pixels, and you’ll be able to see the flag

from PIL import Image

def change_black_to_white(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    data = img.getdata()
    new_data = []

    for pixel in data:
        if pixel[:3] == (0, 0, 0):
            new_data.append((255, 255, 255, pixel[3]))
        else:
            new_data.append(pixel)

    img.putdata(new_data)
    img.save(output_path)

change_black_to_white('input.png', 'output_image.png')


CTF{BOO!\_TURN_RIGHT}
