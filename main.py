from random import randint

size = 10
amountField = size*size
amountBombs = round(amountField/10)
field =[]

for i in range(amountField):
    field.append(0)

x=0
while x<amountBombs:
    randomField = field[randint(0,amountField-1)]
    #print("e", x)
    if randomField == "b":
        #print("w", x)
        pass
    else:
        field[randint(0,amountField-1)] = "b"
        x = x+1
        #print("b")
    

for i in range(amountField):
    if field[i]=="b":
        if not i%size==0:
            if field[i-1]!="b":
                field[i-1]+=1
        if not i%size==size-1:
            if field[i+1]!="b":
                field[i+1]+=1
        if not i<size:
            if field[i-size]!="b":
                field[i-size]+=1
        if not i<size and not i%size==size-1:
            if field[i-size+1]!="b":
                field[i-size+1]+=1
        if not i<size and not i%size==0:
            if field[i-size-1]!="b":
                field[i-size-1]+=1
        if not i>=size*(size-1):
            if field[i+size]!="b":
                field[i+size]+=1
        if not i>=size*(size-1) and not i%size==size-1:
            if field[i+size+1]!="b":
                field[i+size+1]+=1
        if not i>=size*(size-1) and not i%size==0:
            if field[i+size-1]!="b":
                field[i+size-1]+=1
print(field)

discordText = ""
for i in range(amountField):
    if i%size==0 and i!=0:
        discordText += "\n"
    discordText += "||"
    if field[i] == 0:
        discordText += ":nix:"
    elif field[i] == 1:
        discordText += ":one:"
    elif field[i] == 2:
        discordText += ":two:"
    elif field[i] == 3:
        discordText += ":three:"
    elif field[i] == 4:
        discordText += ":four:"
    elif field[i] == 5:
        discordText += ":five:"
    elif field[i] == 6:
        discordText += ":six:"
    elif field[i] == 7:
        discordText += ":seven:"
    elif field[i] == 8:
        discordText += ":eight:"
    elif field[i] == "b":
        discordText += ":bomb:"
    discordText += "||"


print(discordText)