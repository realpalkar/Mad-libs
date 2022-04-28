from tkinter import *

root = Tk()
root.geometry = ('300x300')
root.title('Mad Libs Generator')
Label(root, text= 'Mad libs generator', font='arial 20 bold').pack()
Label (root, text= 'Click any one', font= 'arial 15 bold').place(x=40, y=80)

def madlib1():
    place = input('enter name of place in mumbai: ')
    food = input('enter your fav street food in mumbai: ')
    height = input('enter your height: ')
    animal =  input('name your fav animal: ')
    print('we were always rich.' + ' That summer, we went for vacation to ' + place + '.' + ' We eat food at Taj.' + ' We ordered ' + food + '.' + ' We tip ' + height + ' rs to waiter' + '.' + ' Paiso ki kami nahi hai.' + ' City has beautiful people and we look like ' + animal + ' in front of them.')

def madlib2():
    actor = input('name of actor/actress: ')
    animal = input('name of animal: ')
    weight = input('enter your weight: ')
    shape = input('enter your fav shape: ')
    print('I\'m big fan of ' + actor + '. But I look lika a ' + animal + '. To look like ' + actor + ' ,I put ' + weight + ' kg' + ' of make up on my face.' + ' But result is terrible.' + ' My hips are quite ' + shape + '. Everybody likes them.')

Button(root, text= 'The Vacation', font='arial 15', command= madlib1, bg='ghost white').place(x=60, y= 120)
Button(root, text= 'My hero', font= 'arial 15', command= madlib2,  bg='ghost white').place(x=70, y= 180)

root.mainloop()