import re

with open('santa_data.txt', encoding='utf-8') as f:
    text = f.read()
    textfx = re.sub('Связаться с ним можно так:(.*)?О', 'O' , text)
    textfxx = re.sub('себе твой подопечный рассказывает это: ','своих пожеланиях и интересах рассказывает так: ', textfx)
    print(textfxx)
with open ('fixed_santa.txt', 'w', encoding= 'utf-8') as f:
    f.write(textfxx)