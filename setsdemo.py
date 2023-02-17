letter = input("Enter a letter: ").lower()
guessed_letters = set()

while letter:
  guessed_letters.add(letter)
  print(guessed_letters)
  letter = input("Enter a letter: ").lower()

print("DONE")
print(f"You guessed: {len(guessed_letters)} letters." )

  