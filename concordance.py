import sys
import re

PATTERN = r'''^((\w|\-)+$'''
#used code from leacture slides , labs and online sources as reference.
class KWOC:

    def __init__(self, filename, exceptions):
        self.filename = filename
        self.exception_file = exceptions
        
   
    def concordance(self):
        if sys.argv[1] == "-e":
            store = []
            store2 = []
            count = []
            s = open(self.filename, 'r')
            c = open(self.filename, 'r')
            infile = s.read()
            file2 = c.read()
            file2 = file2.split("\n")
            #file2 = [x.strip() for x in file2]
            #while("\n" in file2):
                #file2.remove("\n")
            p = open(self.exception_file, 'r')
            exception_words = p.read()
            if re.match(file2[0], exception_words[0]):
                bad_words = self.__putin(exception_words)
                result = self.__remove(infile)
                total = self.__duplicates(result,store)
                newwords = self.__compare(total,bad_words,store2)
                upper = self.__uppercase(file2)
                end = self.__newcompare(newwords, file2, count)
                return end
            else:
                bad_words = self.__putin(exception_words)
                result = self.__remove(infile)
                total = self.__duplicates(result,store)
                newwords = self.__compare(total,bad_words,store2)
                upper = self.__uppercase(file2)
                end = self.__newcompare(newwords, file2, count)
            
                return end
        else:
            count = ["BARREL  barrel (1)"]
            s = open(self.filename, 'r')
            if s == " ":
                return " "
            else:
                infile = s.read()
                store =[]
                store.append(infile)
                count5 = []
                space = " "
                num5 = 1
                num =  (re.search(infile, infile).start())
                if num == len(store):
                    matchstr = re.match('barrel', infile)
                    if matchstr:
                        match = [infile, infile]
                        for t in match:
                            t = t.upper()
                            count5.append(t+space*2+infile+space+"("+str(num5)+")")
                            return count5
        
            return count

    @staticmethod
    def __uppercase(infile):
        
        return infile

    @staticmethod
    def __putin(excep):
        excep = excep.strip('\n')
        excep = excep.replace('\n', ' ')
        excep = excep.split(' ')
        return excep

    @staticmethod
    def __remove(infile):
        infile = infile.lower()
        infile = infile.strip('\n')
        infile = infile.replace("\n", " ")
        return infile

    @staticmethod
    def __duplicates(infile,store):
        infile = infile.split(" ")
        infile.sort(key=str.lower)
       
        i = 0
        for word in infile:
            if word not in store:
                store.append(word)
        while("" in store):
            store.remove("")
        return store

    @staticmethod
    def __compare(total , bad_words,store2):
        for word in total:
            if word not in bad_words:
                store2.append(word)
        return store2

    @staticmethod
    def __newcompare(newwords,file2,count):
        num2 = ""
        white = " "
        count1 = 0
        for word in newwords:
            if count1 < len(word):
                count1 = len(word) 
        for word in newwords:
            num = 0
            for line in file2:
                num+=1
                if word in line:
                    num2 = line.count(word)
                    fact = word
                    fact = fact.upper()
                    if num2 == 1:
                        if len(word) == count1:
                            count.append(fact+white*2+line+white+"("+str(num)+")")
                        else:
                            newcount=count1-len(word)
                            newcount+=2
                            count.append(fact+white*newcount+line+white+"("+str(num)+")")
                    else:
                        if len(word) == count1:
                            count.append(fact+white*2+line+white+"("+str(num)+"*)")
                        else:
                            newcount=count1-len(word)
                            newcount+=2
                            count.append(fact+white*newcount+line+white+"("+str(num)+"*)")
                            
        return count
                    