for _ in range(int(input())):
    word = input()
    guess = input()
    M = ""
    for i in range(len(word)):
        if word[i] == guess[i]:
            M += "G"
        else:
            M += "B"
    print(M)