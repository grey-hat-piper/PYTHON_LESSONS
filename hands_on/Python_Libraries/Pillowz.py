from PIL import Image  # Ask for the artisan's specific skill
from PIL import ImageFilter  # Ask for the artisan's specific skill

# Open an image file
image = Image.open('Vibe432.jpg')

# The artisan works their magic: rotate and convert to grayscale
rotated_image = image.rotate(45)
bw_image = rotated_image.convert('L')

# Save the new creation
bw_image.save('my_artistic_image.jpg')

#Resize the image
resized_image = bw_image.resize((200, 200))
resized_image.save('my_resized_image.jpg')
resized_image.show()  # Display the final masterpiece

# Blur the image using a filter

blurred_image = image.filter(ImageFilter.GaussianBlur(5))       
blurred_image.save('my_blurred_image.jpg')
blurred_image.show()  # Display the blurred masterpiece

#flip the image
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)  
flipped_image.save('my_flipped_image.jpg')
flipped_image.show()  # Display the flipped masterpiece 