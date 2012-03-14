"""
fortune_teller.py
===
1. Create a list of fortunes: 'you will write a program', 'you have a lot of tabs in your future', 'boo!' and store it in a variable called fortunes
2. Use random to print out a random fortune when you run the program
3. Run the program several times

Expected Output:

$ python fortune_teller.py 
boo!
$ python fortune_teller.py 
you have a lot of tabs in your future
$ python fortune_teller.py 
you have a lot of tabs in your future
"""
import random

fortunes = ["he who sleeps with itchy ass wakes up with smelly fingers" , "When you squeeze an orange, orange juice comes out - because that's what's inside." , "You will live a long life and eat many fortune cookies."]
index = random.randint(0,2)
print "%s, %s" % (index,fortunes[index])