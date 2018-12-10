import image  # imports the image module

img = image.Image("colorSwap.jpg")  # makes an image object
new_img = image.EmptyImage(img.getWidth(), img.getHeight()) # creates new image
win = image.ImageWin(img.getWidth(), img.getHeight()) # creates window

# To start with, each pixel already has RGB values, and positions in the grid right? 

# Then if we want to invert the colors we say 

for col in range(img.getWidth()):		# lists columns
    for row in range(img.getHeight()):	# lists rows
        p = img.getPixel(col, row)		# selects each pixel by position on grid
        new_red = 0
        green = p.getGreen()
        blue = p.getBlue()

        new_pixel = image.Pixel(new_red, green, blue)

        new_img.setPixel(col, row, new_pixel)

new_img.draw(win) # renders image
win.exitonclick()
