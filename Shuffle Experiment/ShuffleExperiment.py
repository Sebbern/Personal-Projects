cardlist = open("input.txt", "r").read().splitlines()

carda = cardlist[0]
carda = carda.split()
truecarda = carda
cardb = cardlist[1]
cardb = cardb.split()
cardcheck = []
shuffle = 0

while True:
    shuffle += 1

    for (i, u) in zip(carda, cardb):
        cardcheck.append(i)
        cardcheck.append(u)
    
    carda = cardcheck[:int(len(cardcheck)/2)]
    cardb = cardcheck[int(-len(cardcheck)/2):]
    cardcheck = []

    if carda == truecarda:
        break

print(shuffle)
