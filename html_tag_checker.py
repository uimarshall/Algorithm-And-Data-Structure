class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

s = Stack()

#===========================================================================
#Takes the file and extracts the opening and closing tags from  the html file
def read_file(filename):
    """This function takes an html file as an input and returns a list
     containing all the characters as items int the list except the newline
     character and space"""
    with open(filename,'r') as f:
        reader = f.read()
        file_char = []
        for item in reader:
            if item == '\n' or item == ' ':
                pass
            else:
                file_char.append(item)
        return file_char

#===========================================================================
#Takes the output from read_file function, extracts only the html symbols and rearranges them
def remove_unwanted_char(html_ls):
    """Takes in a list of all individual characters in an html file and creates
    a new list containing all opening angle brackets followed by the closing
    angle brackets"""
    html_open_tags = []
    html_close_tags = []
    for char in file_char:
        if char == "<":
            html_open_tags.append(char)
        elif char == ">":
            html_close_tags.append(char)
    #appending the closing tag to the openiing tag
    for char in html_close_tags:
        html_open_tags.append(char)
    #list_symbol_string = str(new_symbol_open_string)
    #print(html_open_tag)
    return html_open_tags

#===========================================================================
#Takes the output from remove_unwanted_char and checks if symbols balance up
def html_tag_checker(symbol_list):
    """This function takes in a list containing html opening then closing
    angle brackets. It returns True if all opening and closing brackets
    balance out and returns False otherwise"""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_list) and balanced:
        symbol = symbol_list[index]
        if symbol == "<":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


#print(read_file('helloworld.html'))
file_char = read_file('helloworld.html')
symbol_list = remove_unwanted_char(file_char)
print(html_tag_checker(symbol_list))
