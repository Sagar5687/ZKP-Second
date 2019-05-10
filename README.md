# ZKP
ZKP login python scripts

1st - register a user name and password with reg.py
2nd - logon the server with login.py
3rd - Authorise details with authorise.py


These scripts are used for a user password to be verified without the password being saved. The user is authorised using the username and the server checks for the a record of that username. Then the client must calulate a challenge provided by the server y value and the server makes a calculation with the y value and the record stored for that username. The result of each calculation should be the same showing that the client knows x value without sharing with the server. So the server has zero knowledge of the users text password.

A generator value is assigned as g 

A prime number is assigned as n

Other g and n files with different bit size of numbers are present in the server values folder. for example n8.txt is a 8 bit number.

Y is set as the servers verifier. The value of why is the word "verify" is hashed using the sha 256 function and then the hexidecimal hash converted to decimal.

The "reg" script asks the user to register a user name and password. The password the user chooses is then hashed using sha 256 and the hexidecimal hash is then converted into decimal. The Generator value is then raised to the power of the password hash in decimal format and then modded by the prime number(secretvalue). This is the value saved by the server in a text file named after the username and from this value it is too difficult to compute the original password value.

The "login" script will then ask the user to enter the username they entered when registering. This allows the logon script to find the file stored on the server for that user. The login script then takes the password value x from the client and the y value from the server to calculate val1=g^(x+r)%(p-1) mod n. It then solves the server challenge of g^y mod n (c). These calculations are then saved on the server. 

The "authorise" script then takes these values and calculateds c*secretvalue mod n. This sum should match val1 caluclated previousey. If the value matches then the sensitive data is revealed. If the values have been moddified since the original registration then access will be denied. 

It can be observed from the server file that the x value of the password is not present but the client has proved they know the x value with out sharing. This is zero knowledge proof.
