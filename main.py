import string




# Start with this and J A V to get Boat Patriot Twitter
BPT_vocab_dict = {
    "a": "patriot",
    "b": "ensure",
    "c": "wise",
    "d": "board",
    "e": "guards",
    "f": "shirt",
    "g": "hot",
    "h": "spoiled",
    "i": "this",
    "j": "boat",
    "k": "fire",
    "l": "village",
    "m": "blaze",
    "n": "four",
    "o": "dragon",
    "p": "scene",
    "q": "show",
    "r": "baby",
    "s": "audio",
    "t": "gasp",
    "u": "air",
    "v": "twitter",
    "w": "orcs",
    "x": "fall",
    "y": "doubt",
    "z": "change"
}

def getVocab(m_letter, m_vocab_dict):
    return m_vocab_dict[m_letter]

def makeLine(m_word, m_vocab_dict):
    line = ""
    for letter in m_word:
        line += getVocab(letter, m_vocab_dict) + " "
    return line

def makeTitle(m_seed, m_vocab_dict):
    m_title = ""
    for letter in m_seed:
        m_title += getVocab(letter, m_vocab_dict) + " "
    return m_title

def writePoem(m_seed, m_vocab_dict):
    m_title = makeTitle(m_seed, m_vocab_dict)

    titlewords = m_title.split()
    m_lines = []
    
    for word in titlewords:
        m_lines.append(makeLine(word, m_vocab_dict))
    
    for i in range(0,3):
        for word in m_lines[i].split():
            m_line = ""
            for letter in word:
                m_line += getVocab(letter, m_vocab_dict) + " "
            m_lines.append(m_line)
    
    return m_title, m_lines

if __name__ == "__main__":

    print( "Enter 26 words, one for each letter of the alphabet:\n" )

    #Start by setting the vocabulary for your IBM poem
    #This is done by entering a word for each letter of the alphabet
    # vocab_dict = {k: v  for k, v in 
    #             zip(string.ascii_lowercase, 
    #             [input(f"{string.ascii_lowercase[i]}: ").lower() 
    #             for i in range(0,26)])
    #             }

    #Then, enter a three letter word or phrase that acts as a 'seed' for the poem
    startletters = input("Enter 3 letter word or phrase (i.e. 'IBM'): ").lower()
    
    title, lines = writePoem(startletters, BPT_vocab_dict)
    print(title.upper())
    for line in lines:
        print(line)
