
Mytable = [10,20,30,40]
score = 0

score = Mytable[2]           # score devient la 3eme valeur (30)
Mytable[2] = Mytable[1]      # La 3eme valeur devient la 2eme donc 10,20,20,40
Mytable[1] = score           # La 2eme valeur devient score (30)

print (Mytable)


# 2 
Mytable = [3,2,9,0]
Plusgrand = Mytable[0]
score = 0
petit = 0 

for i in range(len(Mytable)):
    if Plusgrand < Mytable[i]:
        score = Plusgrand          
        Plusgrand= Mytable[i]     
        Mytable[i] = score
        Mytable.pop(i)
        Mytable.append(Plusgrand)

print (Mytable)

# 3

Mytable = [19,29,399,10]
Grand = 0
score = 0

for j in range(len(Mytable)):
    Position = j
    Grand = Mytable[j]
    for i in range(len(Mytable)):
        if Grand < Mytable[i]:
            score = Grand           
            Grand = Mytable[i]      
            Mytable[i] = score
            Mytable.pop(i)        
            Mytable.append(Grand)
print (Mytable)



# 4 car a chaque fois qu'un chiffre est considéré comme plus grand l'algorithme l'envoi a la fin et revient au début en plus de dévoir checker tout les tableau


X = "X"
O = "O"

