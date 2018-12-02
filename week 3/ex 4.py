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

freq_dict =  get_word_frequency_from_file_dict("input.txt")
print(freq_dict)
write_freq_dict_to_file("output.csv",freq_dict)

