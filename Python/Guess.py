import random

n = random.randint(1, 100)
print("I have an integer [1-100]. Guess my integer")
i = 1
while True:
    g = int(input("Guess number " + str(i) + ": "))
    i += 1
    l = random.random()
    if not (g>=1 and g<=100):
        print("Enter an integer [1-100], stupid.")
        continue
    if g==n:
        break
    if g<n:
        if random.random()>l:
            gl = "greater"
        else:
            gl = "less"
    if g>n:
        if random.random()>l:
            gl = "less"
        else:
            gl = "greater"
    print("""
    You guessed wrong.
    My number is {} than that.
    I have a {}% chance of lying.
    """.format(gl, int(l*100)))
print("Congratulations! You guessed my number.")