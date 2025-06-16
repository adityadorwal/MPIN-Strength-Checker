#Check the Demographics by making the combination that can contain mpin and then check for it.
def check_demographics(date , mpin):
    dd,mm,yyyy = date.split("-")
    yy =yyyy[-2:]
    
    if(len(mpin) == 4):
        date_combination = [dd+mm,mm+dd,yy+mm,mm+yy,dd+yy,yy+dd,yyyy]
        if mpin in date_combination:return(True)
    else:
        date_combination = [dd+mm+yy,mm+dd+yy,yy+dd+mm,yy+mm+dd,yyyy+mm,mm+yyyy,dd+yyyy,yyyy+dd]
        if mpin in date_combination:return(True)
    return(False)
        
    