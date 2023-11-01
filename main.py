
print("=========Python Auction Project=========")
name = input("What is your name? \n")
print(f"Hello {name}!")

def auction():
  item = input(f"{name} what is the name of the item you are selling?\n")
  price = float(input(f"How much do you want to post the {item} for {name}?\n$"))
  
  return name, item, price




def options(name, item, price):
  while True:
      option = input(f"Do you wish to bid on the {item} for ${price}? \n\tYes or No\n")
      if option.lower() in ["yes", "y"]:
          while True:
              bid = float(input(f"How much do you want to bid on the {item}: \n$"))
              if bid >= price:
                  return f"Congratulations {name}, you have won the auction on the {item} for the price of ${bid}!"
              else: 
                  print(f"\nYou have been outbid!\nPlease place a higher bid!\nThe {item} has a minimum bid price of ${price}\n")
      elif option.lower() in ["no", "n"]:
          print(f"{name} has chosen not to bid on the {item}")
          item = input(f"{name} what is the name of the item you are selling?\n")
          price = float(input(f"How much do you want to post the {item} for?\n$"))
      else:
          print("Enter a valid option")



while True: 
    name, item, price = auction()
    result = options(name, item, price)

    print(result)

