# ZKP
ZKP login python script

This script is used for a user password to be verified without the password being saved. The user is then authorised usin the password but the password is not needed to be keeped by the server. So the server has zero knowledge of the users text password.

A generator value is assigned as g 

A prime number is assigned as n

Y is set as the servers verifier. The value of why is the word verify hashed using the sha 256 function and then the hexidecimal hash converted to decimal.

The script asks the user to register a password. The password the user chooses is then hashed using sha 256 and the hexidecimal hash is then converted into decimal. 

The Generator value is then raised to the power of the password hash in decimal format and then modded by the prime number. 
This is the value saved by the server in the x variable and from that value it cannot compute the original password.

When the user enters a password for verification the password is then hashed using sha256 then the hexidecimal value is then converted to decimal and the decimal value is assigned to the a variable.

The v variable is the result of the server taking the g value and raising it to the power of the y value and moding by n.

The server then takes the saved password value of x raises it to the power of y and modded by n. this value is assigned to the m1 varible.

The v variable is then raised to the power of the a variable from the entered password and then modded by n. This value is assigned the m2 varible.

if the m1 and m2 variable match then it is clear that the password entered by the user matches the password initially registered. If the values do not match then the entered password is not calulating the same value as the password registered.
