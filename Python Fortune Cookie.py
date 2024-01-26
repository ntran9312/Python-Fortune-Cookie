# Write a program that:
  # Asks for the user’s name.
  # Asks the user to input a number between 1 and 5.
  # Outputs a personalised fortune/message (that includes the user’s name) depending on which number they picked.

name = input("What is your name?:")
two = "You will grow an extra 5 inches tonight"
three = "You will shrink 3 inches"
four = "You will stub your toe tonight"
five = "You will find $5 later today"

fortune = input("Enter a number 1-5:")
if fortune == "1":
  print("Today is your lucky day " + name + ", you will recieve $100 000 tomorrow!")
elif fortune == "2":
  print("It seems you are on the short side " + name + ", you will grow 5 more inches tonight")
elif fortune == "3":
  print("You did not luck out today " + name + ", you will shrink 3 inches")
elif fortune == "4":
  print("You will stub your toe tonight " + name)
elif fortune == "5":
  print("This may not be the lottery " + name + ", but you are going to find $5 today")
else:
  print("Sorry that is not in my system")
  
