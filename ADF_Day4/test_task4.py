"""Day 4"""
import re
import logging
# import pytest
import config as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

class TestParent:
    """Class"""
    @classmethod
    def reading(cls):
        """method"""
        x_var="nivi2.txt"
        with open(x_var, "r") as file:
            lines = file.read()
        return lines

    @classmethod
    def readwrite(cls):
        """method"""
        x_var = "nivi2.txt"
        with open(x_var, "r") as file:
            lines = file.readlines()
        return lines

    @classmethod
    def display(cls,output):
        """method"""
        print(output)
        print("File written successfully")

    @classmethod
    def writecontents(cls,nivi):
        """method"""
        with open(Y_VAR, 'w') as file1:
            for items in nivi:
                file1.write('%s ' % items)
        file1.close()

class TestSubclass(TestParent):
    """Class"""

    def prefix(self):
        """method"""
        files = self.readwrite()
        nivi = []
        count = 0
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for str1 in string:
                if str1 != "":
                    if str1.startswith("to"):
                        nivi.append(str1)
                        count = count + 1
        self.display(count)
        logging.debug("Starting with to")
        return nivi

    def test_prefix(self):
        """method"""
        res1 = self.prefix()
        res2 = ['to','together','tonight']
        assert res1 == res2

    def suffix(self):
        """method"""
        nivi = []
        files = self.readwrite()
        count =0
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for str1 in string:
                if str1 != "":
                    if str1.endswith("ing"):
                        nivi.append(str1)
                        count = count + 1
        logging.debug("Ending with ing")
        self.display(nivi)
        self.writecontents(nivi)
        return nivi

    def test_suffix(self):
        """method"""
        res1 = self.suffix()
        res2 = ['going', 'coming']
        assert res1 == res2

    def max_occuring(self):
        """method"""
        files = self.readwrite()
        list1 = []
        str1=""
        str2=""
        freq = 0
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for str1 in string:
                if str1 != "":
                    list1.append(str1)

        for i in list1:
            cnt = list1.count(i)
            if cnt > freq:
                freq = cnt
                str2 = i

        logging.debug("Maximum occuring word")
        self.display(str2)
        self.writecontents(str2)
        return str2

    def test_max(self):
        """method"""
        res1 = self.max_occuring()
        res2 = "aaa"
        assert res1 == res2

    def palindrome(self):
        """method"""
        files = self.readwrite()
        nivi = []
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for str1 in string:
                if str1 != "":
                    rev = ''.join(reversed(str1))
                    if str1 == rev:
                        nivi.append(str1)
        logging.debug("Palindrome")
        self.display(nivi)
        self.writecontents(nivi)
        return nivi

    def test_palindrome(self):
        """method"""
        res1 = self.palindrome()
        res2 = ['aaa', 'malayalam', 'madam', 'aaa', 'bbb', 'aaa']
        assert res1 == res2

    def unique_list(self):
        """method"""
        list1 = []
        files = self.readwrite()
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for str1 in string:
                if str1 != "":
                    list1.append(str1)
        unique = []
        for x in list1:
            if x not in unique:
                unique.append(x)

        logging.debug("Unique List")
        self.display(unique)
        self.writecontents(unique)
        return unique

    def test_unique(self):
        """method"""
        res1 = self.unique_list()
        res2 = ['to', 'together', 'aaa', 'malayalam', 'madam', 'bbb', 'abd',
                'dcb', 'hello', 'going', 'coming', 'tonight']
        assert res1 == res2

    def word_dict(self):
        """method"""
        count=0
        list1 = []
        files = self.readwrite()
        for line in files:
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for str1 in string:
                if str1 != "":
                    list1.append(str1)

        for i in enumerate(list1):
            self.display(i)
            count = count +1
            self.writecontents(i)
        logging.debug("Dictionary word")
        return count

    def test_word(self):
        """method"""
        res1 = self.word_dict()
        res2 = 18
        assert res1 == res2

    def split_vowels(self):
        """method"""
        files = self.readwrite()
        vowels = ""
        list1 = []
        count = 0
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for str1 in string:
                if str1 != 0:
                    list1.append(str1)
            vowels = [re.sub("[aeiouAEIOU]", "", i) for i in list1]
            for i in vowels:
                self.display(i)
                self.writecontents(i)
                count = count + 1
            self.display(count)
        logging.debug("Split Vowels")
        return count

    def test_splitvowels(self):
        """method"""
        res1 = self.split_vowels()
        res2 = 22
        assert res1 == res2

class TestChild(TestParent):
    """class"""

    def capitalize(self):
        """method"""
        caps = []
        files = self.readwrite()
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for i in string:
                letter1 = list(i)
                letter1[2::3] = [l.upper() for l in letter1[2::3]]
                i = ''.join(letter1)
                caps.append(i)
        self.display(caps)
        self.writecontents(caps)
        logging.debug("Capilatize 3rd character")
        return caps

    def test_caps1(self):
        """method"""
        res1 = self.capitalize()
        res2 = ['to', 'toGetHer', '', 'aaA', 'maLayAlaM', 'maDam', 'aaA', 'bbB', 'abD',
                'abD', 'abD', 'dcB', 'dcB', 'dcB', 'aaA', 'heLlo', 'goIng', 'coMinG', 'toNigHt']
        assert res1 == res2

    def capitalize5th(self):
        """method"""
        files = self.readwrite()
        string=""
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for i in range(4, len(string), 5):
                string[i] = string[i].upper()
        self.display(string)
        self.writecontents(string)
        logging.debug("Capitalize fifth word")
        return string

    def test_caps2(self):
        """method"""
        res1 = self.capitalize5th()
        res2 = ['aaa', 'malayalam', 'madam', 'aaa', 'BBB', 'abd', 'abd',
                'abd', 'dcb', 'DCB', 'dcb', 'aaa', 'hello', 'going', 'COMING', 'tonight']
        assert res1 == res2

    def replace(self):
        """method"""
        str1=""
        files = self.readwrite()
        for line in files:
            string = re.sub("[^a-zA-Z0-9]", " ", line)
            str1 = string.replace(" ", "-")
        self.display(str1)
        self.writecontents(str1)
        logging.debug("Replace space with '-' ")
        return str1

    def test_replace(self):
        """method"""
        res1 = self.replace()
        res2 = "aaa-malayalam-madam-aaa-bbb-abd-abd-" \
                "abd-dcb-dcb-dcb-aaa-hello-going-coming-tonight"
        assert res1 == res2

    def newline(self):
        """method"""
        files = self.reading()
        input1 = files.replace('\n', ';')
        self.display(input1)
        self.writecontents(input1)
        logging.debug("Replace newline with semicolon ")
        return input1

    def test_newline(self):
        """method"""
        res1 = self.newline()
        res2 = "to together;aaa malayalam madam aaa bbb " \
               "abd abd abd dcb dcb dcb aaa hello going coming tonight"
        assert res1 == res2

# MAIN FUNCTION
#
Y_VAR = cfg.names["outputfilename"]

obj=TestSubclass()
ob=TestChild()
obj.prefix()
obj.suffix()
obj.max_occuring()
obj.palindrome()
obj.unique_list()
obj.word_dict()
obj.split_vowels()
ob.capitalize()
ob.capitalize5th()
ob.replace()
ob.newline()
obj.test_prefix()
obj.test_suffix()
obj.test_max()
obj.test_palindrome()
obj.test_unique()
obj.test_word()
obj.test_splitvowels()
ob.test_caps1()
ob.test_caps2()
ob.test_replace()
ob.test_newline()
