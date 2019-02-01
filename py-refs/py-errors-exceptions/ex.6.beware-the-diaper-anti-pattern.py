def someScaryFunction():
    print("someScaryFunction")


try:
    someScaryFunction()
except:
    print("An error occured. Moving on!")

# A bare except allows you to catch all exceptions in one

# In his book "How To Make Mistakes in Python" [O'Reilly, 2018], Mike Pirnat calls this the diaper pattern, and it is a really, really bad idea. I'll allow him to summarize...
# ...all the precious context for the actual error is being trapped in the diaper, never to see the light of day or the inside of your issue tracker. When the “blowout” exception occurs later on, the stack trace points to the location where the secondary error happened, not to the actual failure inside the try block.
