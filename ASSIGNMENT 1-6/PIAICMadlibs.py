print('Welcome to Madlibs Game!\nFill the words below to get started:\n')

noun = str.capitalize(input('Enter a noun of place (e.g., city, place): '))
adj = str.lower(input('Enter an adjective (e.g., smelly, gigantic): '))
verb = str.lower(input('Enter a verb (e.g., dance, sneeze): '))
food = str.lower(input('Enter a type of food (e.g., samosa, halwa): '))
festival = str.capitalize(input('Enter a festival (e.g., Eid, Basant): '))
clothing = str.lower(input('Enter a type of clothing (e.g., shalwar kameez, kurta): '))

story = f"In the busy streets of {noun}, there was a {adj} shop where people would {verb} over plates of {food}. During {festival}, everyone wore {clothing} that looked like it had been designed by a mad tailor. The celebration ended with a parade of uncles wearing sunglasses."

print('Here is your Madlibs story\n')
print(story)