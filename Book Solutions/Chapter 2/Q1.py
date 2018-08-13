import sys
import unicodedata
def print_unicode_table(words):
        print("decimal   hex   chr  {0:^40}\n".format("name"))
        print("-------  -----  ---  {0:-<40}\n".format(""))

        for code in range(ord(" "),sys.maxunicode+1):
            c=chr(code)
            if words.find(c)!=-1:
                try:
                    name=unicodedata.name(c)
                except ValueError:
                    continue
                print("{0:7}  {0:5X}  {0:^3c}  {1}\n".format(code, name.title()))
            
x=input("Enter the words: ")
print_unicode_table(x)
