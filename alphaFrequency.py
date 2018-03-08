import string
def checkio(text):
    # l = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
    #      'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    #      's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
    #      }
    # atext = text.lower()
    # for a in atext:
    #     if a.isalpha():
    #         l[a] = l.get(a) + 1
    #         # print(l)
    # maxnum = ''
    # count = 0
    # for a in l.keys():
    #     if l.get(a) > count:
    #         maxnum = a;
    #         count = l.get(a)
    # print(maxnum)
    # return maxnum

    ####################################################
    #####大神的写法
    text = text.lower()
    print(string.ascii_lowercase)

    return max(string.ascii_lowercase, key=text.count)




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
