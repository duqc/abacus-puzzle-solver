def can_sum(a, number):
    dp = [False] * (number + 1)
    dp[0] = True

    for j in range(len(a)):
        for _ in range(4):
            for i in range(number, a[j] - 1, -1):
                if dp[i - a[j]]:
                    dp[i] = True
    
    return dp[number]

def find_combination(a, number):
    dp = [False] * (number + 1)
    dp[0] = True
    combination = [0] * len(a)

    for j in range(len(a)):
        for _ in range(4):
            for i in range(number, a[j] - 1, -1):
                if dp[i - a[j]]:
                    dp[i] = True
                    if dp[number]:
                        while number > 0:
                            for j in range(len(a)):
                                count = 0
                                while count < 4 and number >= a[j] and dp[number - a[j]]:
                                    combination[j] += 1
                                    number -= a[j]
                                    count += 1
                                    break
                        return combination
    
    return None

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
YO PLEASE READ THIS LOL

to get proper results you have to change the beads list to be whats actually in the game. for example if you wanted to solve the first one you
would change the list to be [1728,144,72,12,6]. ok good luck

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""



beads = [52115389,1728, 288, 144, 72, 12, 10, 6]
number = int(input("input number: "))

if number > 52115389:
    print("yo if ur tryna do the funny gears puzzle and not something else its just [1, 0, 0, 0, 0, 0, 1, 0] the solver takes a god awful time to solve anything larger then 52115389 cause i cant code")
if can_sum(beads, number):
    result = find_combination(beads, number)
    print("found:", result)
else:
    print("oh god (no solve)")
