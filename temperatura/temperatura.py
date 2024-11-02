n = 4
dani = 0
temp1,temp2,temp3,temp4 = map(int, input("Unesite temperaturu za dan : ").split(", "))
prosek = (temp1 + temp2 + temp3 + temp4)/n
if(temp1 < prosek):
    dani += 1
if(temp2 < prosek):
    dani += 1
if(temp3 < prosek):
    dani += 1
if(temp4 < prosek):
    dani += 1
print("prosek je ", prosek)
print(dani, "dana je temperatura bila manja nego prosek svih temperatura")