#Skilaverkefni 2
#höfundur: Jón Benediktsson

inp=""
while inp !="exit":
    print("""Skilaverkefni 2 :)
1. summa annarsveldi
2. runa talna
3.þversumma
4.samnefnari
eða exit tila að hætta.""")
    inp=input("skrifaðu inn númer dæmis: ")
    print()

    #liður 1
    if inp =="1":
        def summa(x):
            if x>1:return x**2+summa(x-1)
            else:return 1
        inpl1=int(input("settu inn tölu: "))
        print("utkoman er: "+str(summa(inpl1)))

    #liður 2
    elif inp == "2":
        def runa(x):
            if x>1:
                return (runa(x-1)+" "+str((x+1)*x//2))
            else:
                return ("1")
        inpl2=int(input("settu inn tölu: "))
        print("utkoman er: " +runa(inpl2))

    #liður 3
    elif inp=="3":
        def thversumma(x):
            if len(x)>1:
                return int(x[0])+ thversumma(x[1:])
            else:
                return int(x)
        inpl3 = input("settu inn tölu: ")
        print("utkoman er: " + str(thversumma(inpl3)))

    #liður 4
    elif inp=="4":
        def samnefnari(a, b):
            if min(a, b) > 1:
                for x in range(2,min(a, b) + 1):
                    if (a % x) + (b % x) == 0:
                        break
                if x == min(a,b)+1:
                    return 1
                else:
                    return x * samnefnari(a // x, b // x)
            else:
                return 1
        inpl4 = input("settu inn tölur aðgreindar með einu bili: ").split(" ")
        inpl4=list(map(int,inpl4))
        print("utkoman er: " + str(samnefnari(inpl4[0],inpl4[1])))


    elif inp == "exit":break

    else:print(inp+" er ekki eithvað sem er til")
    print()