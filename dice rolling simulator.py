from tkinter import*
from ttkthemes import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
import random # a meme idea--> kids uses-ide legend uses-notepad
root=Tk() # create a normal dice.
a=10
dice_3='\u2682' # CREATE A CHANCES LABEL..
dice_2='\u2681'
dice_1='\u2680'# bug when we buy dices
dice_4='\u2683'
dice_5='\u2684'
dice_6='\u2685'
this_dice_has_MORE_four='\u2683','\u2683','\u2683','\u2683','\u2680','\u2681','\u2682','\u2684','\u2685'
random_=random.choice(this_dice_has_MORE_four)
root.geometry('900x700')
root.maxsize(900,700)
dice_l_3_1 = Label(root, font=('helvetica', 260))
root.minsize(900,700)
root.title('Dice Simulator')
dice_l=Label(root,font=("helvetica",260)) #
dice_l_2=Label(root,font=('helvetica',260))
dice_l_4=Label(root,font=('helvetica',45))
or_label=Label(root,font=('helvetica',45))
money=2000
text_mon_dat=StringVar()
text_mon_dat.set(f'Balance-{money}$')
rs_Label=Label(root,text=f'Balance-{money}$',font=('Courier',30),textvariable=text_mon_dat)
rs_Label.place(x=1,y=1)
about_pro=Button(root,text='\u24D8',font=(5),border=0)
about_pro.place(x=600-300,y=100)
about_pro_max=Button(root,text='\u24D8',border=0,font=(5))
about_pro_max.place(x=1,y=100)
about_pro_max_ultra=Button(root,text='\u24D8',border=0,font=(5))
about_pro_max_ultra.place(x=600,y=100)
def about_pro_():
	from tkinter import messagebox
	messagebox.showinfo('Message','This Dice Has More Chances To Get Four. And Your 2 Times Point Will Increase And Also Your Money Will Increase 2 Times')
def about_pro_max_():
	from tkinter import messagebox
	messagebox.showinfo('Message','This Dice Has More Chances To Get Five. And Your 4 Times Point Will Increase')
def about_pro_max_ultra_():

	from tkinter import messagebox
	messagebox.showinfo('Message','This Dice Has More Chances To Get Six. And Your 6 Times Point Will Increase')
about_pro.config(command=about_pro_)
about_pro_max.config(command=about_pro_max_)
about_pro_max_ultra.config(command=about_pro_max_ultra_)
price_Label_5=Label(root,font=('Courier',20,'bold'))
price_Label_6=Label(root,font=('Courier',20,'bold'))
price_Label_4=Label(root,font=('Courier',20,'bold'))
chances1=6

def chances():
	global chances_label
	global val
	global chances1
	global money
	text_mon_dat.set(f'Balance-{money}$')

	dat_two.set(f'Balance-{money}$')

	val=StringVar()
	val.set(f'Chances Left:{chances1}')
	chances_label=Label(top_level,text=f'Chances Left:{chances1}',textvariable=val,font=('Courier',20))
	chances_label.place(x=665,y=40)
	if chances1==0:
		dat_two.set(f'Balance-{money}$')
		text_mon_dat.set(f'Balance-{money}$')

		ques_1=messagebox.askquestion('Info','Chances Finised!!!! Do You Want To Buy More Chances?')
		# show shop if answer is yes else:
		if ques_1=='yes':
			# show shop
			store_to_buy_more_chances()
		else:

			messagebox.showinfo('(:',f'Your Luck Scored:{point_dat.get()[::-1][0:2:][::-1]}')
			Start_The_Roll.config(state=DISABLED)
			chances1=6

			
			root.deiconify()
			top_level.destroy()

			

		# show spinbox to buy chances
  
def main_roll():
	global random_
	this_dice_has_MORE_four='\u2683','\u2683','\u2683','\u2683','\u2680','\u2681','\u2682','\u2684','\u2685'
	random_=random.choice(this_dice_has_MORE_four)
	dice_l_3.config(text=f'{random.choice(random_)}')
	print(random_)
	global point
	global chances1
	global money
	global money
	dat_two.set(f'Balance-{money}$')

	if (random_)=='\u2680':
		point+=2 # add money also
		chances1-=1
		point_dat.set(f'Point:{point}')
		money+=10
		
		print(money)
		dat_two.set(f'Balance-{money}$')

		text_mon_dat.set(f'Balance-{money}$')
		chances()



	elif (random_)=='\u2681':
		point+=4
		chances1-=1		
		point_dat.set(f'Point:{point}')
		money+=40
		print(money)
		dat_two.set(f'Balance-{money}$')

		text_mon_dat.set(f'Balance-{money}$')
		chances()

	elif (random_)=='\u2682':
		point+=6
		chances1-=1
		point_dat.set(f'Point:{point}')
		money+=60

		print(money)
		dat_two.set(f'Balance-{money}$')

		text_mon_dat.set(f'Balance-{money}$')
		chances()

	elif (random_)=='\u2683':
		point+=8
		chances1-=1
		point_dat.set(f'Point:{point}')
		money+=80
		print(money)
		dat_two.set(f'Balance-{money}$')
		text_mon_dat.set(f'Balance-{money}$')
		chances()

	if (random_)=='\u2684':
		point+=10
		chances1-=1
		point_dat.set(f'Point:{point}')
		money+=100
		print(money)
		dat_two.set(f'Balance-{money}$')
		text_mon_dat.set(f'Balance-{money}$')
		chances()

	elif (random_)=='\u2685':
		point+=12
		chances1-=1
		point_dat.set(f'Point:{point}')
		money+=120
		print(money)
		dat_two.set(f'Balance-{money}$')
		text_mon_dat.set(f'Balance-{money}$')
		chances()

	else:
		dat_two.set(f'Balance-{money}$')
		text_mon_dat.set(f'Balance-{money}$')

	dat_two.set(f'Balance-{money}$')


# 	heiiii=open('score.py','w')
# 	dat=heiiii.write(f'''points=[{point},{point}].sort()
# print(points)''')
# 	# create hight socre option

# 	print(open('score.py','r').read())
# 	dat_two.set(f'Balance-{money}$')
def store_to_buy_more_chances():
	# tommrow code shop
	# spinbox to buy how many
	Strore=ThemedTk(themebg=True)
	Strore.set_theme('arc')
	indie=tkk.Label(root,text='How Many Chances? :')
	head=ttk.Label(Strore,text='Store',font=('Courier',30,'bold'))
	number_of_chaces=ttk.Spinbox(Strore,from_=0,to=24,width=3,font=Font(family='times',size=15))
	head.pack()
	indie.pack(  )
	number_of_chaces['state']='readonly'
	number_of_chaces.pack()




def main_pro():
	root.iconify()
	global  dice_l_3
	global Point
	global point_dat
	global point
	global top_level
	global Start_The_Roll
	global dat_two
	top_level=Toplevel()
	dice_l_3=Label(top_level,text='\u2683',font=('helvetica',260))
	point=1
	point_dat=StringVar()
	dice_l_3.place(x=300, y=1)
	top_level.maxsize(900,450)
	top_level.minsize(900,450)
	top_level.title('Dice Simulator')
	Start_The_Roll=Button(top_level,text='Roll The Dice!!',command=main_roll)
	dat_two=StringVar()
	rs_Label=Label(top_level,text=f'Balance-{money}$',font=('Courier',20),textvariable=dat_two)
	dat_two.set(f'Balance-{money}$')
	rs_Label.place(x=1,y=1)
	Point=Label(top_level,text=f'Point:{point}',font=('Courier',20),textvariable=point_dat)
	point_dat.set(f'Point: {point}')
	Point.place(x=750,y=1)
	Start_The_Roll.place(x=380,y=310)
	dat_two.set(f'Balance-{money}$')
	text_mon_dat.set(f'Balance-{money}$')

def minus_for_prodice():
	global money
	if money>=700:
		from tkinter import messagebox
		money-=700
		rs_Label.config(text=f'Balance:{money}$')
		messagebox.showinfo('Info','Loading Main Scene..')
		main_pro()
	else:
		radio_6_get.set(0)
		from tkinter import messagebox
		messagebox.showinfo('Info',"You Don't have enough money!")
def minus_for_promaxdice():
	if money>=999:

		global money_
		money_=money-999
		print(money_)
		rs_Label.config(text=f'Balance-{money_}$')
		from tkinter import messagebox
		messagebox.showinfo('Info','Loading Main Scene..')
	else:
		radio_6_get.set(0)
		from tkinter import messagebox
		messagebox.showinfo('Info',"You Don't have enough money!")
def minus_for_ultrapromaxdice():
	if money>=2000:

		global money_Bts
		money_Bts=money-1999
		print(money_Bts)
		rs_Label.config(text=f'Balance-{money_}$')
		from tkinter import messagebox
		messagebox.showinfo('Info','Loading Main Scene..')
	else:
		radio_6_get.set(0)
		from tkinter import messagebox
		messagebox.showinfo('Info','''You Don't have enough money!''')
def get_value():
	if radio_6_get.get()==0:
		from tkinter import messagebox
		messagebox.showinfo('????','PLease Buy One!')
	elif radio_6_get.get()==4:
		minus_for_prodice()
	elif radio_6_get.get()==5:
		minus_for_promaxdice()
	elif radio_6_get.get()==6:
		minus_for_ultrapromaxdice()
def roll_dice():
	global radio_6_get
	global radio_6
	global radio_5
	global radio_4
	radio_6_get=IntVar()
	radio_6=Radiobutton(root,text='Ultra-Pro-Max-Dice',font=('helvetica',15),variable=radio_6_get,value=6)
	radio_5=Radiobutton(root,text='Pro-Dice',font=('helvetica',15),variable=radio_6_get,value=4)
	radio_4=Radiobutton(root,text='Pro-Max-Dice',font=('helvetica',15),variable=radio_6_get,value=5)
	dice_6='\u2685'
	dice_5='\u2684'
	dice_4='\u2683'
	price_6=2000
	price_5=999
	price_4=700
	price_Label_5.config(text=f'''Price-{price_5}$''')
	price_Label_5.place(y=300+25-5,x=40)
	price_Label_4.config(text=f'''Price-{price_4}$''')
	price_Label_4.place(y=300+25-5,x=350)
	price_Label_6.config(text=f'Price-{price_6}$')
	price_Label_6.place(y=300+25-5,x=660)
	dice_l.config(text=f'{dice_6}')
	dice_l_2.config(text=f'{dice_5}')
	dice_l_3_1.config(text=f'{dice_4}')
	dice_l_2.place(y=1)
	dice_l.place(x=600,y=1)
	radio_6.place(x=639,y=375)
	radio_5.place(x=350,y=375)
	radio_4.place(x=50,y=375)
	dice_l_3_1.place(x=300,y=1)
b1=Button(root,text='Buy This One And Go!',command=get_value)
roll_dice()
b1.place(x=345,y=425)
root.mainloop()
