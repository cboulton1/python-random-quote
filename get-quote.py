import random

def primary():
  #print("Keep it logically awesome.")

  with open("quotes.txt") as f:
    quotes = f.readlines()

  rnd_num_quotes = random.randint(1, len(quotes))
  
  for i in range(rnd_num_quotes):
    last_index = len(quotes) - 1
    rnd_index = random.randint(0, last_index)
    print(quotes[rnd_index].replace("\n", ""))
    quotes.remove(quotes[rnd_index])

if __name__== "__main__":
  primary()
