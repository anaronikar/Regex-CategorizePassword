''' 
Python program to categorize password
as strong or weak using Regex 
'''  

# importing the module for regular expressions  
import re
  

def password(x):
   
    # ensuring that the password is not a newline or space
    if x == "\n" or x == " ":
        return "WARNING : password cannot be a newline or space!"
   
    # ensuring that the password length is in between 9 and 20
    if 9 <= len(x) <= 20:
        # checks if a character occurs three or more times in a row
        if re.search(r'(.)\1\1', x):
            return "WEAK Password : same character repeats three or more times in a row"
   
        # checks if the same string pattern is occurring
        if re.search(r'(..)(.*?)\1', x):
            return "WEAK Password : same string pattern repetition"
   
        else:
            return "STRONG Password!"
    

    # ensures that the password is between 9 to 20 characters only
    else:
        return "WARNING : length of password must be 9-20 characters only."
  

def main():
   
   val = input("\nEnter the password : ")
   print(password(val))
   

if __name__ == '__main__':
    main()




''' 

Instructions for execution:-
> On compiling and running the code, the user will be asked to enter a password.
> The user must enter a password of length 9 to 20 characters only, when the aboxe message is displayed.
> Entered password cannot be newline or a space character.
> When a password is entered, a warning message is displayed in case it is haxing a repetition of same characters 3 
or more times in the same row.
> When a password is entered, a warning message is displayed in case there is repetition of the same string pattern. 
> Depending on the satisfaction of the aboxe conditions, on entering a password, an appropriate message is going to 
be displayed.



Examples of outputs:-

1)  Enter the password : Xqqa$&nop8
    STRONG Password!

2)  Enter the password :
    WARNING : password cannot be a newline or space!

3)  Enter the password : 1j2nCh
    WARNING : length of password must be 9-20 characters only.

4)  Enter the password : Yyyasdxjyppsd
    WEAK Password : same string pattern repetition

5)  Enter the password : 119$hs821
    STRONG Password!

6)  Enter the password : aaanxIDo29$73&
    WEAK Password : same character repeats three or more times in a row

7)  Enter the password : 3010appy
    WARNING : length of password must be 9-20 characters only.

'''