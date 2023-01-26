import string

print( "Enter 26 words, one for each letter of the alphabet:\n" )

vocab_dict = {k: v  for k, v in zip(string.ascii_lowercase, [input(f"{i}: ").lower() for i in range(0,26)] )}

# Start with this and J A V to get Boat Patriot Twitter
# vocab_dict = {
#     "a": "patriot",
#     "b": "ensure",
#     "c": "wise",
#     "d": "board",
#     "e": "guards",
#     "f": "shirt",
#     "g": "hot",
#     "h": "spoiled",
#     "i": "this",
#     "j": "boat",
#     "k": "fire",
#     "l": "village",
#     "m": "blaze",
#     "n": "four",
#     "o": "dragon",
#     "p": "scene",
#     "q": "show",
#     "r": "baby",
#     "s": "audio",
#     "t": "gasp",
#     "u": "air",
#     "v": "twitter",
#     "w": "orcs",
#     "x": "fall",
#     "y": "doubt",
#     "z": "change"
# }

startletters = input("Enter 3 letter word or phrase (i.e. 'IBM'): ").lower()

title = ""

lines = []

def getVocab(letter):
    return vocab_dict[letter]

def makeLine(word):
    line = ""
    for letter in word:
        line += getVocab(letter) + " "
    return line

def makeTitle(m_letters):
    m_title = ""
    for letter in m_letters.split():
        print(letter)
        print(getVocab(letter))
        m_title += getVocab(letter) + " "
    return m_title
    
def firstThreeLines(title):
    titlewords = title.split()
    for word in titlewords:
        lines.append(makeLine(word))

def finishPoem():
    for i in range(0, 3):
        words = lines[i].split()
        for word in words:
            m_line = ""
            for letter in word:
                m_line += getVocab(letter) + " "
            lines.append(m_line)

title = makeTitle(startletters)
firstThreeLines(title)
finishPoem()

print("Title: " + title)
for line in lines:
    print(line+"\n")   
