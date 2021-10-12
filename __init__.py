import check50
import check50.c

@check50.check()
def exists():
    """hangman.c exists"""
    check50.exists("hangman.c")
    
@check50.check(exists)
def compiles():
    """hangman.c compiles"""
    check50.c.compile("hangman.c", lcs50=True)

    hangman = open("hangman.c").read()
    header = open("hangman.h").read()
    
    with open("hangman_file.c", "w") as f:
        f.write(hangman)
        f.write("\n")
        f.write(header)
    check50.c.compile("hangman_file.c", lcs50=True)
