"""
There are T test cases. The first line consist of an integer T (1≤T≤500).

T lines follow:

The first line contains the number of words in the sentence, N.
The second line contains N words, containing only uppercase letters (A-Z).
It is guaranteed that the sum of N across all T test cases is at most 10^5.

For each of the test cases, in the i-th line, output YES if the i-th sentence is a grammatically correct sentence, and output NO otherwise.

WE → “DONT”, “KNOW”
THEY → “DONT”, “KNOW”
DONT → “KNOW”
KNOW → “WE”, “THEY”, “THAT”
THAT → “WE”, “THEY”
"""

from operator import truth

test_cases = int(input())

print("Number of test cases: " + str(test_cases))

for test_case in range(0, test_cases):
    global truth_value

    wordsCount = int(input())

    print("Number of words in test case " + str(test_case) + " is " + str(wordsCount))

    sentence = input().split(" ")

    previousWord = ""

    truth_value = True
    
    for i in range(0, wordsCount):

        print("Current word is "+ str(sentence[i]))
        
        if previousWord != "":
            if previousWord != "WE" and previousWord != "DONT" and previousWord != "KNOW" and previousWord != "THAT" and previousWord != "THEY":
                truth_value = False

            else:
                match previousWord:
                    case "WE":
                        if sentence[i] != "DONT" and sentence[i] != "KNOW":
                            truth_value = False
                            break
                        else: 
                            pass
                    case "THEY":
                        if sentence[i] != "DONT" and sentence[i] != "KNOW":
                            truth_value = False
                            break
                        else:
                            pass
                    case "DONT":
                        if sentence[i] != "KNOW":
                            truth_value = False
                            break
                        else:
                            pass
                    case "KNOW":
                        if sentence[i] == "WE":
                            pass
                        elif sentence[i] != "THEY" and sentence[i] != "THAT":
                            truth_value = False
                            break
                        else:
                            pass
                    case "THAT":
                        if sentence[i] != "WE" and sentence[i] != "THEY":
                            truth_value = False
                            break
                        else:
                            pass
                    case _:
                        truth_value = False
                        break

        print(truth_value)
        
        previousWord = sentence[i]

        f = open("grammar.txt", "a")



    if truth_value != False:
        f.write("YES\n")
        f.close()
        print("YES, the sentence is grammatically correct")
    else:
        f.write("NO\n")
        f.close()
        print("NO")
        

        
