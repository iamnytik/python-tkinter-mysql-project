from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="password",database="dbmsproject")
check=0

def enter():
    def addlogistic_unit():

        e1=ent1.get()
        e2=ent2.get()
        e3=ent3.get()
        cur=con.cursor()
        x='y'
        cur.execute("insert into logistic_units(logistic_unit_id,trans_type,rent,available) values(%s,%s,%s,%s)",(e1,e2,e3,x))
        con.commit()
        logistic_unitid.delete(0,END)
        trans_type.delete(0,END)
        price.delete(0,END)
        messagebox.showinfo('success',"logistic_unit inserted!")
    #frame2add()

#function for deleting a logistic_unit
    def dellogistic_unit():
        e1=ent1.get()
        e2=ent2.get()
        e3=ent3.get()
        cur=con.cursor()
        x='y'
        cur.execute("delete from logistic_units where logistic_unit_id=%s and available=%s",(e1,x))
        con.commit()
        logistic_unitid.delete(0,END)
        trans_type.delete(0,END)
        price.delete(0,END)
        messagebox.showinfo('success','logistic_unit deleted!!')

#creating the main window
    root=Toplevel()
    root.geometry("500x500")
    root.title("DBMS PROJECT by Nytik,@iamnytik")

    #creating a notebook for tabs(admin,book,return)
    notebook=ttk.Notebook(root)
    notebook.pack()

    #creating 3 frames 
    frame1=Frame(notebook,width=500,height=500)
    frame2=Frame(notebook,width=500,height=500)  
    frame3=Frame(notebook,width=500,height=500)

    frame1.pack(fill="both",expand=1)
    frame2.pack(fill="both",expand=1)
    frame3.pack(fill="both",expand=1)

    notebook.add(frame1,text="admin")
    notebook.add(frame2,text="book")
    notebook.add(frame3,text="return")

    #notebook.hide(1)

    # def show():
    #    notebook.add(frame2,text="book")


    ent1=IntVar()
    ent2=StringVar()
    ent3=IntVar()

    #adding and droping logistic_unit window
    lab=Label(frame1,text="WELCOME TO LOGISTICAL MANAGEMENT SYSTEM").pack()

    lab1=Label(frame1,text="UNIT_ID").place(x=150,y=50)
    logistic_unitid=Entry(frame1,textvariable=ent1)
    logistic_unitid.place(x=225,y=50)

    lab2=Label(frame1,text="UNIT_TYPE").place(x=150,y=80)
    trans_type=Entry(frame1,textvariable=ent2)
    trans_type.place(x=225,y=80)

    lab3=Label(frame1,text="RENT").place(x=150,y=110)
    price=Entry(frame1,textvariable=ent3)
    price.place(x=225,y=110)

    but1=Button(frame1,text="ADD AN UNIT",command=addlogistic_unit).place(x=200,y=200)
    but2=Button(frame1,text="DROP AN UNIT",command=dellogistic_unit).place(x=300,y=200)

    #butshow=Button(frame1,text="GO TO BOOK",command=show).place(x=250,y=400)
    # def frame2add():
    #displaying available logistic_units
    labf=Label(frame2,text="AVAILABLE UNITS").pack()

    treescroll=Frame(frame2)
    treescroll.pack()

    scroll=Scrollbar(frame2)
    scroll.pack(side=RIGHT,fill=Y)
    tree=ttk.Treeview(frame2,yscrollcommand=scroll.set) #yscrollcommand=scroll.set)
    scroll.config(command=tree.yview)

    #vsb=Scrollbar(root,orient="vertical")
    #vsb.configure(command=tree.yview)
    #tree.configure(yscrollcommand=vsb.set)
    #vsb.pack(fill=Y,side=RIGHT)

    tree['show']='headings'
    s=ttk.Style(root)
    s.theme_use("clam")
    tree.pack()

    tree['columns']=("logistic_unit_id","trans_type","rent")
    cur=con.cursor()
    y='y'
    cur.execute("select logistic_unit_id,trans_type,rent from logistic_units where available='y'")
        #con.commit()
        #cur.close()
    tree.column("logistic_unit_id",width=50,minwidth=50,anchor=CENTER)
    tree.column("trans_type",width=100,minwidth=100,anchor=CENTER)
    tree.column("rent",width=150,minwidth=150,anchor=CENTER)

        #headings
    tree.heading("logistic_unit_id",text="logistic_unitid",anchor=CENTER)
    tree.heading("trans_type",text="trans_type",anchor=CENTER)
    tree.heading("rent",text="rent",anchor=CENTER)

    i=0
    for row in cur:
        tree.insert('',i,text='',values=(row[0],row[1],row[2]))
        i+=1

    con.commit()

    #vsb=Scrollbar(root,orient="vertical")
    #vsb.configure(command=tree.yview)
    #tree.configure(yscrollcommand=vsb.set)
    #vsb.pack(fill=Y,side=RIGHT)

    ent4=IntVar()
    ent5=StringVar()
    ent6=StringVar()
    ent7=StringVar()
    ent8=StringVar()
    ent9=IntVar()
    def update_user():
        a=ent4.get()
        b=ent5.get()
        c=ent6.get()
        d=ent7.get()
        e=ent8.get()
        f=ent9.get()#sus 
        cur=con.cursor()
        
        cur.execute("UPDATE users SET  user_id=(%s),name= (%s), email= (%s),startdate=(%s),loc=(%s),time=(%s)   WHERE    user_id= (%s)    ",(a,b,c,d,e,f,a))
        con.commit()

        messagebox.showinfo("success","UPDATED USER DETAILS")
    #function to book a logistic_unit
    def booklogistic_unit():
        a=ent4.get()
        b=ent5.get()
        c=ent6.get()
        d=ent7.get()
        e=ent8.get()
        f=ent9.get()#sus 
        cur=con.cursor()
        cur.execute("insert into users(name,email,startdate,loc,time) values(%s,%s,%s,%s,%s)",(b,c,d,e,f))
        con.commit()
        cur=con.cursor()
        cur.execute("select user_id from users where name=%s and email=%s",(b,c))
        ac=0
        for r in cur:
            ac=r[0]
        con.commit()
        cur=con.cursor()
        n='n'
        cur.execute("insert into manages(user_id,logistic_unit_id) values(%s,%s)",(ac,a))
        x='n'
        cur.execute("update logistic_units set available=%s where logistic_unit_id=%s",(x,a))
        con.commit()
        #cur.execute("update manages set user_id = (select user_id from users natural join logistic_units where name=%s and email=%s)",(b,c))
        #con.commit()
        #cur.execute("delete from users where user_id not in (select  user_id from manages)")
        #con.commit()
        #messagebox.showinfo("success","logistic_unit booked")
        #cur.execute("delete from manages where manages.logistic_unit_id=%s in (select logistic_unit_id from logistic_units where available='n')",(a))
        #con.commit()
        cur.execute("delete from manages where logistic_unit_id not in (select logistic_unit_id from logistic_units)")
        con.commit()
        cur.execute("delete from users where user_id not in (select user_id from manages)")
        con.commit()
        messagebox.showinfo("success","logistic_unit booked")
        logistic_unitbook.delete(0,END)
        logistic_unitname.delete(0,END)
        logistic_unitmail.delete(0,END)
        logistic_unitdate.delete(0,END)
        logistic_unitloc.delete(0,END)

    def total_cursor():
        pass
        #cur.execute('declare @rent int IF NOT EXISTS')
        cur.execute("create or replace view  summary  as select logistic_unit_id,user_id,name,email,time,rent from manages natural join users natural join logistic_units where available='n';")
         
 
    
    def returnlogistic_unit():
        root1=Toplevel()
        root1.geometry("600x600")
        root1.title("RELEASE LOGISTICAL_UNIT")
        lab=Label(root1,text="UNIT TO BE RETURNED").pack()
        tree1=ttk.Treeview(root1)
        tree1["show"]="headings"
        s=ttk.Style(root1)
        s.theme_use("clam")
        tree1["columns"]=("logistic_unitid","userid","name","email","time","rent",'total')#cost
        tree1.column("logistic_unitid",width=70,minwidth=70,anchor=CENTER)
        tree1.column("userid",width=70,minwidth=70,anchor=CENTER)
        tree1.column("name",width=150,minwidth=150,anchor=CENTER)
        tree1.column("email",width=150,minwidth=150,anchor=CENTER)
        tree1.column("time",width=150,minwidth=150,anchor=CENTER)
        tree1.column("rent",width=150,minwidth=150,anchor=CENTER)
        tree1.column("total",width=150,minwidth=150,anchor=CENTER)
        tree1.heading("logistic_unitid",text="logistic_unitid",anchor=CENTER)
        tree1.heading("userid",text="userid",anchor=CENTER)
        tree1.heading("name",text="name",anchor=CENTER)
        tree1.heading("email",text="email",anchor=CENTER)
        tree1.heading("time",text="usage_time",anchor=CENTER)
        tree1.heading("rent",text="rent",anchor=CENTER)
        tree1.heading("total",text="total",anchor=CENTER)
        cur=con.cursor()

        cur.execute("select logistic_unit_id,user_id,name,email,time,rent from manages natural join users natural join logistic_units where available='n'")
        i=0
        for row in cur:
            tree1.insert('',i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5]))
            i+=1
        con.commit()

        
        def rclogistic_unit():
            s1=bt1.get()
            s2=bt2.get()
            s3=bt3.get()
            cur=con.cursor()
            y='y'
            cur.execute("update logistic_units set available=%s where logistic_unit_id=%s",(y,s1))
            con.commit()
            cur.execute("delete from manages where logistic_unit_id=%s and user_id=%s",(s1,s2))
            con.commit()
            messagebox.showinfo("logistic_unit returned","thank u come again!")
            b1.delete(0,END)
            b2.delete(0,END)
            b3.delete(0,END)
            
        bt1=IntVar()
        bt2=IntVar()
        bt3=StringVar()
        
        
        
        l1=Label(root1,text="UNIT_ID").place(x=210,y=270)
        b1=Entry(root1,textvariable=bt1)
        #b1.place(x=260,y=270)

        b1.place(x=300,y=270)
        l2=Label(root1,text="USERID").place(x=210,y=300)
        b2=Entry(root1,textvariable=bt2)
        #b2.place(x=260,y=300)
        
        b2.place(x=300,y=300)
        l3=Label(root1,text="NAME").place(x=210,y=330)
        b3=Entry(root1,textvariable=bt3)
        #b3.place(x=260,y=330)

        b3.place(x=300,y=330)
        b4=Button(root1,text="RETURN UNIT",command=rclogistic_unit).place(x=250,y=370)

        vsb=ttk.Scrollbar(root1,orient="vertical")
        vsb.configure(command=tree1.yview)
        tree1.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)
        
        
        tree1.pack()    
        root1.mainloop()



    lab4=Label(frame2,text="UNIT_ID").place(x=120,y=270)
    logistic_unitbook=Entry(frame2,textvariable=ent4)
    logistic_unitbook.place(x=200,y=270)

    lab5=Label(frame2,text="NAME").place(x=120,y=300)
    logistic_unitname=Entry(frame2,textvariable=ent5)
    logistic_unitname.place(x=200,y=300)

    lab6=Label(frame2,text="EMAIL").place(x=120,y=330)
    logistic_unitmail=Entry(frame2,textvariable=ent6)
    logistic_unitmail.place(x=200,y=330)

    lab7=Label(frame2,text="DATE").place(x=120,y=360)
    logistic_unitdate=Entry(frame2,textvariable=ent7)
    logistic_unitdate.place(x=200,y=360)

    lab8=Label(frame2,text="LOCATION").place(x=120,y=390)
    logistic_unitloc=Entry(frame2,textvariable=ent8)
    logistic_unitloc.place(x=220,y=390)

    lab9=Label(frame2,text="TIME").place(x=120,y=420)
    logistic_unittime=Entry(frame2,textvariable=ent9)
    logistic_unittime.place(x=220,y=420)#sus

    but3=Button(frame2,text="UTILIZE AN UNIT ",command=booklogistic_unit).place(x=50,y=450)
    b10=Button(frame2,text="REFRESH",command=enter).place(x=310,y=450)

    b10=Button(frame2,text="UPDATE",command=update_user).place(x=220,y=450)


    la=Label(frame3,text="RELEASE UNIT PORTAL").place(x=190,y=10)
    but4=Button(frame3,text="GO TO RELEASE UNIT",command=returnlogistic_unit).place(x=200,y=100)
    #tree.pack()
    frame2.mainloop()
    root.mainloop()



def submit():
    c=0
    username=a.get()
    password=b.get()
    cur.execute("select *from admin")
    for i in cur:
        if i[0]==username and i[1]==password:
            global check
            c=1
            check=1
            break
   #else 
      # if i[0]==user
    #xyz need to implement a diffrent view for two users  
    #cur.execute("select *from users")
    #need to change admin table by adding a new column called user id 
    if c==1:
        messagebox.showinfo("valid!","welcome! admin")
        enter()
                   
    else:
        messagebox.showwarning("not valid!!","try again!")

    
r=Tk()
r.title(" LOGISTICS MANAGEMENT  SYSTEM")
r.geometry("550x550")
s=ttk.Style(r)
s.theme_use("clam")
cur=con.cursor(buffered=True)
#Procedure

cur.execute("CREATE PROCEDURE IF NOT  EXISTS validate_customer (IN time INT) DETERMINISTIC NO SQL BEGIN 	IF time < 2 THEN 		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You must book for a minimum of 2 days '; 	END IF; END; ")
cur.execute("CREATE TRIGGER IF NOT EXISTS  validate_time BEFORE INSERT ON users FOR EACH ROW BEGIN CALL validate_customer( NEW.time); END;")

con.commit()
a=StringVar()
b=StringVar()
t=Label(r,text="ADMIN PORTAL").pack()
user=Label(r,text="USERNAME").place(x=100,y=150)
g=Entry(r,textvariable=a)
g.place(x=220,y=150)
passw=Label(r,text="PASSWORD").place(x=100,y=180)
h=Entry(r,textvariable=b)
h.place(x=220,y=180)
bo=Button(r,text="SUBMIT",command=submit)
bo.place(x=250,y=220)
#b5=Button(r,text="REFRESH",command=enter)
#b5.place(x=250,y=250)
con.commit()
r.mainloop()


