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

a = [1728, 288, 144, 72, 12, 10, 6]
number = int(input("input number: "))

if can_sum(a, number):
    result = find_combination(a, number)
    print("found:", result)
else:
    print("oh god (no solve)")
