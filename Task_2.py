#import libraries here

def main():
  a=input("Enter name of the month [ex. June]: ")
  b=int(input("Enter the day [ex. 5]: "))
  if a=="January" or a=="February" or a=="March" or a=="April" or a=="May" or a=="June" or a=="July" or a=="August" or a=="September" or a=="October" or a=="November" or a=="December":
    if 0<b<=31:
      if (a=="March"  and b>=20) or a=="April" or a=="May" or (a=="June" and b<21):
        print(a,b,"is in Spring")
      if (a=="September" and b<22) or a=="July" or a=="August" or (a=="June" and b>=21):
        print(a,b,"is in Summer")
      if (a=="September" and b>=22) or a=="October" or a=="November" or (a=="December" and b<21):
        print(a,b,"is in Fall")
      if (a=="December" and b>=21) or a=="January" or a=="February" or (a=="March" and b<20):
        print(a,b,"is in Winter")
  pass

if __name__ == "__main__":
  main()
