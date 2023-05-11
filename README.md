# Discord AI Image Generator Bot

This is a Discord bot that generates customized images using the BigGAN model from TensorFlow Hub. Users can input the object, style, resolution, and purpose of the image they want to generate, and the bot will generate and send the image to the Discord channel.

## Prerequisites

To use this bot, you need to have the following installed:

- Python 3.6 or higher
- TensorFlow 2.x
- TensorFlow Hub
- Pillow
- discord.py

## Usage

1. Clone this repository to your local machine using `git clone https://github.com/SathiraSriSathsara/image-generator-discord-bot.git`
2. Navigate to the directory using `cd discord-ai-image-generator-bot`
3. Create a `token.txt` file in the same directory and paste your Discord bot token in the file.
4. Run the bot using the command `python bot.py` in your terminal.
5. In your Discord server, use the command `!generate [object] [style] [resolution] [purpose]` to generate a customized image.

 `[object]` is the object you want to generate, e.g., spider-man, cat, dog, etc.<br>
 `[style]` is the style you want to apply to the object, e.g., cyberpunk, cartoon, watercolor, etc.<br>
 `[resolution]` is the resolution of the image you want to generate, e.g., 4k, 1080p, 720p, etc.<br>
 `[purpose]` is the purpose of the image you want to generate, e.g., wallpaper, avatar, meme, etc.<br>

The bot will generate the image and send it to the Discord channel.

Example: `!generate spider-man cyberpunk 4k wallpaper`

## Contributing

If you want to contribute to this project, feel free to open a pull request or submit an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
