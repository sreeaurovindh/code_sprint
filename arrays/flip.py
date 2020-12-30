cards = []
for i in range(52):
    cards.append(0)
for i in range(52):
    print(cards)
    for j in range(52):
        if (j+1)%(i+1) == 0:
            if cards[j] == 0:
                cards[j] = 1
            else:
                cards[j]= 0
count = 0
for i in range(len(cards)):
    count = count +cards[i] 

print(count)