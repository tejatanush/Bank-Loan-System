from tkinter import*
from tkinter import ttk,messagebox
import pymysql
class customer:
    def __init__(self,root):
        self.root=root
        self.root.title('Bank loan system')
        self.root.geometry('1350x720+0+0')
        title=Label(self.root,text="Bank loan system",font=('times nwe rommon',40,'bold'),bg='yellow',fg='red',bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)

        self.loanId=StringVar()
        self.name=StringVar()
        self.mob=StringVar()
        self.age=StringVar()
        self.add=StringVar()
        self.amo=StringVar()
        self.interest=StringVar()
        self.du=StringVar()
        self.mp=StringVar()
        self.tp=StringVar()


        Detail_F=Frame(self.root,bd=4,relief=RIDGE)
        Detail_F.place(x=10,y=100,width=500,height=620)
        lbl_id=Label(Detail_F,text='Loan Id',font=('times new rommon',18,'bold'))
        lbl_id.grid(row=0,column=0,padx=20,pady=10)
        txt_id=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.loanId)
        txt_id.grid(row=0,column=1)

        lbl_name=Label(Detail_F,text='Full Name',font=('times new rommon',18,'bold'))
        lbl_name.grid(row=1,column=0,padx=20,pady=10)
        txt_name=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.name)
        txt_name.grid(row=1,column=1)

        lbl_mob=Label(Detail_F,text='Mobile Number',font=('times new rommon',18,'bold'))
        lbl_mob.grid(row=2,column=0,padx=20,pady=10)
        txt_mob=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.mob)
        txt_mob.grid(row=2,column=1)

        lbl_age=Label(Detail_F,text='Age',font=('times new rommon',18,'bold'))
        lbl_age.grid(row=3,column=0,padx=20,pady=10)
        txt_age=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.age)
        txt_age.grid(row=3,column=1)

        lbl_add=Label(Detail_F,text='Address',font=('times new rommon',18,'bold'))
        lbl_add.grid(row=4,column=0,padx=20,pady=10)
        txt_add=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.add)
        txt_add.grid(row=4,column=1)

        lbl_amo=Label(Detail_F,text='Loan Amount',font=('times new rommon',18,'bold'))
        lbl_amo.grid(row=5,column=0,padx=20,pady=10)
        txt_amo=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.amo)
        txt_amo.grid(row=5,column=1)

        lbl_in=Label(Detail_F,text='Rate of Interest',font=('times new rommon',18,'bold'))
        lbl_in.grid(row=6,column=0,padx=20,pady=10)
        txt_in=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.interest)
        txt_in.grid(row=6,column=1)

        lbl_du=Label(Detail_F,text='Duration(months)',font=('times new rommon',18,'bold'))
        lbl_du.grid(row=7,column=0,padx=20,pady=10)
        txt_du=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.du)
        txt_du.grid(row=7,column=1)

        lbl_mp=Label(Detail_F,text='Monthly Payment',font=('times new rommon',18,'bold'))
        lbl_mp.grid(row=8,column=0,padx=20,pady=10)
        txt_mp=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.mp)
        txt_mp.grid(row=8,column=1)

        lbl_tp=Label(Detail_F,text='Total Payment',font=('times new rommon',18,'bold'))
        lbl_tp.grid(row=9,column=0,padx=20,pady=10)
        txt_tp=Entry(Detail_F,font=('time new rommon',18,'bold'),bd=3,relief=FLAT,textvariable=self.tp)
        txt_tp.grid(row=9,column=1)


        RFrame=Frame(self.root,bd=4,relief='groove')
        RFrame.place(x=535,y=90,width=800,height=520)

        yscroll=Scrollbar(RFrame,orient=VERTICAL)
        self.employee_table=ttk.Treeview(RFrame,column=('empid','name','duration','rate','mpayment','tpayment','mobile','add','age','amo'),yscrollcommand=yscroll.set(0,0.001))
        yscroll.pack(side=RIGHT,fill=Y)
        yscroll.config(command=self.employee_table.yview)
        self.employee_table.heading('empid',text='Loan Id')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('duration',text='Duration(years)')
        self.employee_table.heading('rate',text='Rate of Interest')
        self.employee_table.heading('mpayment',text='Monthly Payment')
        self.employee_table.heading('tpayment',text='Total Payment')
        self.employee_table.heading('mobile',text='Mobile number')
        self.employee_table.heading('add',text='Address')
        self.employee_table.heading('age',text='Age')
        self.employee_table.heading('amo',text='Amount')
        self.employee_table['show']='headings'
        self.employee_table.column('empid',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('duration',width=100)
        self.employee_table.column('rate',width=100)
        self.employee_table.column('mpayment',width=100)
        self.employee_table.column('tpayment',width=100)
        self.employee_table.column('mobile',width=100)
        self.employee_table.column('add',width=100)
        self.employee_table.column('age',width=100)
        self.employee_table.column('amo',width=100)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.fetch()
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)



        btnFrame=Frame(self.root,bd=4,relief='groove')
        btnFrame.place(x=535,y=610,width=800,height=100)
        btn1=Button(btnFrame,text='Add Record',font='arial 15 bold',command=self.addrecord)
        btn1.grid(row=0,column=0,padx=10,pady=10)
        btn2=Button(btnFrame,text='Update',font='arial 15 bold',command=self.update)
        btn2.grid(row=0,column=1,padx=10,pady=10)
        btn3=Button(btnFrame,text='Delete',font='arial 15 bold',command=self.delete)
        btn3.grid(row=0,column=2,padx=10,pady=10)
        btn4=Button(btnFrame,text='Reset',font='arial 15 bold',command=self.reset)
        btn4.grid(row=0,column=3,padx=10,pady=10)
        btn5=Button(btnFrame,text='Exit',font='arial 15 bold',command=self.Exit)
        btn5.grid(row=0,column=4,padx=10,pady=10)


    def total(self):
        p= int(self.amo.get())
        r= int(self.interest.get())
        y= int(self.du.get())
        t= (p*r*y*12)/100
        m=(p+t)/(y*12)
        self.mp.set(str(round(m,2)))
        self.tp.set(str(p+t))



    def addrecord(self):
        if self.loanId.get()=='':
                messagebox.showerror('Error,customer details are must')
        else:
            con=pymysql.connect(host='localhost',user='root',password='',database='emp')
            cur=con.cursor()
            cur.execute("Select * from customer")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==self.loanId.get():
                    messagebox.showerror('Error','Duplicate entry not allowed')
                    return
            self.total()
            cur.execute('insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.loanId.get(),
                                                                self.name.get(),
                                                                self.du.get(),
                                                                self.interest.get(),
                                                                self.mp.get(),
                                                                self.tp.get(),
                                                                self.mob.get(),
                                                                self.add.get(),
                                                                self.age.get(),
                                                                self.amo.get()))
            con.commit()
            
            self.fetch()
            con.close()
    def fetch(self):
            con=pymysql.connect(host='localhost',user='root',password='',database='emp')
            cur=con.cursor()
            cur.execute("Select * from customer")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.employee_table.delete(*self.employee_table.get_children())
                for row in rows:
                    self.employee_table.insert('',END,values=row)
                con.commit()
                con.close()
    def get_cursor(self,ev):
        cur_row=self.employee_table.focus()
        content=self.employee_table.item(cur_row)
        row=content['values']
        self.loanId.set(row[0])
        self.name.set(row[1])
        self.du.set(row[2])
        self.interest.set(row[3])
        self.mp.set(row[4])
        self.tp.set(row[5])
        self.mob.set(row[6])
        self.add.set(row[7])
        self.age.set(row[8])
        self.amo.set(row[9])
    def update(self):
        if self.loanId.get()=='':
            messagebox.showerror('Error','Input information for update')   
        else:
            con=pymysql.connect(host='localhost',user='root',password='',database='emp')
            cur=con.cursor()
            cur.execute("update customer set Name=%s, Duration=%s, Rate_of_interest=%s,  Monthly_Payment=%s,Total_Payment=%s,Mobile_number=%s,Address=%s,Age=%s,Amount=%s WHERE Loan_Id=%s",(self.loanId.get(),
                                                                                                                                        self.name.get(),
                                                                                                                                        self.du.get(),
                                                                                                                                        self.interest.get(), 
                                                                                                                                        self.mp.get(),
                                                                                                                                        self.tp.get(),
                                                                                                                                        self.mob.get(),
                                                                                                                                        self.add.get(),
                                                                                                                                        self.age.get(),
                                                                                                                                        self.amo.get()))
            messagebox.showinfo('info',f'Recor{self.loanId.get()} Updated Successfully')
            con.commit()
            self.fetch()
            con.close()
            self.reset()
    def delete(self):
            if self.loanId.get()=='':
                messagebox.showerror('Error','Input loan id to delete the record')
            else:
                con=pymysql.connect(host='localhost',user='root',password='',database='emp')
                cur=con.cursor()
                cur.execute("delete from customer where Loan_Id=%s",self.loanId.get())
                con.commit()
                con.close()
                self.fetch()
                self.reset()
                


    def reset(self):
        self.loanId.set('')
        self.name.set('')
        self.mob.set('')
        self.age.set('')
        self.add.set('')
        self.amo.set('')
        self.interest.set('')
        self.du.set('')
        self.mp.set('')
        self.tp.set('')
            

    def Exit(self):
        if messagebox.askyesno('Exit','Do you really want to exit'):
                root.destroy()
            


    




root=Tk()
obj=customer(root)
root.mainloop()