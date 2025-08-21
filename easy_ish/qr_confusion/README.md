# QR Confusion
## Misc

What does this data even mean?

- CSV is coordinates of black pixels of a QR code. write a script to put this all together:
```
from PIL import Image
import csv

def decode_coordinate(coord):
    x, y = map(int, coord.split(','))
    return (x, y)

def decode_coordinates(encoded_coordinates):
    return [decode_coordinate(coord) for coord in encoded_coordinates]

# Read the black pixel coordinates from the CSV file
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row
    for row in reader:
        encoded_coordinates = [col for col in row]

decoded_coordinates = decode_coordinates(encoded_coordinates)

# Recreate the QR code image
image = Image.new("1", (500, 500), color=255)
for x, y in decoded_coordinates:
    print(x, y)
    image.putpixel((x, y), 0)

image.save("result.png")
```


CTF{qr8_j0b!}

