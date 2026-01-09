def energy(text):
   text = text * 300000000 ** 2
   return(text)


def  main():
   mass = int(input("M: "))
   print(f"E: {energy(mass)}")
main()