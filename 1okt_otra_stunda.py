sk1=13
sk2=3

sask=sk1+sk2#saskaitam rez=16
print(sask)
print(sk1,"+",sk2,"=",sask)


at=sk1-sk2#atnemsana rez=10
print(at)

reiz=sk1*sk2#reizinasana rez=39
print(reiz)

dal=sk1/sk2#dalisana rez=4.3(3)
print(dal)

dal2=sk1//sk2#dalisana bez atlikuma rez=4
print(dal2)

atl=sk1%sk2#atlikuma noteiksana rez=1
print(atl)

pak=sk1**sk2#reizinasana pakape rez=2197
print(pak)

#salidzinasa
print(10>9)#true
print(2==4)#folse
a=2
a1="2"
print(a==a1)#folse, jo viens ir skaitlis, otrs ir teksts
print(1<0)#folse
#!= nav vienads

#>= lielaks vai vienasds
#bus sadi (>= dads variants nestradas)
#<= mazakas vai lielakas

# and &&
# japasakan x mainigasi va atrasties starp 5 un 10, ka pierakstas
#x>5 && x<10

#or || izvelk patieso mainīgo
#y>5 || y<10
#xor ^ izvelk nepatieso mainigo

if1=30
if2=2
if if1>if2:
    print("Skaitlis 30 lielāks neka skaitlis 2")
else:
    print("Skaitlis 30 nav lielāks parn 2")#tiek izmantots nosacijums if