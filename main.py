from PIL import Image, ImageDraw, ImageFont

name=input('enter name : ')
photo=input('enter photo file name : ')

backimage = Image.new('RGB', (320, 640), (255, 255, 255))
im2 = Image.open(photo)
im1 = im2.copy()
back_im=im1.resize((200,200))

myFont = ImageFont.truetype('roboto.ttf', 40)
smfont = ImageFont.truetype('roboto.ttf', 20)

backimage.paste(back_im, (50, 80))
draw = ImageDraw.Draw(backimage)
draw.text((80, 10), "wanted", (255, 0, 0), font=myFont)
draw.text((50, 300), name, (255, 150, 0), font=myFont)

draw.text((10, 400), "he is an international Shoe thief", (255, 150, 0), font=smfont)
draw.text((10, 450), "Let me know if you see him ", (255, 150, 0), font=smfont)
draw.text((10, 500), "contact : 001 ", (255, 150, 0), font=smfont)

backimage.save('out.jpg')