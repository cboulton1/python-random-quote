import random

def primary():
  
  # option to add quote(s) to quotes.txt
  response = input("Add a quote? y/n ")
  while response.lower() == "y":
    quote = input("Type quote: ")
    with open("quotes.txt", "a") as f:
      f.writelines("\n" + quote)
    print("Quote added")
    response = input("Add another quote? y/n ")
  
  with open("quotes.txt") as f:
    quotes = f.readlines()

  # print a random number of quotes from quotes.txt
  rnd_num_quotes = random.randint(1, len(quotes))
  for i in range(rnd_num_quotes):
    last_index = len(quotes) - 1
    rnd_index = random.randint(0, last_index)
    print(quotes[rnd_index].replace("\n", ""))
    quotes.remove(quotes[rnd_index])

if __name__== "__main__":
  primary()
