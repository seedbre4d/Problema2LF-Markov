# Implementarea algoritmului lui Markov



from culori import *



ld = chr(955)  # lambda se afla pe pozitia 955 in codul ASCII in Python 3


class Rule:
    def __init__(self,dictionary):
        self.v=dictionary
        self.rule_in = ""
        self.rule_out = ""

    def set(self):
        while True:
            print("In: ",end='')
            self.rule_in = input()
            if is_in_dictionary(self.v, self.rule_in):
                break
            print("Regula contine cel putin un caracter care nu face parte din dictionarul dat.\nIncearca din nou")
        while True:
            print("Out: ",end='')
            self.rule_out = input()
            if is_in_dictionary(self.v, self.rule_out):
                break
            print("Regula contine cel putin un caracter care nu face parte din dictionarul dat.\nIncearca din nou")

    def get(self):
        return ("{} -> {}".format(self.rule_in, self.rule_out))


def is_in_dictionary(v: str, word: str):
    for ch in word:
        try:
            v.index(ch)
        except ValueError:
            if ch is ".":
                if word.index(ch) == 0:
                    continue
            return False
    return True


def is_dictionary(v: str):
    for ch in v:
        try:
            v[v.index(ch) + 1:].index(ch)
        except ValueError:
            continue
        return False
    return True


def set_rules(rules_number, set_of_rules,v):
    for i in range(1, rules_number + 1):
        print(warning("Rule number {}:" .format(i)))
        rule = Rule(v)
        rule.set()
        set_of_rules.append(rule)


def get_rules(set_of_rules):
    for rule in set_of_rules:
        print("{}. {}".format(set_of_rules.index(rule), rule.get()))


def main_menu():
    while True:
        wordlist=[]
        v=[]
        set_of_rules=[]
        print("1. Set dictionary\n2. Set rules\n3. Set wordlist\n4. Apply rules for word\n5. Exit\n> ", end='')
        option = input()
        if not option.isdigit():
            print("{}Wrong choice.{}\nPress {}<enter>{} to try again." .format(Culoare.red,Culoare.default,\
                  Culoare.yellow,Culoare.default))
            input()
            continue
        if int(option) == 1:
            while True:
                print("Dictionary: ", end='')
                v = input()
                if not is_dictionary(v):
                    print("{}Not a valid dictionary: at least one char is repeating.{}\nPress {}<enter>{} to try again."\
                          .format(Culoare.red,Culoare.default,Culoare.yellow,Culoare.default))
                    input()
                    continue
                print(
                    "Is this correct?\n{}y{}/{}<any other input>{}".format(Culoare.blue, Culoare.default, Culoare.red,
                                                                           Culoare.default))
                verify = (input())
                if verify is 'y' or verify is 'Y':
                    break

        elif int(option) == 2:
            while True:
                print("Number of rules: ", end='')
                rules_number = int(input())
                set_of_rules = []
                set_rules(rules_number, set_of_rules,v)
                print("The rules you have set are the following: ")
                get_rules(set_of_rules)
                print(
                    "Is this correct?\n{}y{}/{}<any other input>{}".format(Culoare.blue, Culoare.default, Culoare.red,
                                                                           Culoare.default))
                verify = (input())
                if verify is 'y' or verify is 'Y':
                    break
        elif int(option) == 3:
            while True:
                if not v:
                    print("{}Error: the dictionary is empty; can not add words{}\nPress {}<enter>{} to return to"\
                          "main menu.".format(Culoare.red,Culoare.default,Culoare.yellow,Culoare.default))
                    input()
                    break
                print("Input wordlist. When done, press {}<enter>{} without typing anything." .format(Culoare.yellow,\
                                                                                                      Culoare.default))
                wordlist = []
                while True:
                    print("Input: ", end='')
                    wordlist.append(input())
                    if wordlist[len(wordlist) - 1] is "":
                        wordlist.pop()
                        break
                    if not is_in_dictionary(v,wordlist[len(wordlist) - 1]):
                        print("{}Eroare: cuvantul tocmai adaugat contine caractere ce nu sunt in dictionar.\n"\
                              "apasa {}<enter>{} pentru a incerca din nou." .format(Culoare.red,Culoare.default,\
                                                                                    Culoare.yellow,Culoare.default))
                        break
                print("Wordlist: ")
                for word in wordlist:
                    print(word)
                print(
                    "Is this correct?\n{}y{}/{}<any other input>{}".format(Culoare.blue, Culoare.default, Culoare.red,
                                                                           Culoare.default))
                verify = (input())
                if verify is 'y' or verify is 'Y':
                    break

        elif int(option) == 4:
            print("soon to be.")
        elif int(option) == 5:
            print("exit now")
        else:
            print("{}Wrong choice.{}\nPress {}<enter>{} to try again." .format(Culoare.red,Culoare.default,Culoare.yellow,Culoare.default))
            input()
        print("")


main_menu()
