import matplotlib.pyplot as plt

# holds the list of the words in the file
words_list = []

# open the file and read all words into "word_list"
with open('words.txt', 'r') as f:
    for line in f:
        for word in line.split(","):
            if word[-1] == "\n":
                word = word[0:len(word) - 1:1]
            words_list.append(word.lower())


# generate words by a character (including or excluding)
def words_generator(character, include=True):
    character = character.lower()
    for inner_word in words_list:
        if (character in inner_word and include) or (character not in inner_word and not include):
            yield inner_word


# find how many times a character appears in the file
def find_how_many_times(character):
    counter = 0
    for inner_word in words_list:
        for inner_character in inner_word:
            if inner_character == character:
                counter += 1
    return counter


# get the x axis values
def get_x_axis(nubmer_of_characters=10):
    x_axis = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    if nubmer_of_characters > len(abc):
        nubmer_of_characters = len(abc)
    for i in range(0, nubmer_of_characters, 1):
        x_axis.append(abc[i])
    return x_axis


# get the y axis for the x axis values
def get_y_axis_for_some_x_axis(x_axis):
    y_axis = []
    for character in x_axis:
        y_axis.append(find_how_many_times(character))
    return y_axis


def initiate_graph():
    # x axis values
    x = get_x_axis()

    # corresponding y axis values
    y = get_y_axis_for_some_x_axis(x)

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('character')
    # naming the y axis
    plt.ylabel('how many times')

    # giving a title to my graph
    plt.title('characters graph!')


# function to show the plot
def show_graph():
    initiate_graph()
    plt.show()
