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
