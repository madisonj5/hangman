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

@check50.check(compiles)
def test():
    """testing a"""
    check50.run("./hangman a").stdin("a").stdout("a You guessed it!").exit(0)
    
@check50.check(compiles)
def newTest():
    """testing test"""
    check50.run("./hangman test").stdin("e").stdin("t").stdin("w").stdin("s").stdout("t e s t You guessed it!").exit(0)

