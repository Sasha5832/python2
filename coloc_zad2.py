def przepisz(a):
    clean_string = "".join(c for c in a if c.isalnum())
    reversed_substring = clean_string[::-4]
    print(reversed_substring)


a = "abcdifghijklmnopqrstuwdxyz"
przepisz(a)
