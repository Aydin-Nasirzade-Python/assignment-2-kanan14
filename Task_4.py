#import libraries here

def main():
  a=int(input("Enter the year [ex. 2021]: "))
  if a>0:
    if a%12 == 0:
      print(a,"is the year of the Monkey")
    elif a%12==1:
      print(a,"is the year of the Rooster")
    elif a%12==2:
      print(a,"is the year of the Dog")
    elif a%12==3:
      print(a,"is the year of the Pig")
    elif a%12==4:
      print(a,"is the year of the Rat")
    elif a%12==5:
      print(a,"is the year of the Ox")
    elif a%12==6:
       print(a,"is the year of the Tiger")
    elif a%12==7:
      print(a,"is the year of the Hare")
    elif a%12==8:
      print(a,"is the year of the Dragon")
    elif a%12==9:
      print(a,"is the year of the Snake")
    elif a%12==10:
      print(a,"is the year of the Horse")
    elif a%12==11:
      print(a,"is the year of the Sheep")
    else:
      print("Invalid year!")
  else:
    print("Invalid year!")

  pass

if __name__ == "__main__":
  main()
