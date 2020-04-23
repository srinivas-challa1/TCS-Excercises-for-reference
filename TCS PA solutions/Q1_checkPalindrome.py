def check_palindrome(strlst):
    palindromes = []
    for string in strlst:
        if(string[::-1].lower() == string.lower()):
            palindromes.append(string)
    return(palindromes)


if __name__ == "__main__":
    count = int(input())
    strlst = []
    for _ in range(count):
        strlst.append(input())
    output = check_palindrome(strlst)
    if(len(output) != 0):
        for palindrome in output:
            print(palindrome)
    else:
        print("No palindrome found!")
