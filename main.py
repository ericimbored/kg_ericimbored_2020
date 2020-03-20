import sys

def AreIso(string1, string2):
    m = {} # mapping of each character in String1 to String2
    r = {} # mapping of each character in String2 to String1
    for i, c in enumerate(string1):
        if c in m:
            if string2[i] != m[c]:
                return False
        else:
            m[c] = string2[i]
        if string2[i] in r:
            if c != r[string2[i]]:
                return False
        else:
            r[string2[i]] = c
    return True

print(AreIso(sys.argv[1], sys.argv[2]))
