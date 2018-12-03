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



class trie:
    def __init__(self):
        self.root = trie_node({})

    def fill_from_file(self,file_name):
        input_file = open(file_name,'r')
        for line in input_file:
            for word in line.split():
                # delete punctuation:
                table = str.maketrans({key: None for key in string.punctuation})
                word = word.translate(table)
                word = word.lower()
                if word is not '':
                    if word[0] not in self.root.next_nodes: #add first letter of the word
                        self.root.next_nodes[word[0]] = trie_node({})
                    current = self.root.next_nodes[word[0]]
                    for letters in range(1,len(word)):
                        w = word[:letters+1]
                        print(w,letters)
                        if w not in current.next_nodes:
                            current.next_nodes[w] = trie_node({})
                        if letters == len(word)-1:
                            print("freq increment")
                            current.next_nodes[w].freq +=1
                            break
                        current = current.next_nodes[w]

    def get_word(self):
        current = self.root
        print(current.next_nodes)
        current = current.next_nodes['c']
        print(current.next_nodes)
        current = current.next_nodes["ca"]
        print(current.freq)
        current = current.next_nodes["can"]
        print(current.freq)
        print(current.next_nodes)

    def write_to_csv(self,file_name):
        output_file = open(file_name,"w")




freq_dict =  get_word_frequency_from_file_dict("input.txt")
print(freq_dict)
write_freq_dict_to_file("output.csv",freq_dict)
t = trie()
t.fill_from_file("input.txt")
t.get_word()

