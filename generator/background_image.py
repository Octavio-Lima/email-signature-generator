from PIL import Image


def generate_background_image(filename: str):
    hexa_mask = Image.open("style/images/hexa_mask.png").convert("L")
    person = Image.open(f"style/people/{filename}.png").resize(hexa_mask.size)
    blank = Image.new("RGB", hexa_mask.size, (128, 128, 128))

    blank.putalpha(0)

    result = Image.composite(person, blank, hexa_mask)

    background = Image.open("style/images/diedro_bg.png")
    background.paste(result, (200, 745), hexa_mask)

    background.save(f"style/background/{filename}.png", "png")
