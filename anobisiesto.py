def anobi ():

    añobisiesto: int = int (input("ingrese año"))

    if(añobisiesto % 4 == 0 and (añobisiesto % 100 != 0 or añobisiesto% 400 == 0)):
        print(f" elaño {añobisiesto} si es bisiesto")
    else:
      print(f" El año {añobisiesto} NO es bisiesto")

print(anobi())
