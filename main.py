import string
from PIL import Image, ImageDraw, ImageFont

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

def getVocabWord(m_letter, m_vocab_dict):
    # Wrapper function to get a word from the vocabulary dictionary
    return m_vocab_dict[m_letter]

def makeLine(m_word, m_vocab_dict):
    # This function takes a word and returns a line of the poem based
    # on the IBM Poem rules 
    # (each letter is used to make a word of a new line)
    line = ""
    for letter in m_word:
        line += getVocabWord(letter, m_vocab_dict) + " "
    return line

def makeTitle(m_seed, m_vocab_dict):
    # This function takes in the 3 seed letters and creates the title
    # from the vocab dictionary
    m_title = ""
    for letter in m_seed:
        m_title += getVocabWord(letter, m_vocab_dict) + " "
    return m_title

def writePoem(m_seed, m_vocab_dict):
    # This is the main function that generates the poem
    # It takes in the seed and vocab dictionary, runs the 
    # helper functions and returns the title and lines of the poem

    # Create the title
    m_title = makeTitle(m_seed, m_vocab_dict)
    # Set up the lines list
    m_lines = []
    
    # For each word in the title, generate a line
    for word in m_title.split():
        m_lines.append(makeLine(word, m_vocab_dict))
    
    # Because of the rules of the IBM poem, we know that the title is
    # always three words long. So, we go over the first three lines 
    # that were just generated and generate new lines for each word in 
    # those first three lines
    for i in range(0,3):
        for word in m_lines[i].split():
            m_line = ""
            for letter in word:
                m_line += getVocabWord(letter, m_vocab_dict) + " "
            m_lines.append(m_line)
    
    # And that's it! We have our poem!
    # Return the title and lines as separate variables
    return m_title, m_lines

def generateImage(m_title, m_lines):
    # This function generates an image of the poem
    # It takes in the title and lines of the poem and returns
    # an image object

    # In an IMB poem, each time a word is used, the font size
    # is increased by 1. So, we need to keep track of how many times 
    # each word is used, not including the title.

    # Set up the image
    image = Image.new("RGB", (800, 600), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    titlefont = ImageFont.truetype("arialbd.ttf", 20,)

    # Draw the title
    draw.text((10, 10), m_title.upper(), (0, 0, 0), font=titlefont)

    # Define the base font to be used for the body
    bodyfont = ImageFont.truetype("arial.ttf", 9)

    # Set up the word count dictionary
    wordcount = {}

    # Set up the line count
    linecount = 0

    # Set up the y position
    y = 40

    # For each line in the poem
    for line in m_lines:
        # For each word in the line
        for word in line.split():
            # If the word is in the word count dictionary
            if word in wordcount:
                # Increment the count by 1
                wordcount[word] += 1
            else:
                # Otherwise, add the word to the dictionary with a count of 1
                wordcount[word] = 1
            # Draw the word
            draw.text((10, y), word.upper(), (0, 0, 0), font=bodyfont)
            # Increment the y position by 10
            y += 10
        # Increment the line count by 1
        linecount += 1
        # Increment the y position by 10
        y += 10

    filename = m_title.replace(" ", "_") + ".png"
    image.save(filename)

    # Return 0 for success
    return 0

if __name__ == "__main__":

    print( "Enter 26 words, one for each letter of the alphabet:\n" )

    # Start by setting the vocabulary for your IBM poem
    # This is done by entering a word for each letter of the alphabet
    
    # vocab_dict = {k: v  for k, v in 
    #             zip(string.ascii_lowercase, 
    #             [input(f"{string.ascii_lowercase[i]}: ").lower() 
    #             for i in range(0,26)])
    #             }

    # Then, enter a three letter word or phrase that acts as a 'seed' for the poem
    
    startletters = input("Enter 3 letter word or phrase (i.e. 'IBM'): ").lower()
    
    # Finally, generate the poem
    title, lines = writePoem(startletters, BPT_vocab_dict)

    # And print it out!
    print()
    print(title)
    print()
    for line in lines:
        print(line)

    # And generate an image of the poem
    generateImage(title, lines)
