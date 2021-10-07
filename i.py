import os
files = os.listdir("./")
mdpath = "./README.md"
mdcreate = open(mdpatch,w)
for file in files:
    image=f'![](https://gitlab.com/gotopaz/Assets/images/size/320x320/{file}.png)'
    mdcreate.write(image+"\r\n")
