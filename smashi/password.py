import passgen

def generate(length=12, punctuation=False, digits=True, letters=True, case='both'):
    return passgen.passgen(length, punctuation, digits, letters, case)
