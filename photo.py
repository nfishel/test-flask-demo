from PIL import Image, ImageEnhance, ImageFont, ImageDraw, ImageFilter
import os

path = "./imgs"
pathOut = "./editedImgs"

for filename in os.listdir(path):
  img = Image.open(f"{path}/{filename}")

  edit = img.filter(ImageFilter.SHARPEN).convert('L')
  factor = 1.5
  enhancer = ImageEnhance.Contrast(edit)
  edit = enhancer.enhance(factor)
  draw = ImageDraw.Draw(edit)
  font = ImageFont.truetype("lgr.ttf", size=438)
  draw.text((10,25), "CHICAGO",fill="yellow", font=font)
  clean_name = os.path.splitext(filename)[0]
  edit.save(f"./{pathOut}/{clean_name}_edited.jpg")