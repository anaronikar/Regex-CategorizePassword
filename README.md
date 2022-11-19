# Regex-CategorizePassword
A python program to <b>categorize passwords as strong or weak</b>, using the concepts of <b>Regular Expression</b>(Regex).

### Instructions for execution:-

> On compiling and running the code, the user will be asked to enter a password.

> The user must enter a password of length 9 to 20 characters only, when the aboxe message is displayed.

> Entered password cannot be newline or a space character.

> When a password is entered, a warning message is displayed in case it is having a repetition of same characters 3 
or more times in the same row.

> When a password is entered, a warning message is displayed in case there is repetition of the same string pattern. 

> Depending on the satisfaction of the aboxe conditions, on entering a password, an appropriate message is going to 
be displayed.

### Examples of various possible outputs:-

1.  Enter the password : Xqqa$&nop8 <br>
    STRONG Password!

2.  Enter the password : <br>
    WARNING : password cannot be a newline or space!

3.  Enter the password : 1j2nCh <br>
    WARNING : length of password must be 9-20 characters only.

4.  Enter the password : Yyyasdxjyppsd <br>
    WEAK Password : same string pattern repetition

5.  Enter the password : 119$hs821 <br>
    STRONG Password!

6.  Enter the password : aaanxIDo29$73& <br>
    WEAK Password : same character repeats three or more times in a row

7.  Enter the password : 3010appy <br>
    WARNING : length of password must be 9-20 characters only.
