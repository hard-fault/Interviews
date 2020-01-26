def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0]}
    print "first_match - {}".format(first_match)

    return first_match and isMatch(text[1:], pattern[1:])

text = "abced"
pattern = "abcd"
print isMatch(text,pattern)

