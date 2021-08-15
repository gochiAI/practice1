# practice1
python for,rangeを使った簡単なスクリプト  
.md用の連番画像を表示させたい時にいちいち書くのは、だるかった。  

# usage
需要ないと思うよ。

S = open('出力ファイル名',mode='a')


for Story in range(1,44):  
  Story = "{0:02d}".format(Story)  
  Y=f'![](URLとか{Story}.jpeg)'  
  S.write(Y+"\r\n")  
