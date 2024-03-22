from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import datetime as dt
import datetime
from tkinter import messagebox
import os
cwd = os.getcwd()

# Get current year and month
date=datetime.date.today()
dateformat=date.strftime("%d-%m-%Y")
current_date=date.strftime("%d")
current_year = dt.now().year
current_month = dt.now().month

if not os.path.exists("Tests"):
    os.mkdir("Tests")
if not os.path.exists("Xrays"):
    os.mkdir("Xrays")
# Define the directory structure
year_folder = os.path.join(cwd,"Tests", str(current_year))
month_folder = os.path.join(year_folder, str(current_month))
date_folder = os.path.join(month_folder, str(current_date))
# Create the year folder if it doesn't exist
if not os.path.exists(year_folder):
    os.mkdir(year_folder)

# Create the month folder if it doesn't exist
if not os.path.exists(month_folder):
    os.mkdir(month_folder)
if not os.path.exists(date_folder):
    os.mkdir(date_folder)
year_folder1 = os.path.join(cwd,"Xrays", str(current_year))
month_folder1 = os.path.join(year_folder1, str(current_month))
date_folder1 = os.path.join(month_folder1, str(current_date))
# Create the year folder if it doesn't exist
if not os.path.exists(year_folder1):
    os.mkdir(year_folder1)

# Create the month folder if it doesn't exist
if not os.path.exists(month_folder1):
    os.mkdir(month_folder1)
if not os.path.exists(date_folder1):
    os.mkdir(date_folder1)

con=sqlite3.connect("opddatabase.db")
c=con.cursor()
c.execute("CREATE TABLE if not exists database (opdno text ,name text,age text,gender text,place text,date text)")
con.commit()
con.close()

root = Tk()
root.title("Electronic Health Record Management System")


def newpatientwindow():
    newpatientwindow=Toplevel()
    newpatientwindow.title("New Patient Entry")

    def newpatiententry():
        con=sqlite3.connect("opddatabase.db")
        c=con.cursor()
        c.execute("INSERT INTO database VALUES (:opdno,:name,:age,:gender,:place,:date)",{"opdno":opdnoentry.get(),"name": nameentry.get().lower(),"age":ageentry.get(),"gender":gendervar.get(),"place":placeentry.get().lower(),"date":dateentry.get()})
        con.commit()
        con.close()
        messagebox.showinfo("Success","Entry Succesful")

    Label(newpatientwindow,text="OPD no.").grid(row=0,column=0,padx=10,pady=10)
    Label(newpatientwindow,text="Name").grid(row=1,column=0,padx=10,pady=10)
    Label(newpatientwindow,text="Age").grid(row=2,column=0,padx=10,pady=10)
    Label(newpatientwindow,text="Gender").grid(row=3,column=0,padx=10,pady=10)
    Label(newpatientwindow,text="Place").grid(row=4,column=0,padx=10,pady=10)
    Label(newpatientwindow,text="Date").grid(row=5,column=0,padx=10,pady=10)

    opdnoentry=Entry(newpatientwindow,width=20,border=3)
    opdnoentry.grid(row=0,column=2,padx=10,pady=10)
    nameentry=Entry(newpatientwindow,width=20,border=3)
    nameentry.grid(row=1,column=2,padx=10,pady=10)
    ageentry=Entry(newpatientwindow,width=20,border=3)
    ageentry.grid(row=2,column=2,padx=10,pady=10)
    gendervar=StringVar(newpatientwindow)
    gendervar.set("Male")
    genderentry=OptionMenu(newpatientwindow,gendervar,"Male","Female")
    genderentry.grid(row=3,column=2,padx=10,pady=10)
    placeentry=Entry(newpatientwindow,width=20,border=3)
    placeentry.grid(row=4,column=2,padx=10,pady=10)
    dateentry=Entry(newpatientwindow,width=20,border=3)
    dateentry.grid(row=5,column=2,padx=10,pady=10)
    dateentry.insert(0,dateformat)
    Button(newpatientwindow,text="Submit",command=newpatiententry).grid(row=6,column=1,padx=10,pady=10)
    newpatientwindow.mainloop()
def oldpatientwindow():
    oldpatientwindow=Toplevel()
    def searchdetails():
        con=sqlite3.connect("opddatabase.db")
        c=con.cursor()
        c.execute("SELECT *,opdno FROM database WHERE opdno=:opdno",{"opdno":opdnoentry1.get()})
        records=c.fetchall()
        opdnolabel=records[0][0]
        namelabel=records[0][1]
        agelabel=records[0][2]
        genderlabel=records[0][3]
        placelabel=records[0][4]
        datelabel=records[0][5]
        list2=[opdnolabel,namelabel,agelabel,genderlabel,placelabel,datelabel]
        list1=["OPD no.","Name:","Age:","Gender:","Place:","Date:","Mob no","Dues:","Lab Dues:","Xray Dues:", "Lab Tests:","Xrays:","Fees Paid","Bill number"]
        for i in range(len(list1)):
            Label(oldpatientwindow,text=list1[i]).grid(row=i+2,column=0,padx=5,pady=5)
        for i in range(len(list2)):
            Label(oldpatientwindow,text=list2[i]).grid(row=i+2,column=1,padx=5,pady=5)
        dateentry2=Entry(oldpatientwindow,width=30,border=5)
        dateentry2.grid(row=7,column=1)
        dateentry2.insert(0,dateformat)
        mobnoentry=Entry(oldpatientwindow,width=30,border=5)
        mobnoentry.grid(row=8,column=1)
        duesentry=Entry(oldpatientwindow,width=30,border=5)
        duesentry.grid(row=9,column=1)
        labduesentry=Entry(oldpatientwindow,width=30,border=5)
        labduesentry.grid(row=10,column=1)
        xrayduesentry=Entry(oldpatientwindow,width=30,border=5)
        xrayduesentry.grid(row=11,column=1)
        labtestsentry=Entry(oldpatientwindow,width=30,border=5)
        labtestsentry.grid(row=12,column=1)
        xraysentry=Entry(oldpatientwindow,width=30,border=5)
        xraysentry.grid(row=13,column=1)
        feesentry=Entry(oldpatientwindow,width=30,border=5)
        feesentry.grid(row=14,column=1)
        billnoentry=Entry(oldpatientwindow,width=30,border=5)
        billnoentry.grid(row=15,column=1)
        def savetodatabase():
            con=sqlite3.connect(f"{opdnolabel}.db")
            c=con.cursor()
            c.execute("CREATE TABLE if not exists ptdatabase (opdno text ,name text,age text,gender text,place text,date text,mobno text,dues text,labdues text,xraydues text, labtests text,xrays text,fees text,billno text)")
            c.execute("INSERT INTO ptdatabase VALUES (:opdno,:name,:age,:gender,:place,:date,:mobno,:dues,:labdues,:xraydues,:labtests,:xrays,:fees,:billno)",{"opdno":opdnolabel,"name": namelabel.lower(),"age":agelabel,"gender":genderlabel,"place":placelabel,"date":dateentry2.get(),"mobno":mobnoentry.get(),"dues":duesentry.get(),"labdues":labduesentry.get(),"xraydues":xrayduesentry.get(),"labtests":labtestsentry.get(),"xrays":xraysentry.get(),"fees":feesentry.get(),"billno":billnoentry.get()})
            con.commit()
            con.close()
            messagebox.showinfo("Popup","Success")
            
        Button(oldpatientwindow,text="Submit",command=savetodatabase).grid(row=20,column=0,columnspan=2,sticky="nsew")
    Label(oldpatientwindow,text="OPD no.").grid(row=0,column=0,padx=10,pady=10)
    opdnoentry1=Entry(oldpatientwindow)
    opdnoentry1.grid(row=0,column=1,padx=10,pady=10)
    Button(oldpatientwindow,text="Sumbit",command=searchdetails).grid(row=1,column=0,columnspan=2,padx=10,pady=10)

    oldpatientwindow.mainloop()
def showdatabase():
    showdatabasewindow=Toplevel()
    showdatabasewindow.geometry("1350x650")
    Label(showdatabasewindow,text="OPD no:").pack()
    opdnoentry3=Entry(showdatabasewindow,width=20,border=5)
    opdnoentry3.pack()
    def showptdatabase():
        con=sqlite3.connect(f"{opdnoentry3.get()}.db")
        c=con.cursor()
        c.execute("SELECT *,opdno FROM ptdatabase WHERE opdno=:opdno",{"opdno":opdnoentry3.get()})
        records=c.fetchall()
        treeframe=Frame(showdatabasewindow)
        treeframe.pack()
        tree_scroll=Scrollbar(treeframe)
        tree_scroll.pack(side=RIGHT,fill=Y)
        tree_scrollh=Scrollbar(treeframe,orient="horizontal")
        tree_scrollh.pack(side=BOTTOM,fill=X)
        mytree=ttk.Treeview(treeframe,yscrollcommand=tree_scroll.set,xscrollcommand=tree_scrollh.set)
        tree_scroll.config(command=mytree.yview)
        tree_scrollh.config(command=mytree.xview)
        mytree['columns']=("opdno","name","age","gender","place","date","mobno","dues","labdues","xraydues","labtests","xrays","fees","billno")
        mytree.column("#0",width=0)
        mytree.column("opdno",width=120)
        mytree.column("name",width=120)
        mytree.column("age",width=120)
        mytree.column("gender",width=120)
        mytree.column("place",width=120)
        mytree.column("date",width=120)
        mytree.column("mobno",width=120)
        mytree.column("dues",width=120)
        mytree.column("labdues",width=120)
        mytree.column("xraydues",width=120)
        mytree.column("labtests",width=120)
        mytree.column("xrays",width=120)
        mytree.column("fees",width=120)
        mytree.column("billno",width=120)
        mytree.heading("#0",text="")
        mytree.heading("opdno",text="OPD no")
        mytree.heading("name",text="Name")
        mytree.heading("age",text="Age")
        mytree.heading("gender",text="Gender")
        mytree.heading("place",text="Place")
        mytree.heading("date",text="Date")
        mytree.heading("mobno",text="Mob No")
        mytree.heading("dues",text="Dues")
        mytree.heading("labdues",text="Lab Dues")
        mytree.heading("xraydues",text="X Ray Dues")
        mytree.heading("labtests",text="Lab Tests")
        mytree.heading("xrays",text="X Rays")
        mytree.heading("fees",text="Fees Paid")
        mytree.heading("billno",text="Bill no.")

        for i in range(len(records)):        
            mytree.insert(parent="",index="end",iid=i+1,text="",values=records[i])
        mytree.pack()

    Button(showdatabasewindow,text="Submit",command=showptdatabase).pack()
    showdatabasewindow.mainloop()
def searchbynamewindow():
    findbyname=Toplevel()
    def searchbyname():
        searchname1entryvalue=searchname1.get()
        searchname1entryvalue.lower()
        con=sqlite3.connect("opddatabase.db")
        c=con.cursor()
        c.execute("SELECT *,name FROM database WHERE name=:name",{"name":searchname1entryvalue})
        global records
        records=c.fetchall()
        record1=str()
        for record in records:
            record1 += str(record[0]) +"\t"+str(record[1])+"\t"+str(record[2])+"\t"+str(record[3])+"\t"+str(record[4])+"\t"+str(record[5])+ "\n"
        queerylabel = Label(findbyname, text=record1)
        queerylabel.pack()
    Label(findbyname,text="Name: ").pack()
    searchname1=Entry(findbyname)
    searchname1.pack()
    Button(findbyname,text="Submit",command=searchbyname).pack()
    findbyname.mainloop()
def searchbynameplacewindow():
    findbynameplace=Toplevel()
    def searchbynameplace():
        searchname2entryvalue=searchname2.get()
        searchplaceentryvalue=searchplace.get()

        con=sqlite3.connect("opddatabase.db")
        c=con.cursor()
        c.execute("SELECT *,name FROM database WHERE name=:name AND place=:place",{"name":searchname2entryvalue.lower(),"place":searchplaceentryvalue.lower()})
        records2=c.fetchall()
        record12=str()
        for record in records2:
            record12 += str(record[0]) +"\t"+str(record[1])+"\t"+str(record[2])+"\t"+str(record[3])+"\t"+str(record[4])+"\t"+str(record[5])+ "\n"
        queerylabel = Label(findbynameplace, text=record12)
        queerylabel.pack()
    Label(findbynameplace,text="Name: ").pack()
    searchname2=Entry(findbynameplace)
    searchname2.pack()
    Label(findbynameplace,text="Place: ").pack()
    searchplace=Entry(findbynameplace)
    searchplace.pack()
    Button(findbynameplace,text="Submit",command=searchbynameplace).pack()
    findbynameplace.mainloop()
def showtestfolder():
    os.startfile("Tests")
def showxrayfolder():
    os.startfile("Xrays")
def showdues():
        opdnolist=[]
        namelist=[]
        placelist=[]
        dueslist1=[]
        dueslist=[]
        con=sqlite3.connect("opddatabase.db")
        c=con.cursor()
        c.execute("SELECT *,oid FROM database")
        records=c.fetchall()     
        for record in records:
            opdnolist.append(record[0])
            namelist.append(record[1])
            placelist.append(record[4])
        
        for opdno in opdnolist:
            con=sqlite3.connect(f"{opdno}.db")
            c=con.cursor()
            c.execute("SELECT * FROM ptdatabase")
            records=c.fetchall()
            con.commit()
            con.close()
            for record in records:
                dueslist1.append(record[7])
            dueslist.append(dueslist1[len(dueslist1)-1])
        dueswindow=Toplevel()
        treeframe=Frame(dueswindow)
        treeframe.pack()
        tree_scroll=Scrollbar(treeframe)
        tree_scroll.pack(side=RIGHT,fill=Y)
        mytree=ttk.Treeview(treeframe,yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=mytree.yview)
        
        mytree['columns']=("opdno","name","place","dues")
        mytree.column("#0",width=0)
        mytree.column("opdno",width=120)
        mytree.column("name",width=120)   
        mytree.column("place",width=120)           
        mytree.heading("#0",text="")
        mytree.heading("opdno",text="OPD no")
        mytree.heading("name",text="Name")        
        mytree.heading("place",text="Place")        
        mytree.heading("dues",text="Dues")
        uniqueid=0
        for opdno,name,place,dues in zip(opdnolist,namelist,placelist,dueslist):
            iid=f"{opdno}_{name}"
            mytree.insert(parent="",index="end",iid=iid,text="",values=(opdno,name,place,dues))
            uniqueid+=1
                        
        mytree.pack()
        dueswindow.mainloop()
            
            
Label(root,text="Electronic Health Records System").grid(row=0,column=0,columnspan=2,padx=10,pady=10)
Button(root,text="New Patient",command=newpatientwindow).grid(row=1,column=0,columnspan=2,padx=10,pady=10)
Button(root,text="Old Patient",command=oldpatientwindow).grid(row=2,column=0,columnspan=2,padx=10,pady=10)
Button(root,text="Search by OPD no.",command=showdatabase).grid(row=3,column=0,padx=10,pady=10)
Button(root,text="Search by Name",command=searchbynamewindow).grid(row=3,column=1,padx=10,pady=10)
Button(root,text="Search by Name and Place",command=searchbynameplacewindow).grid(row=4,column=0,columnspan=2,padx=10,pady=10)
Button(root,text="Tests",command=showtestfolder).grid(row=5,column=0,padx=10,pady=10)
Button(root,text="Xrays",command=showxrayfolder).grid(row=5,column=1,padx=10,pady=10)
Button(root,text="Show Dues",command=showdues).grid(row=6,column=0,padx=10,pady=10)

root.mainloop()