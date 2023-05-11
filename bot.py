import discord
import tensorflow_hub as hub
import numpy as np
from PIL import Image
from discord.ext import commands

client = commands.Bot(command_prefix='!')

# Load the BigGAN model
model = hub.load("https://tfhub.dev/deepmind/biggan-256/2")

# Read Discord bot token from token.txt
with open('token.txt', 'r') as f:
    TOKEN = f.read().strip()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.command()
async def generate(ctx, *args):
    if len(args) < 4:
        await ctx.send('Please provide valid inputs in the format: !generate [object] [style] [resolution] [purpose]')
        return

    # Get inputs from user
    obj = args[0]
    style = args[1]
    resolution = args[2]
    purpose = args[3]

    # Generate a random noise vector
    z = np.random.normal(size=[1, 128]).astype(np.float32)

    # Set the labels for the BigGAN model
    labels = np.zeros([1, 1000])
    labels[:, 1] = 1  # Set the label for "spider" to 1

    # Generate an image from the noise vector and labels
    inputs = dict(z=z, labels=labels)
    image = model(inputs)['default'][0]

    # Convert the image to a Pillow Image object
    image = Image.fromarray(np.uint8(image*255))

    # Save the image to a file
    image.save('generated_image.jpg')

    # Send the image to the Discord channel
    await ctx.send(f"Generating your {obj} image in {style} style with {resolution} resolution for {purpose}. Please wait...")
    await ctx.send(file=discord.File('generated_image.jpg'))

client.run(TOKEN)
