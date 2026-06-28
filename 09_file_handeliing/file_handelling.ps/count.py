import sys
# def count_lines(filename):
#     with open(filename) as f:
#         return len(f.readlines())
    
# if __name__=="__main__":
#     filename=sys.argv[0]
#     num_lines=count_lines(filename)
#     print(f"the number lines in {filename} are {num_lines}")
    
# # python 09_file_handeliing/file_handelling.ps/count.py tasks.txt

def search_word(word,string):
    return string.count(word)

if __name__=="__main__":
    if len(sys.argv) != 3:
        print("Usage: python count.py <filename> <word>")
        sys.exit()

    filename=sys.argv[1]
    word=sys.argv[2]
    with open(filename) as f:
        string=f.read()
        b=search_word(word,string)
        print(f"the occurences are {b} is  '{word}' in file")
        
# python 09_file_handeliing/file_handelling.ps/count.py tasks.txt line