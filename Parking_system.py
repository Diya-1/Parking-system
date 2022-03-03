from multiprocessing.connection import answer_challenge
from tkinter import *
from tkinter import messagebox
from click import command
from matplotlib.pyplot import grid
import mysql.connector 
import time
from datetime import date

global conn,cursor
conn = mysql.connector.connect(
    host='localhost', database='parking_system', user='root', password='password',auth_plugin = 'mysql_native_password',)
cursor = conn.cursor()
def ins_rec(): 
    sql = 'insert into parking_type(name,price) values("{}",{});'.format(name.get(),price.get())
    cursor.execute(sql)
    cursor.execute('select max(id) from parking_type')
    no = cursor.fetchone()
    messagebox.showinfo("ADDED",' New Parking Type added....\n\nNew Parking Type ID is : {} \n\n\n'.format(no[0]))
    
def aptr_back():
    aptr.pack_forget()
    menu.pack()
def add_parking_type_record():
    menu.pack_forget()
    global name,price,aptr
    name=StringVar()
    price=StringVar()
    aptr=Frame(Diya)
    aptr.pack()
    Label(aptr,text='Enter Parking Type( 1. Two wheelar 2. Four Wheeler ) : ',font = "Algerian 20 ").grid(row=0,column=0)
    Entry(aptr,textvariable=name).grid(row=0,column=1)
    Label(aptr,text='Enter Parking Price per day : ',font = "Algerian 20 ").grid(row=1,column=0)
    Entry(aptr,textvariable=price).grid(row=1,column=1)
    Button(aptr,text="Back",command=aptr_back).grid(row=2,column=0)
    Button(aptr,text="Submit",command=ins_rec).grid(row=2,column=1)

def adding_slots():
    sql = 'insert into parking_space(type_id,status) values \
            ("{}","{}");'.format(parking_type_id.get(),status.get()) 
    cursor.execute(sql)
    cursor.execute('select max(id) from parking_space;')
    no = cursor.fetchone()
    messagebox.showinfo("ADDED",'New Parking Space Record added....\n\nYour Parking ID is : {} \n\n\n'.format(no[0]))

def apsr_back():
    apsr.pack_forget()
    menu.pack()

def add_parking_slot_record():
    menu.pack_forget()
    global parking_type_id,status,apsr
    parking_type_id = StringVar()
    parking_type_id.set('1')
    status = StringVar()
    status.set('Open')
    apsr=Frame(Diya)
    apsr.pack()
    Label(apsr,text='Enter Parking Type( 1. Two wheelar 2.Four Wheeler ) :').grid(row=0,column=0)
    Radiobutton(apsr,text = "Two Wheeler",font = "Algerian 20 ",variable=parking_type_id,value='1').grid(row=0,column=1)
    Radiobutton(apsr,text = "Four Wheeler",font = "Algerian 20 ",variable=parking_type_id,value='2').grid(row=0,column=2)
    Button(apsr,text="Back",command=apsr_back).grid(row=2,column=0)
    Button(apsr,text='Submit',command=adding_slots).grid(row=2,column=1)

def adding_vehicle():
    entry_date = date.today()
    sql = 'insert into transaction(vehicle_id,parking_id,entry_date) values \
           ("{}","{}","{}");'.format(vehicle_id.get(),parking_id.get(),entry_date)
    cursor.execute(sql)
    cursor.execute('update parking_space set status ="full" where id ={}'.format(parking_id.get()))
    messagebox.showinfo("ADDED",' Record added successfully.................')

def anv_back():
    anv.pack_forget()
    menu.pack()

def add_new_vehicle():
    menu.pack_forget()
    global vehicle_id,parking_id,anv
    anv=Frame(Diya)
    vehicle_id = StringVar()
    parking_id = StringVar()
    anv.pack()
    Label(anv,text = "Vehicle Login Screen",font = "Algerian 30 ").grid(row=0,column=0)   
    Label(anv,text='Enter Vehicle Number :',font = "Algerian 20 " ).grid(row=1,column=0)
    Entry(anv,textvariable=vehicle_id).grid(row=1,column=1)
    Label(anv,text='Enter parking ID :',font = "Algerian 20 ").grid(row=2,column=0)
    Entry(anv,textvariable=parking_id).grid(row=2,column=1)
    Button(anv,text="Back",command=anv_back).grid(row=3,column=0)
    Button(anv,text="Submit",command=adding_vehicle).grid(row=3,column=1)

def rmv():
    exit_date = date.today()
    sql = 'select parking_id,price,entry_date from transaction tr,parking_space ps, parking_type pt \
           where tr.parking_id = ps.id and ps.type_id = pt.id and \
           vehicle_id ="'+vehicle_id.get()+'" and exit_date is NULL;'
    cursor.execute(sql)
    record = cursor.fetchone()
    days = (exit_date-record[2]).days 
    if days ==0:
        days = days+1
    amount = record[1]*days
    messagebox.showinfo('Logout Details ','Parking ID : {}\n\nVehicle ID : {}\n\nParking Date : {}\n\nCurrent Date : {}\n\nAmount Payable : {}'.format(record[0],vehicle_id.get(),record[2],exit_date,amount))
    sql1 = 'update transaction set exit_date ="{}" , amount ={} where vehicle_id ="{}" \
            and exit_date is NULL;'.format(exit_date,amount, vehicle_id.get())
    sql2 =  'update parking_space set status ="open" where id = {}'.format(record[0])
    cursor.execute(sql1)
    cursor.execute(sql2)

def anr_back():
    anr.pack_forget()
    menu.pack()

def remove_vehicle():
    menu.pack_forget()
    global vehicle_id,anr 
    anr=Frame(Diya)
    vehicle_id=StringVar()
    anr.pack()
    Label(anr,text = "Vehicle Logout Screen",font = "Algerian 30 ").grid(row=0,column=0)
    Label(anr,text='Enter vehicle No :',font = "Algerian 20 ").grid(row=1,column=0)
    Entry(anr,textvariable=vehicle_id).grid(row=1,column=1)
    Button(anr,text="Back",command=anr_back).grid(row=2,column=0)
    Button(anr,text="Remove",command=rmv).grid(row=2,column=1)
    

def show():
    if choice.get() in('1'):
        sql = 'select ps.id,name,price, status \
          from parking_space ps , parking_type pt where ps.id = pt.id AND ps.id ={}'.format(value.get())
    else:
        sql = 'select id,vehicle_id,parking_id,entry_date from transaction where exit_date is NULL;'

    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
    s=Tk()
    for row in results:
        Label(s,text='\n').pack()
        Label(s,text=row).pack()
    s.mainloop()
    if records < 1:
        messagebox.showerror('Record not found ')

def se_back():
    se.pack_forget()

def set_feild():
    field = ''
    global value,se
    se=Frame(Diya)
    value=StringVar()
    if choice.get() == '1':
        field = 'id'
    elif choice.get() == '2':
        field = 'vehicle No'
    se.pack()
    Label(se,text='Enter value to search :',font = "Algerian 20 ").grid(row=0,column=1)
    Entry(se,textvariable=value).grid(row=1,column=1)
    Button(se,text="Back",command=se_back).grid(row=2,column=0)
    Button(se,text="Submit",command=show).grid(row=2,column=2)

def sh_back():
    sh.pack_forget()
    menu.pack()

def search_menu():
    menu.pack_forget()
    global choice,sh
    sh= Frame(Diya)
    choice = StringVar()
    choice.set('1')
    sh.pack()
    Label(sh,text=' S E A R C H  P A R K I N G  M E N U ',font = "Algerian 30 ").grid(row =0,column=1)
    Radiobutton(sh,text='1.  Parking ID ',font = "Algerian 20 ",variable=choice,value='1').grid(row =1,column=1)
    Radiobutton(sh,text='2.  Vehicle Parked ',font = "Algerian 20 ",variable=choice,value='2').grid(row =2,column=1)
    Button(sh,text="Back",command=sh_back).grid(row =4,column=0)
    Button(sh,text="Submit",command=set_feild).grid(row =4,column=2)


def parking_status(status):
       
    sql ="select * from parking_space where status ='{}'".format(status)
    cursor.execute(sql)
    records = cursor.fetchall()
    st = Tk()
    for row in records:
       Label(st,text=row).pack()
    st.mainloop()

def vehicle_status_report():
    global vs 
    vs = Frame(Diya)
    vs.pack()
    # Label(vs,text= 'Vehicle Status - Currently Parked',font="Algerian 30").grid(row=0,column=0)
    sql='select * from transaction where exit_date is NULL;'
    cursor.execute(sql)
    records = cursor.fetchall()
    v = Tk()
    for row in records:
       Label(v,text=row).pack()
    v.mainloop()

def display():        
    if choice.get() == '1':
        parking_status("open")
    elif choice.get() == '2':
        parking_status("full")
    elif choice.get() == '3':
        vehicle_status_report()
    
def di_back():
    di.pack_forget()
    menu.pack()

def display_info():
    menu.pack_forget()
    global choice,di
    di = Frame(Diya)
    choice = StringVar()
    choice.set('1')
    di.pack()
    Label(di,text=' P A R K I N G    R E P O R T S ',font = "Algerian 30 ") .grid(row=0,column=1)
    Radiobutton(di,text='1.  Free Space ',font = "Algerian 20 ",variable=choice,value='1').grid(row=1,column=1)
    Radiobutton(di,text='2.  Occupied Space ',font = "Algerian 20 ",variable=choice,value='2').grid(row=2,column=1)
    Radiobutton(di,text='3.  Vehicle Status ',font = "Algerian 20 ",variable=choice,value='3').grid(row=3,column=1)
    Button(di,text="Back",command=di_back).grid(row =4,column=0)
    Button(di,text="Submit",command=display).grid(row=4,column=2)
    
    

def Call():
    if str(Choice.get())=='1':
        add_parking_type_record()
    elif str(Choice.get()) == '2':
        add_parking_slot_record()
    elif str(Choice.get()) == '3':
        add_new_vehicle()
    elif str(Choice.get()) == '4':
        remove_vehicle()
    elif str(Choice.get()) == '5':
        search_menu()
    elif str(Choice.get()) == '6':
        display_info()
Diya = Tk()
# bg = PhotoImage(file=r"C:\Users\Hp\parking_system\Parking.png")
# backg = Canvas(Diya)
# backg.pack(fill="both",expand=True)
# backg.create_image(0,0,image=bg,anchor=NW)

menu=Frame(Diya)
Label(menu,text = "PARKING MANAGEMENT SYSTEM",font = "Algerian 30 ").pack()
Choice =StringVar()
Choice.set('1')
Radiobutton(menu,text = "Add new parking type",font = "Algerian 20 ",variable=Choice,value='1').pack()
Radiobutton(menu,text = "Add new parking slot",font = "Algerian 20 ",variable=Choice,value='2').pack()
Radiobutton(menu,text = " Vehicle Login",font = "Algerian 20 ",variable=Choice,value='3').pack()
Radiobutton(menu,text ="Vehicle Logout",font = "Algerian 20 ",variable=Choice,value='4').pack()
Radiobutton(menu,text ="Search",font = "Algerian 20 ",variable=Choice,value='5').pack()
Radiobutton(menu,text ="Display Information",font = "Algerian 20 ",variable=Choice,value='6').pack()
Button(menu,text = "Next",command=Call).pack()
menu.pack()
Diya.mainloop()