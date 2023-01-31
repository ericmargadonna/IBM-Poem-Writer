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

def getFontsForOS(title_size, body_size):
    import os
    if os.name == "nt":
        return ImageFont.truetype("arial.ttf", title_size), ImageFont.truetype("arialbd.ttf", body_size)
    elif os.name == "posix":
        return ImageFont.truetype("/Library/Fonts/Arial.ttf", title_size), ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", body_size)
    
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

def generateImage(m_title, m_lines, title_size=20, start_size=9):
    # This function generates an image of the poem
    # It takes in the title and lines of the poem and returns
    # an image object

    # In an IMB poem, each time a word is used, the font size
    # is increased by 1. So, we need to keep track of how many times 
    # each word is used, not including the title.

    # Set up the image
    image_width = len(max(m_lines))*15
    image_height = len(m_lines)*20+ 75

    image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    titlefont, bodyfont = getFontsForOS(title_size, start_size)

    # Draw the title
    draw.text((10, 10), m_title.upper(), (0, 0, 0), font=titlefont)

    # Set up the word count dictionary
    wordcount = {}

    # Set up the line count
    linecount = 0

    # Set up the x and y position
    x = 10
    y = 40

    #set padding
    padding = 2

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

            #Create a variable for the text to be drawn
            text = word.upper() + " "

            bodyfont = bodyfont.font_variant(size=wordcount[word] + start_size)

            # Draw the word
            draw.text((x, y), text, (0, 0, 0), font=bodyfont)
           
            #Increment the x position by the size of the word
            x += bodyfont.getsize(text)[0]
    
        # Increment the y position by 10 + the size of the largest word
        y += max(wordcount.values()) + start_size + padding
        #Reset the x position
        x = 10

    filename = "photos/" + m_title.replace(" ", "_") + ".png"
    image.save(filename)

if __name__ == "__main__":

    print( "Enter 26 words, one for each letter of the alphabet:\n" )

    # Start by setting the vocabulary for your IBM poem
    # This is done by entering a word for each letter of the alphabet
    
    vocab_dict = {k: v  for k, v in 
                zip(string.ascii_lowercase, 
                [input(f"{string.ascii_lowercase[i]}: ").lower() 
                for i in range(0,26)])
                }

    # Then, enter a three letter word or phrase that acts as a 'seed' for the poem
    
    startletters = input("Enter 3 letter word or phrase (i.e. 'IBM'): ").lower()
    
    # Finally, generate the poem
    title, lines = writePoem(startletters, vocab_dict)

    # And print it out!
    print()
    print(title)
    print()
    for line in lines:
        print(line)

    # And generate an image of the poem
    generateImage(title, lines)