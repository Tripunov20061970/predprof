File = open('space.txt',encoding = "UTF-8")
St = []
l=0
for i in File:
    St.append(i.split('*'))
    l+=1
spaceship=[]
for i in range(1,l):
    spaceship.append(St[i][0].split('-'))
for i in range(0,len(spaceship)-1):
    for j in range(len(spaceship)-2,i-1,-1):
        if int(spaceship[j][1])>int(spaceship[j+1][1]):
            spaceship[j],spaceship[j+1]=spaceship[j+1],spaceship[j]
for i in range(10):
    print(spaceship[i][0])
File.close()