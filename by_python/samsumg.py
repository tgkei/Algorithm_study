class Samsung():
    def __init__(self):
        self.arr =[]
        self.dic= {}
    
    def appendWord(self,word):
        self.arr.append(word)
        if word in self.dic:
            self.dic[word].append(idx)
        else:
            self.dic[word] = [idx]
    
    def changeWord(self,word1,word2):
        temp = []
        for idx in self.dic[word1]:
            self.arr[idx] = word2
            temp.append(idx)
        self.dic.pop(word1)
        if word2 not in self.dic:
            self.dic[word2] = []

        for t in temp:
            self.dic[word2].append(t)
        
    def appendAll(self, word1, word2):
        new_word = word1+word2
        temp_arr = []
        idx = 0
        self.dic=None
        for word in self.arr:
            temp_arr.append(word)
            if word not in self.dic:
                self.dic[word] = [idx]
            else: self.dic[word].append(idx)
            idx+=1
            if word == word1:
                temp_arr.append(word2)
                if word2 not in self.dic:
                    self.dic[word2] = [idx]
                else:
                    self.dic[word2].append(idx)
                idx+=1
        self.arr = temp_arr