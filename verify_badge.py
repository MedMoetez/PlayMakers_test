from PIL import Image, ImageDraw

center = (256, 256)
width, height = 512, 512
center_x = width // 2
center_y = height // 2
radius = center_x

def verify_badge(image_path):
    image = Image.open(image_path)
    if image.size != (512, 512):
        return False, "Image size must be 512x512"

    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y))[3] != 0:  # test if the pixel is opaque
                if (x - center_x) ** 2 + (y - center_y) ** 2 > radius ** 2:  # test if the pixel is outside of the circle
                    return False, "Non-transparent pixels must be within the circular boundary."

    # Check color for happy feeling
    colors = image.getcolors(width * height)
    happy_colors = [(0, 0, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0)]  # for me happy colors are Blue, Red, Yellow, Green
    happy_threshold = 0.5  # The idea is if less than 50% of the pixels in the image have happy colors, the function will return False.
    total_pixels = sum(count for count, _ in colors)
    happy_pixels = sum(count for count, color in colors if color in happy_colors)
    #if (happy_pixels / total_pixels) < happy_threshold:
        #return False, "Colors do not give a 'happy' feeling"

    return True, "Badge verified successfully"

# Example usage
result = verify_badge("example_badge.png")
print(result)




