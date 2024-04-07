#import libraries here

def main():
  a=input("Enter a month [ex. March]: ")
  b=int(input("Enter the day [ex. 12]: "))
  if (1<=a<=31) or (b=="Januray" or b=="February" or b=="March" or b=="April" or b=="May" or b=="June" or b=="July" or b=="August" or b=="September" or b=="October" or b=="November" or b=="December":
    if (a=="December" and b>=22) or (a=="January" and b<=19):
      print("Your zodiac sign is Capricorn")
    elif (a=="January" and b>=20) or (a=="February" and b<=18):
      print("Your zodiac sign is Aquarius")
    elif (a=="February" and b>=19) or (a=="March" and b<=20):
      print("Your zodiac sign is Pisces")
    elif (a=="March" and b>=21) or (a=="April" and b<=19):
      print("Your zodiac sign is Aries")
    elif  (a=="April" and b>=20) or (a=="May" and b<=20):
      print("Your zodiac sign is Taurus")
    elif (a=="May" and b>=21) or (a=="June" and b<=20):
      print("Your zodiac sign is Gemini")
    elif (a=="June" and b>=21) or (a=="July" and b<=22):
      print("Your zodiac sign is Cancer")
    elif (a=="July" and b>=23) or (a=="August" and b<=22):
      print("Your zodiac sign is Leo")
    elif (a=="August" and b>=23) or (a=="September" and b<=22):
      print("Your zodiac sign is Virgo")
    elif (a=="September" and b>=23) or (a=="October" and b<=22):
      print("Your zodiac sign is Libra")
    elif (a=="October" and b>=23) or (a=="November" and b<=21):
      print("Your zodiac sign is Scorpion")
    elif (a=="November" and b>=22) or (a=="December" and b<=21):
      print("Your zodiac sign is Sagittarius")
  pass

if __name__ == "__main__":
  main()
