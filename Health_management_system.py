#______________HEALTH___MANAGEMENT__SYSTE____________
"""This system help to set the diet and exercise plan means you can add your diet and
exercises here and you can check your plans also.If you want to set plan then go with log
option and if you want to check plan then go with retrive option"""
try:
 while(True):
  x=int(input("\nYou wanna log or retrive data?\n1.Log\n2.Retrive\nSelect number:"))
  if x==1:
    print("\nOK which thing you wanna log\n1.Food\n2.Exercise")
    y=int(input("Select number:"))
  else:
    print("\nOK which data you wanna retrive\n1.Food\n2.Exercise")
    z = int(input("Select number:"))

  def getdate():
    import datetime
    return datetime.datetime.now()
  def writefile(y):
    if y==1:
        print("\nOk whose food you wanna log\n1.Prabhat\n2.Rohan\n3.Hammad")
        a = int(input("Select number:"))
        if a == 1:
            k = input("write your data:")
            with open("Prabhatfood.txt", "a") as f:
                K = "[" + str(getdate()) + "]"
                f.write(K+k+"\n")

                print("")
                print(K, ":DATA UPDATED SUCCESSFULLY")
        elif a == 2:
            l = input("write your data:")+"\n"
            with open("rohanfood.txt", "a") as f:
                f.write(l)
                L = "[" + str(getdate()) + "]"
                print("")
                print(L, ":DATA UPDATED SUCCESSFULLY")
        else:
            m = input("write your data:")+"\n"
            with open("hammadfood.txt", "a") as f:
                f.write(m+"\n")
                M = "[" + str(getdate()) + "]"
                print("")
                print(M, ":DATA UPDATED SUCCESSFULLY")
    else:
        print("\nOk whose exercise you wanna log\n1.Prabhat\n2.Rohan\n3.Hammad")
        b = int(input("Select number:"))
        if b == 1:
            n = input("write your data:")+"\n"
            with open("Prabhatex.txt", "a") as f:
                f.write(n)
                N = "[" + str(getdate()) + "]"
                print("")
                print(N, ":DATA UPDATED SUCCESSFULLY")
        elif b == 2:
            o = input("write your data:")+"\n"
            with open("rohanex.txt", "a") as f:
                f.write(o)
                O = "[" + str(getdate()) + "]"
                print("")
                print(O, ":DATA UPDATED SUCCESSFULLY")
        else:
            p = input("write your data:")+"\n"
            with open("hammadex.txt", "a") as f:
                f.write(p)
                P = "[" + str(getdate()) + "]"
                print("")
                print(P, ":DATA UPDATED SUCCESSFULLY")
  def readfile(z):
    if z == 1:
        print("\nOk whose food data you wanna retreive\n1.Prabhat\n2.Rohan\n3.Hammad")
        a = int(input("Select number:"))
        if a == 1:
            with open("Prabhatfood.txt") as f:
                I = "[" + str(getdate()) + "]"
                print("\nNOTE:if nothing is visible below it means there is no data available.")
                print(I,":")
                for x in f:
                    print(x,end="")
        elif a == 2:
            with open("rohanfood.txt") as f:
                J = "[" + str(getdate()) + "]"
                print("\nNOTE:if nothing is visible below it means there is no data available.")
                print(J,":")
                for x in f:
                    print(x, end="")
        else:
            with open("hammadfood.txt") as f:
                K = "[" + str(getdate()) + "]"
                print("\nNOTE:(if nothing is visible below it means there is no data available.)")
                print(K,":")
                for x in f:
                    print( x, end="")
    else:
        print("\nOk whose exercise data you wanna retreive\n1.Harry\n2.Rohan\n3.Hammad")
        b = int(input("Select number:"))
        if  b == 1:
            with open("Prabhatex.txt") as f:
                L = "[" + str(getdate()) + "]"
                print("\nNOTE:(if nothing is visible below it means there is no data available.)")
                print(L,":")
                for x in f:
                    print(x, end="")
        elif b == 2:
            with open("rohanex.txt") as f:
                M = "[" + str(getdate()) + "]"
                print("\nNOTE:(if nothing is visible below it means there is no data available.)")
                print(M,":")
                for x in f:
                        print(x, end="")

        else:
            with open("hammadex.txt") as f:
                N = "[" + str(getdate()) + "]"
                print("\nNOTE:(if nothing is visible below it means there is no data available.)")
                print(N,":")
                for x in f:
                    print(x, end="")

  if x==1:
    writefile(y)
  elif x==2:
    readfile(z)
  print("")
  print("\nDO you wanna check more?\n1.YES\n2.NO")
  cont = int(input("Select number:"))
  if cont == 2:
     break
  else:
     pass
except FileNotFoundError:
    print("!------YOU ARE TRYING TO OPEN SOMETHING WHICH IS NOT AVAILABLE ON YOUR SYSTEM")
    print("ITS BETTER IF YOU FIRST LOG THE DATA AND THEN RETRIVE IT------!")
except Exception as oo:
    print(oo,"is not a number please select a number")