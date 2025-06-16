def commonly_used(mpin):
    
    # For Mpin's[1111,2222,3333.....]
    def all_digits_same(mpin):
        for i in mpin:
            if(i!=mpin[0]):
                return(False)
        return(True)
    
    # For Mpin's[123456,8901,5678]
    def ascending_sequential_digits(mpin):
        initial = int(mpin[0])
        for i in mpin:
            if(initial != int(i)):return(False)
            initial = (initial+1)%10
        return(True)
    
    # For Mpin's[8765,2109,543210]
    def descending_sequential_digits(mpin):
        initial = int(mpin[0])
        for i in mpin:
            if(initial != int(i)):return(False)
            initial = (initial-1)%10
        return(True)
    
    # For Mpin's[1212,454545......]
    def digits_pattern(mpin):
        length=len(mpin)
        divide=2
        while(divide<4):
            for i in range(2,len(mpin),divide):
                if(mpin[0:2]!=mpin[i:i+2]):return(False)
            divide+=1
        return(True)
    
    # For Mpin's[1221,123321,....]
    def digits_palindrome(mpin):
        divide = int(len(mpin)/2)
        a=mpin[:divide]
        b=mpin[-1:-divide-1:-1]
        return(a==b)
    
    # For Mpin's[1122]]
    def set_same_digits(mpin):
        length=len(mpin)
        divide=2
        while(divide<4):
            for i in range(0,length,divide):
                if(mpin[i]!=mpin[i+1]):return(False)
            if(length==4):break
            divide+=1
        return(True)
              
                   
      
    # Calling all the fuctions to check wether it is a commonly used MPIN or not    
    if (all_digits_same(mpin) or
        ascending_sequential_digits(mpin) or
        descending_sequential_digits(mpin) or
        digits_pattern(mpin) or
        digits_palindrome(mpin) or
        set_same_digits(mpin)
    ):
        return True
    else:
        return False
        