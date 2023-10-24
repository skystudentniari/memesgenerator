import requests
from PIL import Image, ImageDraw, ImageFont

requests.get('https://cataas.com/cat/says/hello%20world!')

print('Генератор мемов запущен!')
user_decide = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний:"))

if user_decide == 1:
    bottom_text = input('Введите нижний текст мема:')
    top_text = ''

elif user_decide == 2:
    top_text = input('Введите верхний текст мема:')
    bottom_text = input('Введите нижний текст мема:')

else:
    print("Введён неправильный режим. Перезапустите программу.")
    quit()

print(top_text, bottom_text)

memes = ["D:\\загрузки\\Кот в ресторане.png", "D:\\загрузки\\Кот в очках (1).png"]

print("Выберите картинку для мема.")
for i in range(len(memes)):
    print(i, memes[i])


image = Image.open(memes[int(input("Введите номер картинки."))])
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=70)

text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, (height - text[3] - 10)), bottom_text, font=font, fill="black")

image.save("new_meme.jpg")