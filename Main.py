import tkinter
import math
import tkinter.messagebox
import random

root = tkinter.Tk()
root.minisize(350, 260)
root.title('Guess the number game')

number = random.randint(1,20)

def say_hello():
    print('hello,world!')

def send_low():
    tkinter.messagebox.showinfo("messagebox", "Your guess is too low.")

def check_num():
    global number
    guess = text_guess.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("height", "Your guess is too high.")
    if guess < number:
        tkinter.messagebox.showinfo("low", "Your guess is too low")
    if guess == number:
        tkinter.messagebox.showinfo("good", "Good job")
        number = random.randint(1, 20)

def btn_confirm():
    myName = text_name.get()
    tkinter.messagebox.showinfo("name", 'Well,' + myName + ',I am thinking of a number between 1 and 20.')

