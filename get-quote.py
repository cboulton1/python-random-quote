import random

def primary():
  #print("Keep it logically awesome.")

  with open("quotes.txt") as f:
    quotes = f.readlines()

  last = len(quotes) - 1 # last index in array
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
