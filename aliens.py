"""
There are T test cases. The first line of the input contains a single integer T (1≤T≤20). Then, T test cases follow.

For each test case:

The first line contains a single integer n (1≤n≤10000).

The second line contains a1a2…an, a string of length n consisting only of the letters T and F.

The third line contains b1b2…bn, a string of length n consisting only of the letters T and F.

It is guaranteed that the sum of n across all T test cases is at most 65000.

For each test case, if there is a valid permutation p, output YES on a line, otherwise, print NO on a line. Print them in the order of the test cases.
"""

test_cases = int(input())

print("Number of test cases: " + str(test_cases))

for test_case in range(0, test_cases):
    aliensCount = int(input())

    print("Number of aliens in test case " + str(test_case) + " is " + str(aliensCount))

    alienIdentitiesArray = list(input())

    print(alienIdentitiesArray)

    statementsArray = list(input())

    print(statementsArray)
    
    permutation = []

    for number in range(0, aliensCount):
        permutation.append(number)

    print("First permutation: " + str(permutation))
    
    
    for n in range(0, aliensCount):
        identity = alienIdentitiesArray[n]
        statement = statementsArray[n]
        accusedIndex = permutation[n]
        accusedAlien = alienIdentitiesArray[accusedIndex]

        print(statement)

        match identity:
            case "F":
                if statement == accusedAlien:
                    break



