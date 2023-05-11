import tensorflow_hub as hub
import numpy as np
from PIL import Image

# Load the BigGAN model
model = hub.load("https://tfhub.dev/deepmind/biggan-256/2")

# Generate a random noise vector
z = np.random.normal(size=[1, 128]).astype(np.float32)

# Generate an image from the noise vector
image = model(z)['default'][0]

# Convert the image to a Pillow Image object
image = Image.fromarray(np.uint8(image*255))

# Save the image to a file
image.save('generated_image.jpg')
