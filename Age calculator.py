
# logic:

from datetime import date,datetime
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
root=Tk();track_month_combobox_value_1=IntVar();track_day_combobox_value_1=IntVar();track_month_combobox_value=IntVar();track_day_combobox_value=IntVar()
track_day_combobox_value.set('Day')
track_month_combobox_value.set('Month')
track_month_combobox_value_1.set('Month')
track_day_combobox_value_1.set('Day')
input_data1=StringVar()
input_data=StringVar()
months=(1,2,3,4,5,6,7,8,9,10,11,12);this_variale_has_only_28_days=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28');this_variale_has_only_30_days=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30');this_variale_has_only_31_days=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
root.title('Age Calculator')
root.minsize(400,200)
root.maxsize(400,200)
head=Label(root,text='Age Calculator',font=('Courier',15,'bold'),fg='green4').pack()
Label_=Label(root,text='Date Of Birth:',font=('Courier',12,'bold'),fg='Orange4').place(x=10,y=35)#muic player with lyrics it's my dream
Label_=Label(root,text='Age At The Date Of:',font=('Courier',12,'bold'),fg='Orange4').place(x=190,y=35)#muic player with lyrics it's my dream
def which_day(a):
	if track_month_combobox_value.get()==1:
		day_combobox.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value.get()==2:
		day_combobox.config(values=this_variale_has_only_28_days)
	if track_month_combobox_value.get()==3:
		day_combobox.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value.get()==4:
		day_combobox.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value.get()==5:
		day_combobox.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value.get()==6:
		day_combobox.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value.get()==7:
		day_combobox.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value.get()==8:
		day_combobox.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value.get()==9:
		day_combobox.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value.get()==10:
		day_combobox.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value.get()==11:
		day_combobox.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value.get()==12:
		day_combobox.config(values=this_variale_has_only_31_days)
def which_day_1(b):
	if track_month_combobox_value_1.get()==1:
		m_4.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value_1.get()==2:
		m_4.config(values=this_variale_has_only_28_days)
	if track_month_combobox_value_1.get()==3:
		m_4.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value_1.get()==4:
		m_4.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value_1.get()==5:
		m_4.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value_1.get()==6:
		m_4.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value_1.get()==7:
		m_4.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value_1.get()==8:
		m_4.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value_1.get()==9:
		m_4.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value_1.get()==10:
		m_4.config(values=this_variale_has_only_31_days)
	if track_month_combobox_value_1.get()==11:
		m_4.config(values=this_variale_has_only_30_days)
	if track_month_combobox_value_1.get()==12:
		m_4.config(values=this_variale_has_only_31_days)
def calculate():
	try:
		global to_month
		global from_month
		int_from=int(input_data.get())
		int_from_1=int(input_data1.get())
		birth_date=(date(int_from,track_month_combobox_value_1.get(),int(track_day_combobox_value_1.get())))
		Calculate=(date(int_from_1,track_month_combobox_value.get(),int(track_day_combobox_value.get())))
		brit=(str(birth_date)[0:4:])
		brit_1=(str(Calculate)[0:4:])
		birt_2=(str(birth_date)[5:7:])
		birt_4=(str(Calculate)[5:7:])
		bith89797979=(str(birth_date)[8:])
		bith8979=(str(Calculate)[8:])
		messagebox.showinfo("info",f'{int(brit_1)-int(brit)} Year {int(birt_2)-int(birt_4)} Months {int(bith89797979)-int(bith8979)} Days.')# fix acurracy issue.
	except ValueError:
		messagebox.showerror('Info','Please Enter A Vaild Year Or Month!!!')
month_combobox=Combobox(root,values=months,textvariable=track_month_combobox_value,width=7,state='readonly')
month_combobox.place(x=95,y=65)
info=('Please\n Select\n A\n Month\n Then\n Select\n A\n Day\n')
month_combobox.bind('<<ComboboxSelected>>',which_day)
day_combobox=Combobox(root,textvariable=track_day_combobox_value,width=7,state='readonly',values=info)
day_combobox.place(x=5,y=65)
birth_entry=Entry(root,width=7,font=('Arail',12),textvariable=input_data)
birth_entry.place(x=65,y=110)
year_lab=Label(root,text='Year:-',font=("Arail",15,),fg='purple').place(x=1,y=105)
m_1=Combobox(root,values=months,textvariable=track_month_combobox_value_1,width=7,state='readonly')
m_1.place(x=310,y=65)
m_3=('Please\n Select\n A\n Month\n Then\n Select\n A\n Day\n')
m_1.bind('<<ComboboxSelected>>',which_day_1)
m_4=Combobox(root,textvariable=track_day_combobox_value_1,width=7,state='readonly',values=info)
m_4.place(x=190,y=65)
m_5=Entry(root,width=7,font=('Arail',12),textvariable=input_data1)
m_5.place(x=250,y=110)
m_6=Label(root,text='Year:-',font=("Arail",15,),fg='purple').place(x=190,y=105)
cal=Button(root,text='Calculate Age',command=calculate,background='red1',activebackground='Red1',fg='white',activeforeground='white',borderwidth=6,font=('Arail',12,'bold'))
cal.place(x=130,y=155)
mainloop()
