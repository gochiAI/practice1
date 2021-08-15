S = open('/workspace/practice1/out/o.txt',mode='a')


for Story in range(1,44):
  Y=f'![](https://gitlab.com/gochiusa/DB/Official/Books/main-story/volume1/-/raw/main/Story/{Story}.jpeg)'
  S.write(Y+"\r\n")
