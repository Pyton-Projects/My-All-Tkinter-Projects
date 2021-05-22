
from tkinter import*
import random
import pygame
thing='Rock','Paper','Scissors'
root=Tk()
root.geometry('400x175')
root.minsize(400,175)
root.maxsize(400,175)
root.title('Rock, Paper & Scissors Game!')
USER_choice=StringVar()
USER_choice.set('None')
label=Label(root,text='')
ChoiceS_Label=Label(root,text='')
def result():
	random_thing=(random.choice(thing))
	Selected_thing=(USER_choice.get())
	if Selected_thing==random_thing:
         label.config(text='Tie')

	elif Selected_thing=='Rock' and random_thing=='Scissors':
            label.config(text='You Won!')   
            pygame.mixer.init()
            pygame.mixer.music.load('nioce (1).mp3')
            pygame.mixer.music.play()
	elif Selected_thing=='Scissors' and random_thing=='Paper':	
         label.config(text='You Won!')
         pygame.mixer.init()
         pygame.mixer.music.load('nioce (1).mp3')
         pygame.mixer.music.play()
	elif Selected_thing=='Paper' and random_thing=='Rock':
         label.config(text='You Won!')
         pygame.mixer.init()
         pygame.mixer.music.load('nioce (1).mp3')
         pygame.mixer.music.play()
	else:
         label.config(text='You Lose!')
         pygame.mixer.init()
         pygame.mixer.music.load('bruh.mp3')
         pygame.mixer.music.play()
	slected_choice=(f'Your Choice Is {Selected_thing} And Computer Choice Is {random_thing}')
	ChoiceS_Label.config(text=f'{slected_choice}')
	print(Selected_thing,random_thing)
heading=Label(root,text='Select Your Choice From Down Below')
heading.pack()
Rock=Radiobutton(root,text='Rock',value='Rock',var=USER_choice)
Rock.pack()
Paper=Radiobutton(root,text='Paper',value='Paper',var=USER_choice)
Paper.pack()
Scissors=Radiobutton(root,text='Scissors',value='Scissors',var=USER_choice)
Scissors.pack()
button=Button(root,text='Select!',command=result)
button.pack()
ChoiceS_Label.pack()
label.pack()
mainloop()