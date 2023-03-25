
# This code defines a generator function "parrot()" that uses the "yield" keyword to allow the function to be paused 
# and resumed. The "while True" loop in the generator function waits for a new value to be sent to it using the "send()"
# method. When a new value is sent, the "yield" keyword is resumed, and the value is assigned to the "message" variable. 
# The "print()" function is then called to print the message with a fixed string.

def parrot():
    while True:
        message = yield
        print("Parrot says: {}".format(message))


# the "parrot()" function is called to create a "generator" object named generator. 
# The "send()" method is used to start the generator, sending it a value of "None" to advance to the first "yield" expression. 
# Then, the "send()" method is used twice more to send the strings "Hello" and "World" to the generator.

if __name__ == "__main__":
    generator = parrot()

    generator.send(None)
    generator.send("Hello")
    generator.send("World")

# Note that the first call to "send()" is necessary to start the generator, and it must always send "None". 
# Also, the generator will loop indefinitely unless it is stopped explicitly or the program is interrupted.