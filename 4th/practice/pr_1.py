
#1
text = "Star Trek: Birth of the Federation is a 4X turn-based strategy video game developed by MicroProse and published by Hasbro Interactive. The game was initially released on May 25, 1999 for Windows personal computers."
h_letters = [letter for letter in text if letter != 'a']
google = ''.join(h_letters)
print(google)

#2
without_a = text.replace("a", "")
print(without_a)

#3
cut = text[135:]
print(cut)


#4
text_split = text.split()
print(text_split)

