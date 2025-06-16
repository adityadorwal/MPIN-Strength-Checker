#Importing all the REquired LOcal FIles 
from checker import commonly_used
from demographics import check_demographics
from valid_dob import get_valid_date,check_valid_date



#******************************** FOR LIVE USE WITH WHILE LOOP UNTIL THE MPN IS SET CORRECTLY WITH ALL REQUIRED DETAILS ***************************************
#*************************NEED of user input for dob,spouse_dob,anniversary date,mpin.*********************
      
# print("Welcome to OneBanc")
# print("Thanks for opening account with us")
# print ("Before setting the account , i would require few details from you")
# dob=get_valid_date("Pls enter your DOB in DD-MM-YYYY format : ")
# maritial_status =input("Pls enter your maritial status(Y/n) : ").strip()
# if(maritial_status.lower() == "yes"):
#     spouse_dob=get_valid_date("Pls enter your spouse DOb in DD-MM-YYYY format : ")
#     anniversary_date = get_valid_date("Pls enter your Anniversary date")
# print("Thank you for the details ")

# reasons=["Dummy"]

# while(reasons):
#     mpin = input("Pls SET an 4-digit OR 6-digit MPIN : ").strip()
#     length_mpin = len(mpin)
#     if not(length_mpin ==4 or length_mpin==6):
#         print("Invalid digits of MPIN ,Pls Try again")
#         continue
#     elif not(mpin.isdigit()):
#         print("Please only enter Numeric values ")
#         continue
    
#     reasons=[]
#     if commonly_used(mpin):
#         reasons.append("COMMONLY_USED")
#     if check_demographics(dob,mpin):
#         reasons.append("DEMOGRAPHIC_DOB_SELF")
#     if(maritial_status.lower() == "yes"):
#         if check_demographics(spouse_dob,mpin):
#             reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
#         if check_demographics(anniversary_date,mpin):
#             reasons.append("DEMOGRAPHIC_ANNIVERSARY")
#     if reasons:
#         print("Strength : Weak")
#         print(reasons)
#         print("Pls try again again \n \n")
#     else:
#         print("Strength : Strong")
#         print(reasons)
#******************************** FOR LIVE USE WITH WHILE LOOP UNTIL THE MPN IS SET CORRECTLY WITH ALL REQUIRED DETAILS ***************************************

         
        
        
        
        
        
#******************************** For TESTCASE PURPOSE ***********************************************************************************   
#*******************mpin,dob,spuse_dob,anniversary_date all are as test case input*******************************************************
    
# def InBuilt_testcase(mpin,dob="",spouse_dob="",anniversary_date=""):
#     length_mpin = len(mpin)
#     reasons=[]
#     #Check for correct MPIN Length
#     if not(length_mpin ==4 or length_mpin==6):
#         print("Invalid digits of MPIN ,Pls Try again")
        
#     # Chek wether the MPIN contains only digits  
#     elif not(mpin.isdigit()):
#         print("Please only enter Numeric values ")
    
#     # process if mpin satisfies the condition
#     else:
        
#         #Check for commonly used MPIN's
#         if commonly_used(mpin):
#             reasons.append("COMMONLY_USED")
            
            
#         #Check for Valid DOB and the MPIn"S Demographics via DOB  
#         if (check_valid_date(dob)):
#             return("Pls Enter a correct DOb")
#         else:
#             if check_demographics(dob,mpin):
#                 reasons.append("DEMOGRAPHIC_DOB_SELF")
                
                
#         #Check for valid SPouse_dob and the anniversary date and the check for the demographics       
#         if(spouse_dob!="" and anniversary_date==""):
#             return("Pls enter the anniversary date")
#         elif(spouse_dob=="" and anniversary_date!=""):
#             return("Pls enter your Spouse DOB")
#         elif(spouse_dob!="" and anniversary_date!=""):
#             if check_valid_date(spouse_dob):return("Pls enter correct Date")
#             if check_valid_date(anniversary_date):return("Pls enter correct Date")
#             if check_demographics(spouse_dob,mpin):
#                 reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
#             if check_demographics(anniversary_date,mpin):
#                 reasons.append("DEMOGRAPHIC_ANNIVERSARY")
                
    
#         #Print Strength of the MPIN 
#         if reasons:
#             print("Strength : Weak")
#         else:
#             print("Strength : Strong")
            
#         #Return the List of REasons
#     return("Reasons : ",reasons)

#*************************************FOR TESTCASE PURPOSE****************************************************************




#*************************************FOR GUI INTERFACE WITH ALL REQUIRED FUNCTIONALITY ********************************************
#*************************NEED of user input for dob,spouse_dob,anniversary date,mpin.*********************
   

import tkinter as tk
from tkinter import messagebox
from checker import commonly_used
from demographics import check_demographics
from valid_dob import get_valid_date
 
root = tk.Tk()
root.title("MPIN_VALIDATOR")
root.geometry("600x750")
root.configure(bg='#1e3a8a')

# To check MPIN strength
def check_strength(mpin,dob,spouse_dob,anniversary_date):
    reasons=[]
    if commonly_used(mpin):
        reasons.append("COMMONLY_USED")
    if check_demographics(dob,mpin):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if spouse_dob:
        if check_demographics(spouse_dob,mpin):
            reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
        if check_demographics(anniversary_date,mpin):
            reasons.append("DEMOGRAPHIC_ANNIVERSARY")
    return(reasons)



# TO validate Inputs
def validate_inputs():
    # Storing the Input details in Variables 
    dob = dob_entry.get().strip()
    mpin = mpin_entry.get().strip()
    maritial_status_data = maritial_status.get()
    spouse_dob = spouse_entry.get().strip() if maritial_status_data == 'married' else""
    anniversary_date = anniversary_entry.get().strip() if maritial_status_data == 'married' else""

    result_text.delete(1.0, tk.END)
    strength_label.config(text="")
    
    if not dob:
        messagebox.showerror("Error", "Please enter your Date of Birth!")
        return
    if not get_valid_date(dob):
        messagebox.showerror("Error", "Invalid date format! Please enter in DD-MM-YYYY format.")
        dob_entry.delete(0,tk.END)
        return
    
    if maritial_status_data == "married" and not spouse_dob:
        messagebox.showerror("Error", "Please enter spouse's Date of Birth!")
        return
    
    if maritial_status_data == "married" and not anniversary_date:
        messagebox.showerror("Error", "Please enter Your Anniversary Date!")
        return
    
    if maritial_status_data =="married":
        if not get_valid_date(spouse_dob):
            messagebox.showerror("Error", "Invalid date format! Please enter in DD-MM-YYYY format.")
            spouse_entry.delete(0,tk.END)
            return
        if not get_valid_date(anniversary_date):
            messagebox.showerror("Error", "Invalid date format! Please enter in DD-MM-YYYY format.")
            anniversary_entry.delete(0,tk.END)
            return
    if not mpin:
        messagebox.showerror("Error", "Please enter your MPIN!")
        return
    
    if len(mpin) not in [4, 6]:
        messagebox.showerror("Error", "MPIN must be 4 or 6 digits!")
        mpin_entry.delete(0,tk.END)
        return
    
    if not mpin.isdigit():
        messagebox.showerror("Error", "MPIN must contain only numbers!")
        mpin_entry.delete(0,tk.END)
        return
        
    reasons = check_strength(mpin,dob,spouse_dob,anniversary_date)
    if reasons:
        strength_label.config(text="Strength : WEAK", fg='#dc2626')
        result_text.insert(tk.END, "Your MPIN is weak for the following reasons:\n")
        for i, reason in enumerate(reasons):
            result_text.insert(tk.END, f"{i+1}. {reason}\n")
        result_text.insert(tk.END, "\nPlease choose a different MPIN for better security.")
    else:
        strength_label.config(text="Strength : STRONG", fg='#16a34a')
        result_text.insert(tk.END, "Congratulations! Your MPIN is secure.\n\n")
        result_text.insert(tk.END, "Your MPIN is safe to use!")
        
        
        
        
# to clear all data at once
def clear_all_data():
    dob_entry.delete(0,tk.END)
    mpin_entry.delete(0,tk.END)
    spouse_entry.delete(0,tk.END)
    anniversary_entry.delete(0,tk.END)
    maritial_status.set("married")
    show_mpin.set(False)
    result_text.delete(1.0, tk.END)
    strength_label.config(text="")
    toggle_mpin_display()
    Marriage_field()
    
    

    

# Main Frame 
main_frame = tk.Frame(root,
                      bg="#1e3a8a")
main_frame.pack(fill='both',expand=True, 
                padx=20, pady=20)

# Header Frame
header_frame = tk.Frame(main_frame,bg='#3b82f6',relief='raised' , bd=2)
header_frame.pack(fill='x',pady=(0,10))

# Header Title and Sub Title
title_label = tk.Label(header_frame, text="WELCOME TO OUR BANK", font=('Arial', 25,"bold"),
                       fg='#f3f4f6',bg='#3b82f6')
title_label.pack()

sub_title_label = tk.Label(header_frame, text="MPIN Validator", font=('Arial', 15),
                           fg='#f3f4f6', bg='#3b82f6')  
sub_title_label.pack()

# Content Frame
content_frame = tk.Frame(main_frame,bg = "#f3f4f6",
                        relief='raised' , bd=2)
content_frame.pack(fill = 'x',pady=(10,5))
content_title_validation_label = tk.Label( content_frame,text="Kindly fill the Details:",
                                          font=("Arial",13,'bold'),fg="black")
content_title_validation_label.pack(pady='5',anchor='w')






# Input Frame
input_frame = tk.Frame(main_frame,bg = '#f3f4f6', relief='solid' , bd=2)
input_frame.pack(fill='x',padx=(0,10))






# DOB Frame and Input
dob_frame = tk.Frame(input_frame,bg = '#f3f4f6',relief='raised' , bd=2)
dob_frame.pack(fill='x',pady=(2,5))
dob_frame_label = tk.Label(dob_frame,text="Enter Your DOB in DD-MM-YYYY Format : ",
                           bg='#f3f4f6',fg='black',
                           font=("Arial",10,'bold') )
dob_frame_label.pack(anchor='w')
dob_entry = tk.Entry(dob_frame,relief='solid',font=("Arial",12),
                     fg='black',bg='white',bd='1')
dob_entry.pack(fill='x',pady=(1,2),padx=(4,20))






# Maritial Frame
maritial_frame = tk.Frame(input_frame,bg = '#f3f4f6',relief='raised' , bd=2)
maritial_frame.pack(fill='x',pady=(2,5))
maritial_frame_label = tk.Label(maritial_frame,text="Pls tell about your maritial status: ",
                                bg='#f3f4f6',fg='black',
                                font=("Arial",10,'bold'))
maritial_frame_label.pack(anchor='w')

maritial_status = tk.StringVar(value='married')


# Radio Frame
radio_frame = tk.Frame(maritial_frame,bg='#f3f4f6')
radio_frame.pack(anchor='w',pady=(0,5))
married_radio = tk.Radiobutton(radio_frame,text="Married",variable= maritial_status,
                               value="married",font=("Arial",10),
                               bg='white',fg='black')
married_radio.pack(side='left')
single_radio = tk.Radiobutton(radio_frame,text="Single",variable= maritial_status,
                              value="single",font=("Arial",10),
                              bg='white',fg='black')
single_radio.pack(side='left',padx =(40,0))


# Marriage Details Input Frame
marriage_frame = tk.Frame(maritial_frame,bg='#f3f4f6')

spouse_frame_label = tk.Label(marriage_frame,text="Pls Enter Your Spouse DOB in DD-MM-YYYY Format :",
                              bg='#f3f4f6',fg='black',
                              font=('Arial',10,'bold'))
spouse_frame_label.pack(anchor='w')
spouse_entry = tk.Entry(marriage_frame,relief='solid',font=("Arial",12),
                        fg='black',bg='white',bd='1')
spouse_entry.pack(fill='x', pady=(2,5),padx=(4,20))

anniversary_frame_label = tk.Label(marriage_frame,text="Pls Enter Your Anniversary Date in DD-MM-YYYY Format :",
                                   bg='#f3f4f6',fg='black',
                                   font=('Arial',10,'bold'))
anniversary_frame_label.pack(anchor='w')
anniversary_entry = tk.Entry(marriage_frame,relief='solid',font=("Arial",12),
                             fg='black',bg='white',bd='1')
anniversary_entry.pack(fill='x', pady=(2,5),padx=(4,20))


# Set weather to show Marrige Input Section or Not
def Marriage_field():
    if maritial_status.get() == 'married':
        marriage_frame.pack(fill='x')
    else:
        marriage_frame.pack_forget()

married_radio.config(command=Marriage_field)
single_radio.config(command=Marriage_field)
Marriage_field()





# MPIN Frame and Input
mpin_frame = tk.Frame(input_frame,bg = '#f3f4f6',
                      relief='raised' , bd=2)
mpin_frame.pack(fill='x')
mpin_frame_label = tk.Label(mpin_frame,text="Set Your New MPIN: ",
                            bg='#f3f4f6',fg='black',
                            font=("Arial",12,'bold'))
mpin_frame_label.pack(anchor='w')
mpin_entry = tk.Entry(mpin_frame,relief='solid',font=("Arial",12),
                      fg='black',bg='white',
                      bd='1',show='*')
mpin_entry.pack(fill='x',padx=(4,10))

show_mpin = tk.BooleanVar()


# Show MPIN CheckBox 
def toggle_mpin_display():
    if show_mpin.get():
        mpin_entry.config(show='')
    else:
        mpin_entry.config(show='*')
        
show_checkbox= tk.Checkbutton(mpin_frame,text='Show MPIN',variable=show_mpin,
                              command=toggle_mpin_display,font=('Arial', 9),
                              fg='#6b7280', bg='#f3f4f6')
show_checkbox.pack(anchor='w', pady=(5,0))





# Results section
result_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
result_frame.pack(fill='both', pady=(0, 10))

# Strength display
strength_label = tk.Label(result_frame, text="Strength : ", 
                         font=('Arial', 12, 'bold'), bg='white')
strength_label.pack(pady=5,anchor='w')

# Results text area
text_frame = tk.Frame(result_frame, bg='white')
text_frame.pack(fill='both', expand=True,
                padx=20, pady=(0, 10))
result_text = tk.Text(text_frame, height=8, font=('Arial', 10),
                     bg='#f8fafc', fg='#374151', relief='solid', bd=1,
                     wrap='word')
result_text.pack(fill='both', expand=True)
    
 
 
 
    
    
validate_button = tk.Button(main_frame, text="Validate MPIN", 
                       command=validate_inputs,font=('Arial', 12, 'bold'), 
                           bg="#10b981", fg='white', 
                           relief='raised', bd=2,
                           cursor='hand2')
validate_button.pack(pady=5,side="left",padx=10)


clear_button = tk.Button(main_frame,text='Clear Data', command=clear_all_data,
                         font=('Arial', 10), bg='#ef4444', 
                         fg='white',cursor='hand2')
clear_button.pack(pady=5,side="left",padx=20)


root.mainloop()

#*************************************FOR GUI INTERFACE WITH ALL REQUIRED FUNCTIONALITY ********************************************