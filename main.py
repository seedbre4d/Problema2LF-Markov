# Implementarea algoritmului lui Markov
# Working: algorithm itself
# TODO: implement lambda
# TODO: organize and unify
# TODO: comment code
# ce jeg de materie

from culori import *

ld = chr(955) # 955 is the position of λ in the complete ASCII dictionary. chr(955) just produces λ (Unicode req.)
wordlist = []
set_of_rules = []
number_of_rules = 0
v = ''


class Rule:
    def __init__(self, dictionary):
        self.v = dictionary
        self.rule_in = ''
        self.rule_out = ''

    def set(self):
        while True:
            print("In: ", end='')
            self.rule_in = input()
            if is_in_dictionary(self.v, self.rule_in):
                break
            print(error("Rule containing at least one char that is not included withtin dictionary.),"),'\n',warning("Try again."))
        while True:
            print("Out: ", end='')
            self.rule_out = input()
            if is_in_dictionary(self.v, self.rule_out):
                break
            print(error("Rule containing at least one char that is not included withtin dictionary.),"), '\n',warning("Try again."))

    def get(self):
        return "{} -> {}".format(self.rule_in, self.rule_out)


def is_in_dictionary(v, word):
    for ch in word:
        try:
            v.index(ch)
        except ValueError:
            if ch is ".":
                if word.index(ch) == 0:
                    continue
            return False
    return True


def is_dictionary(v):
    for ch in v:
        try:
            v[v.index(ch) + 1:].index(ch)
        except ValueError:
            continue
        return False
    return True


def set_rules(rules_number, set_of_rules, v):
    for i in range(1, rules_number + 1):
        print(warning("Rule number {}:".format(i)))
        rule = Rule(v)
        rule.set()
        set_of_rules.append(rule)


def get_rules(set_of_rules):
    for rule in set_of_rules:
        print("{}. {}".format(set_of_rules.index(rule), rule.get()))


def apply_rules(set_of_rules, word):
    print("{}{}".format("\n", warning(word)), end='')
    i = 0
    while i < len(set_of_rules):
        try:
            word.index(set_of_rules[i].rule_in)
        except ValueError:
            i += 1
            continue
        word = word[:word.index(set_of_rules[i].rule_in)] + set_of_rules[i].rule_out + word[word.index(
            set_of_rules[i].rule_in) + len(set_of_rules[i].rule_in):]
        print("->{}".format(word), end='')
        if is_final(set_of_rules[i].rule_out):
            print("{} is final".format(set_of_rules[i].rule_out))
            break
        i = 0


def is_final(rule):
    try:
        rule.index(".")
    except ValueError:
        return False
    return True


def main_menu():
    while True:
        print("{}\n1. Set dictionary\n2. Set rules\n3. Set wordlist\n4. Apply rules for word\n5. Exit\n> " .format(warning('Hint! To use λ, just press underscore "_" (without quotation marks). It will automatically be replaced!')), end='')
        option = input()
        if not option.isdigit():
            print("{}\nPress {} to try again.".format(error("Wrong choice."), warning("<enter>")))
            input()
            continue
        if int(option) == 1:
            while True:
                print("Dictionary: ", end='')
                v = input()
                if not is_dictionary(v):
                    print("{}\nPress {} to try again.".format(
                        error("Not a valid dictionary: at least one char is repeating."), warning("<enter>")))
                    input()
                    continue
                print(v,"\nIs this correct?\n{}\{}" .format(correct("y"),error("any other input")))
                verify = (input())
                if verify is 'y' or verify is 'Y':
                    break

        elif int(option) == 2:
            try:
                v
            except:
                print(error("Dictionary is empty."), "Press {} to go back to main.".format(warning("<any key>")))
                input()
                main_menu()
            while True:
                print("Dictionary: ", v)
                print("Number of rules: ", end='')
                try:
                    rules_number = int(input())
                except ValueError:
                    print("{}Hit {} to try again.".format(error("Insert a valid number of rules."), warning("<enter>")))
                    input()
                    continue

                set_of_rules = []
                set_rules(rules_number, set_of_rules, v)
                print("The rules you have set are the following: ")
                get_rules(set_of_rules)
                print(
                    "Is this correct?\n{}\{}".format(correct("y"), warning("any other input")))
                verify = (input())
                if verify is 'y' or verify is 'Y':
                    break
        elif int(option) == 3:
            while True:
                try:
                    v
                except:
                    print(error("Dictionary is empty."), "Press {} to go back to main.".format(warning("<any key>")))
                    input()
                    main_menu()
                print("Input wordlist. When done, press {} without typing anything.".format(warning("enter")))
                wordlist = []
                while True:
                    print("Input: ", end='')
                    wordlist.append(input())
                    if wordlist[len(wordlist) - 1] is "":
                        wordlist.pop()
                        break
                    if not is_in_dictionary(v, wordlist[len(wordlist) - 1]):
                        print("{}. {}".format(error(
                            "Error: the word you just added has at least one char that's not included in the dictionary"),
                            warning("Try again.")))
                        wordlist.pop()
                print("Wordlist: ")
                for word in wordlist:
                    print(word)
                print("Is this correct?\n{}\{}".format(correct("y"), error("any other input")))
                verify = (input())
                if verify is 'y' or verify is 'Y':
                    break

        elif int(option) == 4:
            try:
                wordlist
            except:
                print(error("Wordlist is empty."), "Press {} to go back to main.".format(warning("<any key>")))
                input()
                main_menu()
            try:
                set_of_rules
            except:
                print(error("No rules set."), "Press {} to go back to main.".format(warning("<any key>")))
                input()
                main_menu()
            for word in wordlist:
                apply_rules(set_of_rules, word)
        elif int(option) == 5:
            print("Are you sure you want to exit?\n{}\{}".format(correct("y"), error("any other key")))
            if (input() == "y"):
                print("Exiting...")
                exit()
        else:
            print("{}\nPress {} to try again.".format(error("Wrong chioce."), warning("<enter>")))
            input()
        print("")

main_menu()
