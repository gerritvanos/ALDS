import string

def get_word_frequency_from_file_dict(file_name):
    input_file = open(file_name, "r")
    words_dict = {}
    for line in input_file:
        for word in line.split():
            #delete punctuation:
            table = str.maketrans({key: None for key in string.punctuation})
            word = word.translate(table)
            word = word.lower()
            if word is not '':
                if word not in words_dict:
                    words_dict[word] = 1
                else:
                    words_dict[word] += 1
    return words_dict

def write_freq_dict_to_file(file_name,freq_dict):
    output_file = open(file_name,"w")
    output_file.write("sep=;\n")
    output_file.write("word;frequency\n")
    for key in freq_dict:
        output_string = key + ";" + str(freq_dict.get(key)) + "\n"
        output_file.write(output_string)
    output_file.close()



class trie_node:
    def __init__(self,next_nodes,freq=0):
        self.freq = freq
        self.next_nodes = next_nodes

    def write_to_file(self,output_file,word = None):
        if self.freq > 0:
            output_string = word +";" +str(self.freq) + "\n"
            output_file.write(output_string)
        if self.next_nodes:
            for node in self.next_nodes:
                self.next_nodes[node].write_to_file(output_file,node)

class trie:
    def __init__(self):
        self.root = trie_node({})

    def add_word(self,word):
        current = self.root
        if word[0] not in current.next_nodes:  # add first letter of the word when not in next_nodes from the root
            current.next_nodes[word[0]] = trie_node({})
        current = current.next_nodes[word[0]]
        if len(word) <= 1:
            current.freq += 1
        for letters in range(1, len(word)):
            w = word[:letters + 1]
            if w not in current.next_nodes:
                current.next_nodes[w] = trie_node({})
            if letters == len(word) - 1:
                current.next_nodes[w].freq += 1
                return
            current = current.next_nodes[w]


    def fill_from_file(self,file_name):
        input_file = open(file_name,'r')
        for line in input_file:
            for word in line.split():
                # delete punctuation:
                table = str.maketrans({key: None for key in string.punctuation})
                word = word.translate(table)
                word = word.lower()
                if word is not '':
                    self.add_word(word)

    def write_to_file(self,file_name):
        output_file = open(file_name,"w")
        output_file.write("sep=;\n")
        output_file.write("word;frequency\n")
        self.root.write_to_file(output_file)



def test_freq_table():

    freq_dict =  get_word_frequency_from_file_dict("input.txt") #create dictionary with words and freqencies
    print(freq_dict) #show dict on screen
    write_freq_dict_to_file("output_dict.csv",freq_dict) #wirte dict as frequency table to output_dict.csv

    t = trie() #make empty trie
    t.fill_from_file("input.txt") #fill trie with contents of input.txt
    t.write_to_file("output_trie.csv")#write freqency table to output_trie.csv

test_freq_table()