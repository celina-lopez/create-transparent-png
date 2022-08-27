from PIL import Image
import math

def near(pixel, n, tol):
      return abs(pixel - n) <= tol

def image_to_transparent(image_name, color, tolerance):
  img = Image.open(image_name)
  img = img.convert("RGBA")
  datas = img.getdata()
  newData = []
  tol = math.floor(tolerance * 255)

  for item in datas:
      if near(item[0], color[0], tol) and near(item[1], color[1], tol) and near(item[2], color[2], tol) :
          print(item)
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)

  img.putdata(newData)
  img.save("images/" + image_name, "PNG")



# Color to make transparent
color = (255, 188, 154)
# Color tolerance (how close to color)
tolerance = .25

image_to_transparent("image.png", color, tolerance)

