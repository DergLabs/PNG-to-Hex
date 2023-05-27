
from PIL import Image


def img_to_hex(input_file, output_file):
    img = Image.open(input_file)
    pixels = list(img.getdata())

    with open(output_file, 'w') as f_out:
        for i in range(0, len(pixels), 8):
            hex_values = [f'{pixel[0]:02x}{pixel[1]:02x}{pixel[2]:02x}' for pixel in pixels[i:i+8]]
            f_out.write(' '.join(hex_values) + '\n')

if __name__ == "__main__":
    input_file = '/users/<USER>/desktop/<IMAGE>.png'
    output_file = '/users/<USER>/desktop/<IMAGE_OUT>.hex'
    img_to_hex(input_file, output_file)
