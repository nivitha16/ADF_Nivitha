import re
try:
    file = open("nivi2.txt", "r")
    Lines = file.readlines()
    def prefix():
        nivi=[]
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ",line).split(" ")
            for s1 in string:
                if s1!="":
                    if(s1.startswith("to")):
                        nivi.append(s1)
        print(nivi)
        with open('newday2.txt', 'w') as f:
            for items in nivi:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()

    def suffix():
        nivi = []
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for s1 in string:
                if s1 != "":
                    if (s1.endswith("ing")):
                        nivi.append(s1)
        print(nivi)
        with open('newday2.txt', 'w') as f:
            for items in nivi:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()

    def max_occuring():
        list1 = []
        str1 = ""
        freq = 0
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for s in string:
                if s != "":
                    list1.append(s)

        for i in list1:
            c = list1.count(i)
            if (c > freq):
                freq = c
                str1 = i

        print(str1)

        with open('newday2.txt', 'w') as f:
            for items in str1:
                f.write('%s' % items)
            print("File written successfully")
        f.close()

    def palindrome():
        nivi = []
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for s1 in string:
                if s1 != "":
                    rev = ''.join(reversed(s1))
                    if (s1 == rev):
                        nivi.append(s1)
        print(nivi)
        with open('newday2.txt', 'w') as f:
            for items in nivi:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()

    def unique_list():
        list = []
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for s1 in string:
                if s1 != "":
                    list.append(s1)

        print(list)

    def word_dict():
        list1 = []
        for line in Lines:
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s1 in string:
                if (s1 != ""):
                    list1.append(s1)

        for i in enumerate(list1):
            print(i)

    def split_vowels():
        vowels = ""
        list1 = []
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for s in string:
                if s != 0:
                    list1.append(s)
            vowels = [re.sub("[aeiouAEIOU]", "", i) for i in list1]
            for i in vowels:
                print(i, end=" ")
                with open('newday2.txt', 'w') as f:
                    for items in i:
                        f.write('%s ' % items)
        print("\n")
        print("File written successfully")
        f.close()

    def capitalize():
        caps = []
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for i in string:
                ch = list(i)
                ch[2::3] = [l.upper() for l in ch[2::3]]
                i = ''.join(ch)
                caps.append(i)
        print(caps)
        with open('newday2.txt', 'w') as f:
            for items in caps:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()

    def capitalize5th():
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for i in range(4, len(string), 5):
                string[i] = string[i].upper()
        print(string)
        with open('newday2.txt', 'w') as f:
            for items in string:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()

    def replace():
        for line in Lines:
            string = re.sub("[^a-zA-Z0-9]", " ", line)
            str = string.replace(" ", "-")
        print(str)
        with open('newday2.txt', 'w') as f:
            for items in str:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()

    def newline():
        file = open("nivi2.txt", "r")
        string = file.read()
        input = string.replace('\n', ';')
        print(input)
        f2 = open("newday2.txt", "w+")
        f2.write(input)
        f2.close()


    def switch():
        option = int(input("enter your option: "))

        if option == 1:
            prefix()
        elif option == 2:
            suffix()
        elif option == 3:
            max_occuring()
        elif option == 4:
            palindrome()
        elif option == 5:
            unique_list()
        elif option == 6:
            word_dict()
        elif option == 7:
            split_vowels()
        elif option == 8:
            capitalize()
        elif option == 9:
            capitalize5th()
        elif option == 10:
            replace()
        elif option == 11:
            newline()
        else:
            print("Incorrect option")


    switch()
except:
    print("An exception occured")