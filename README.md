# chi二乗検定と、fisherの正確検定
chi二乗検定と、fisherの正確検定について知見と使い方とか

## fisherの正確検定
考え方としてはノンパラメトリックなんだけど、一個一個のマトリックスの事象が”平等に起こり得る”という帰無仮説を立てると、次のように簡単に組み合わせ表現にすることができる  
<p align="center">
  <img width="150px" src="https://user-images.githubusercontent.com/4949982/36095701-a5f35a36-1036-11e8-8748-7c3b62a265c1.png">
</p>
例.４の目を仮定

<p align="center">
  <img width="350px" src="https://user-images.githubusercontent.com/4949982/36095653-6df7e584-1036-11e8-9530-a157984f0d01.png">
</p>
ある組み合わせが起こりうる頻度

これをpythonでコーディングするとこのようになる  
```python
import math

# web良かった、web悪かった, SI良かった, SI悪かった
a,b,c,d = [5,1,1,6]

ps = []
for a in range(0, 6 + 1):
  b = 6 - a
  c = 6 - a
  d = 7 - b
  ps.append( (a,b,c,d) )

  s = math.factorial( a+b ) * \
  math.factorial( a+c ) * \
  math.factorial( b+d ) * \
  math.factorial( c+d ) / ( math.factorial(a) * \
    math.factorial(b) * \
    math.factorial(c) * \
    math.factorial(d) * math.factorial(a+b+c+d) )
  print(a, s)
print(ps)
```
これを行うと山状の形を自由度に応じて得ることができて、山の面積の95%以外にあればそれは自然に起きたことではないという解釈が成り立ちそうである  
<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/36096096-2d6a7110-1038-11e8-92e5-9591c030aaa5.png">
</p>

これをもってして有効か無効かという視点では、なにかしらバイアスがあって平等に起こり得るという状態が否決されたと見させそうです  

## chi二乗検定
あるあるの検定で最も簡単にできます  

サイコロを具体例にとって説明すると、カイ二乗は、理論的な期待値（すべてのサイコロの目が平等にでる）から、観測された頻度の期待値（実際になんの目が何回でたかなど）の累積の誤差を求める作業と等価に見えます  

<div align="center">
  <img width="285" src="https://user-images.githubusercontent.com/4949982/36349015-5ad69156-14c0-11e8-8b4f-955dfe34de2a.png">
</div>

<div align="center">
  <img width="526" src="https://user-images.githubusercontent.com/4949982/36349049-ff03a0f2-14c0-11e8-9c87-b2b74eb06b20.png">
</div>

このような観測があった場合、例えばx^2は3.19となり、x^2分布をみると、下図のこの辺に位置しており全然中央に近い値なので、差はない（つまり自然なサイコロである）と言えそうです  

<div align="center">
  <img width="526" src="https://user-images.githubusercontent.com/4949982/36349105-ad98c09c-14c2-11e8-95eb-a8b704a8e8d4.png">
</div>
