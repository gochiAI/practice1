S = open('/workspace/practice1/out/i.txt',mode='a')


for Story in range(1,52):
  Story = "{0:02d}".format(Story)
  Y=f'![](https://gitlab.com/gochiusa/DB/Official/Books/main-story/volume1/-/raw/main/Story/{Story}.png)'
  S.write(Y+"\r\n")
