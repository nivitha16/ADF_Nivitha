import re
import logging

logging.basicConfig(
    filename="sample.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

file=""
class parent:
    def __init__(self,file):
        self.file=file

    def reading(self):
        file = open("nivi2.txt", "r")
        Lines=file.read()
        return Lines

    def readwrite(self):
        file = open("nivi2.txt", "r")
        Lines = file.readlines()
        return Lines

    def writecontents(self,nivi):
        with open('newday2.txt', 'w') as f:
            for items in nivi:
                f.write('%s ' % items)
        f.close()

class subclass(parent):

        def prefix(self):
            files=self.readwrite()
            nivi = []
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for s1 in string:
                    if s1 != "":
                        if (s1.startswith("to")):
                            nivi.append(s1)
            logging.debug("Starting with to".format())
            self.display(nivi)
            output=self.writecontents(nivi)

        def suffix(self):
            nivi = []
            files=self.readwrite()
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for s1 in string:
                    if s1 != "":
                        if (s1.endswith("ing")):
                            nivi.append(s1)
            logging.debug("Ending with ing".format())
            self.display(nivi)
            output = self.writecontents(nivi)

        def max_occuring(self):
            files=self.readwrite()
            list1 = []
            str1 = ""
            freq = 0
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for s in string:
                    if s != "":
                        list1.append(s)

            for i in list1:
                c = list1.count(i)
                if (c > freq):
                    freq = c
                    str1 = i

            logging.debug("Maximum occuring word".format())
            self.display(str1)
            output = self.writecontents(str1)

        def palindrome(self):
            files=self.readwrite()
            nivi = []
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for s1 in string:
                    if s1 != "":
                        rev = ''.join(reversed(s1))
                        if (s1 == rev):
                            nivi.append(s1)
            logging.debug("Palindrome".format())
            self.display(nivi)
            output = self.writecontents(nivi)

        def unique_list(self):
            list = []
            files=self.readwrite()
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for s1 in string:
                    if s1 != "":
                        list.append(s1)

            logging.debug("Unique List".format())
            self.display(list)
            output = self.writecontents(list)

        def word_dict(self):
            list1 = []
            files = self.readwrite()
            for line in files:
                string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
                for s1 in string:
                    if (s1 != ""):
                        list1.append(s1)

            for i in enumerate(list1):
                self.display(i)
                output = self.writecontents(i)
            logging.debug("Dictionary word".format())


        def split_vowels(self):
            files=self.readwrite()
            vowels = ""
            list1 = []
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for s in string:
                    if s != 0:
                        list1.append(s)
                vowels = [re.sub("[aeiouAEIOU]", "", i) for i in list1]
                for i in vowels:
                    self.display(i)
                    output = self.writecontents(i)
            logging.debug("Split Vowels".format())



        def capitalize(self):
            caps = []
            files=self.readwrite()
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for i in string:
                    ch = list(i)
                    ch[2::3] = [l.upper() for l in ch[2::3]]
                    i = ''.join(ch)
                    caps.append(i)
            self.display(caps)
            output = self.writecontents(caps)
            logging.debug("Capilatize 3rd character".format())

        def capitalize5th(self):
            files=self.readwrite()
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
                for i in range(4, len(string), 5):
                    string[i] = string[i].upper()
            self.display(string)
            output = self.writecontents(string)
            logging.debug("Capitalize fifth word".format())

        def replace(self):
            files=self.readwrite()
            for line in files:
                string = re.sub("[^a-zA-Z0-9]", " ", line)
                str = string.replace(" ", "-")
            self.display(str)
            output = self.writecontents(str)
            logging.debug("Replace space with '-' ".format())

        def newline(self):
            files=self.reading()
            input = files.replace('\n', ';')
            self.display(input)
            output = self.writecontents(input)
            logging.debug("Replace newline with semicolon ".format())

        def display(self,nivi):
            print(nivi)
            print("File written successfully")


obj=subclass(file)
#main function
def switch():
        option = int(input("enter your option: "))

        if option == 1:
            obj.prefix()
        elif option == 2:
            obj.suffix()
        elif option == 3:
            obj.max_occuring()
        elif option == 4:
            obj.palindrome()
        elif option == 5:
            obj.unique_list()
        elif option == 6:
            obj.word_dict()
        elif option == 7:
            obj.split_vowels()
        elif option == 8:
            obj.capitalize()
        elif option == 9:
            obj.capitalize5th()
        elif option == 10:
            obj.replace()
        elif option == 11:
            obj.newline()
        else:
            print("Incorrect option")

switch()
