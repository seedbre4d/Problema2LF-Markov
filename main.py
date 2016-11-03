# Markov algorithm by Iliescu Dragos-Andrei
# TODO: comment the code a bit more


from culori import *

ld = chr(955)  # 955 is the position of λ in the complete ASCII dictionary. chr(955) just produces λ (Unicode req.)
wordlist = []
set_of_rules = []
number_of_rules = 0
v = ''


class Rule:
    '''
    Class for a rule
    It bears the basic set and get functions, nothing special.
    '''

    def __init__(self, dictionary):
        self.v = dictionary
        self.rule_in = ''
        self.rule_out = ''

    def set(self):
        '''
        Syntax is as follows:
        rule_in -> rule_out
        :return: None
        '''
        while True:
            print("In: ", end='')
            self.rule_in = input()
            # chunk to exchange all _ to λ
            while True:
                try:
                    self.rule_in = self.rule_in[:self.rule_in.index("_")] + ld + self.rule_in[self.rule_in.index("_") + 1:]
                except:
                    break
            if is_in_dictionary(self.v, self.rule_in):
                break

            print(error("Rule containing at least one char that is not included withtin dictionary.),"), '\n',
                  warning("Try again."))
        while True:
            print("Out: ", end='')  # to rule
            self.rule_out = input()

            # chunk to exchange all _ to λ
            while True:
                try:
                    self.rule_out = self.rule_out[:self.rule_out.index("_")] + ld + self.rule_out[self.rule_out.index("_") + 1:]
                except:
                    break

            if is_in_dictionary(self.v, self.rule_out):
                break
            print(error("Rule containing at least one char that is not included withtin dictionary.),"), '\n',
                  warning("Try again."))

    def get(self):
        '''
        Just the getter. It's pretty forward
        :return: rule_in -> rule_out
        '''
        return "{} -> {}".format(self.rule_in, self.rule_out)


def is_in_dictionary(v, word):
    '''
    Checks to see if the word is part of the dictionary
    :param v: dictionary
    :param word: word to check
    :return: True or False, regardin the situation
    '''
    for ch in word:
        try:
            v.index(ch)
        except ValueError:  # if we get ValueError from index() it means that
            if ch is ".":  # we either have
                if word.index(ch) == 0:  # a final rule
                    continue
            return False  # or the word is not part of the dictionary
    return True


def is_dictionary(v):
    '''
    Check to see if the given dictionary follows the rules of a dictionary
    :param v: dictionary
    :return: True or False, regardin the situation
    '''
    for ch in v:
        try:
            v[v.index(ch) + 1:].index(ch)  # if from the position of the ch on we find another ch
        except ValueError:  # we don't get a ValueError
            continue  # it means we're ok, and continue the loop
        return False  # otherwise, we're not following the rules of a dictionary.
    return True


def set_rules(rules_number, set_of_rules, v):
    '''
    Function to set multiple rules
    :param rules_number: explicit
    :param set_of_rules: explicit
    :param v: dictionary
    :return: rien
    '''
    for i in range(1, rules_number + 1):
        print(warning("Rule number {}:".format(i)))
        rule = Rule(v)
        rule.set()
        set_of_rules.append(rule)


def get_rules(set_of_rules):
    '''
    Simple function to print rules
    :param set_of_rules: explicit
    :return: rien
    '''
    for rule in set_of_rules:
        print("{}. {}".format(set_of_rules.index(rule), rule.get()))


def apply_rules(set_of_rules, word):
    '''
    Simple function to apply all the rules for a single word
    :param set_of_rules: explicit
    :param word: explicit
    :return: rien
    '''

    print("{}{}".format("\n", warning(word)), end='')  # prints a new line and the word in yellow
    i = 0
    while i < len(set_of_rules):
        try:
            word.index(set_of_rules[i].rule_in)
        except ValueError:  # if we get ValueError it means that rule #i was not applied
            i += 1  # so we increase i and
            continue  # move on

        # this chunk looks a tad complicated, but it's really not:
        # we replace the word with the part of itself before we find the rule_in
        # we add the respective rule_out
        # and then we replace the other of itself after the rule_in
        word = word[:word.index(set_of_rules[i].rule_in)] + set_of_rules[i].rule_out + word[word.index(
            set_of_rules[i].rule_in) + len(set_of_rules[i].rule_in):]

        # chunk to exchange λ to <rien>
        while True:
            try:
                word = word[:word.index(ld)] + "" + word[word.index(ld) + 1:]
            except ValueError:
                break

        print("->{}".format(word), end='')
        if is_final(set_of_rules[i].rule_out):  # if the rule is final, we're finished.
            break
        i = 0  # if we got here, it means that a rule was applied, and so we start over again


def is_final(rule):
    '''
    Checker for the finaal rule
    :param rule: explicit
    :return: True or False, regarding the case
    '''
    try:
        rule.index(".")
    except ValueError:
        return False
    return True


def main_menu():
    '''
    The main menu
    :return: rien
    '''
    while True:
        # main menu shower
        print("{}\n1. Set dictionary\n2. Set rules\n3. Set wordlist\n4. Apply rules for word\n5. Exit\n> ".format(
            warning(
                'Hint! To use λ, just use underscore "_" (without quotation marks). It will automatically be replaced!')),
            end='')

        # option getter
        option = input()
        if not option.isdigit():  # error avoider
            print("{}\nPress {} to try again.".format(error("Wrong choice."), warning("<enter>")))
            input()
            continue

        # if we chose one, this executes
        if int(option) == 1:
            while True:
                print("Dictionary: ", end='')
                v = input()
                if not is_dictionary(v):
                    print("{}\nPress {} to try again.".format(
                        error("Not a valid dictionary: at least one char is repeating."), warning("<enter>")))
                    input()
                    continue

                # chunk to exchange _ to λ
                try:
                    v = v[:v.index("_")] + ld + v[v.index("_") + 1:]
                except:
                    None

                print(v, "\nIs this correct?\n{}\{}".format(correct("y"), error("any other input")))
                verify = (input())
                if verify is 'y' or verify is 'Y':
                    break

        # if we chose two, this executes
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

        # if we chose three, this executes
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
                    # chunk to exchange _ to λ
                    while True:
                        try:
                            wordlist[len(wordlist)-1] = wordlist[len(wordlist)-1][:wordlist[len(wordlist)-1].index("_")] + ld + wordlist[len(wordlist)-1][wordlist[len(wordlist)-1].index("_") + 1:]
                        except ValueError:
                            break
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

        # if we chose four, this executes
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

        # if we chose five, this executes
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
