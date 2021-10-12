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
    """testing"""
    check50.run("./hangman a").stdin("a").stdout("a You guessed it!").exit(0)
    
    @check50.check(compiles)
def test():
    """testing"""
    check50.run("./hangman test").stdin("a")..stdin("a")..stdin("a").stdout("'_ _ _ _ Guess a letter: _ e _ _ Guess a letter: t e _ t Guess a letter: t e _ t Guess a letter: t e s t You guessed it!").exit(0)

