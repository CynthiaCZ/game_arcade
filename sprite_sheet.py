from PIL import Image

# divide the sprite sheet into 4*4 tile
im = Image.open("sprite_sheet2/sprite2.png")
imgwidth = im.size[0]/4
imgheight = im.size[1]/4
# name each frame with direction + frame number
keyList = ["D1", "D2", "D3", "D4", "L1", "L2", "L3", "L4", "R1", "R2", "R3", "R4", "U1", "U2", "U3", "U4"]
# create a dictionary
d = {}
k = 0
for j in range(4):
    for i in range(4):
        im_crop = im.crop((i*imgwidth,j*imgheight,(i+1)*imgwidth,(j+1)*imgheight))
        k += 1
        key = keyList[k-1]
        d[key] = im_crop
        im_crop.save('sprite_sheet2/' + key + '.png')

# convert the dictionary into variables
for key, val in d.items():
        exec(key + '=val')
