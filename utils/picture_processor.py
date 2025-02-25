import os

from PIL import Image, ImageDraw

from configuration.logger import get_logger


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = get_logger(__name__)


def stamp_ticket(ticket_number: str | int) -> str:
    image_path = os.path.join(BASE_DIR, 'staticfiles', 'images', 'ticket.png')
    image = Image.open(image_path)
    rgb_image = image.convert('RGB')

    draw = ImageDraw.Draw(rgb_image)
    text = str(ticket_number)
    # font = ImageFont.load_default_imagefont("arial.ttf", size=30)
    position = (1180, 623)
    color = (144, 12, 63)
    draw.text(position, text, fill=color, font_size=50)

    save_image_path = os.path.join(
        BASE_DIR, 'staticfiles', 'images', 'sent_tickets', f'ticket_{ticket_number}.jpg'
    )
    rgb_image.save(save_image_path)

    return save_image_path
