import random

santas = []
chosen = {}

with open("secret_answers.tsv", encoding = "utf-8") as f:
    people = f.read().split('\n')[1:]

#вытаскиваю имена для списка сант
for p in people:
    p = p.split('\t')[1:]
    santas.append(p[0])
#print(santas)

#прохожусь по спискам сант, выбираю для санты человека, потом убираю санту и человека из списка
for s in santas[::-1]:
    ran = random.choice(people)
    r = ran.split('\t')[1:]
    while r[0] == s:
        ran = random.choice(people)
        r = ran.split('\t')[1:]
    #print(s, r)
    info = 'Твоего подопечного зовут {}. В школе лингвистики твой подопечный - {}. Связаться с ним можно так: {}. О себе твой подопечный рассказывает это: {}'.format(r[0], r[1], r[2], r[3])
    santas.remove(s)
    people.remove(ran)
    chosen[s] = info

with open('santa_data.txt', 'a', encoding = 'utf-8') as f:
    for c in chosen:
        line = 'Дорогой участник Тайного Санты, {}! {}\n'.format(c, chosen[c])
        f.write(line)



