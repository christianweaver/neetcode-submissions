class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        
        d['*'] = '-1'


    def search(self, word: str) -> bool:
        d = self.trie

        def rec_search(wordd, dictt):
            if wordd == "":
                return '*' in dictt

            c = wordd[0]

            if c == '.':
                for key in dictt:
                    if rec_search(wordd[1:], dictt[key]):
                        return True
                return False
            else:
                if c in dictt:
                    return rec_search(wordd[1:], dictt[c])
                else:
                    return False

        return rec_search(word, d)