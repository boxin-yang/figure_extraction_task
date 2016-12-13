from PIL import Image
im = Image.open("sample.png")

test = im.crop((80,150,100,170))
print(list(test.getdata()))
test.show()
# test.save("2.png", format='png')