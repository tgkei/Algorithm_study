from pprint import pprint


class Trie:
    def __init__(self, tree=None):
        self.head = dict()
        self.head['?'] = dict({"length": dict()})

    def add(self, word):
        cur = self.head

        n = len(word)
        if n not in cur['?']["length"]:
            cur['?']["length"][n] = 1
        else:
            cur['?']["length"][n] += 1
        for i in range(n):
            if word[i] not in cur:
                cur[word[i]] = {}
                cur[word[i]]["length"] = {n: 1}
            else:
                if n not in cur[word[i]]["length"]:
                    cur[word[i]]["length"][n] = 1
                else:
                    cur[word[i]]["length"][n] += 1
            cur = cur[word[i]]

    def match(self, query):
        cur = self.head

        n = len(query)
        ret = 0

        for i in range(n):
            if query[i] in cur:
                cur = cur[query[i]]
            elif query[i] == '?':
                if n in cur["length"]:
                    return cur["length"][n]
                else:
                    return 0
            else:
                break

        return ret

    def show(self):
        pprint(self.head)


def solution(words, queries):
    answer = []
    words = list(set(words))

    trie = Trie()
    trie2 = Trie()

    for word in words:
        trie.add(word)
        trie2.add(word[::-1])

    for query in queries:
        if query.startswith('?'):
            answer.append(trie2.match(query[::-1]))
        else:
            answer.append(trie.match(query))

    return answer


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    # words = ["frodo"]
    # queries = ["fro???"]
    # queries = ["fro??", "fr???", "fro???", "pro?"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))
