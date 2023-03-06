***Password Manager***  


*** What is it? ***  
    This is a simple password manager that allows you to store your passwords in a secure way.  
  
*** Why is it useful? ***  
    It is useful because it allows you to store your passwords in a secure way.  

*** How do I use it? ***  
    You need python 3.6 or higher to use this program.  
    You can run the program by typing the following command in the terminal:  
    ``` python password_manager.py ```  
    You can also run the program by typing the following command in the terminal:  
    ``` python3 password_manager.py ```  

*** Detailed Description ***  
    The program able to do the following things:  
    1. **Add Password for a site** *Adds username and password for a site and encrypts password*  
    2. **Update Password** *Updates the password for a site*  
    3. **Search Password** *Search for a site and displays the username and password*  
    4. **Delete Password** *Deletes entry for a site*  
    5. **List all records in the file** *Lists all the sites and their usernames and passwords*  
    6. **List all records with decrypted passwords** *Lists all the sites and their usernames and decrypted passwords*  
    7. **Exit**

***Enryption Mechanism***  
    This program uses a custom encryption mechanism to encrypt the passwords.  
    The encryption mechanism is based on the following algorithm:  
    1. **Generate a random key value pair** *Generates a random key, value pair for the encryption*  
    2. **Encrypt the password** *Encrypts the password using the key*  
    3. **Decrypt the password** *Decrypts the password using the key*  
  
    **KEY**  
    The key is a string with all ASCII characters, ASCII numbers, and few special characters.  

    **Random Integer**  
    The random integer *randomizer* is a number between 0 and length of *KEY*.  
    
    **VALUE**  
        The function ```random_value(key, randomizer)``` generates a random value with *KEY* and *randomizer* for the encryption.  
        The *Value* is a string with all ASCII characters, ASCII numbers, and few special characters but positively shifted by *Random Integer* and concatinated.  
     
    **Encryption Logic**  
        The dictonary ```encrypt(key, value)``` creates a dictonary with the *key* and *value*.  
        The key is the *KEY* and the value is the *VALUE* encrypted using the *KEY* and *Random Integer*.  

        The function ``` encode_password(password):``` encodes the password and returns the encoded password.
        This also genarates a *.key* file with encrypted password and *randomizer* used to encrypt the password.
        The use of *randomizer* is to regenerate the *key* and *value* for the decryption.
      
    **Decryption Logic**  
        The dictonary ```decrypt(key, value)``` creates a dictonary with the *key* and *value*.  
        The key is the *KEY* and the value is the *VALUE* decrypted using the *KEY* and *Random Integer*.  
        
        The function ``` decode_password(password):``` decodes the password and returns the decoded password.
        This also reads the *.key* file with encrypted password and *randomizer* used to encrypt the password.
        The use of *randomizer* is to regenerate the *key* and *value* for the decryption.

    **Example**
    The following is an example of the encryption and decryption of the password:
    ```  
    key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()'
    randomizer = 5
    value = random_value(key, randomizer) 
    Encyrpted Keys = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()abcde'
    ```                                                                                         
***Further Development***  
    This project is still in development.  
    The following features are planned for the future:  
    1. Master Password for the password manager. This helps to lock the password manager and restrict the access to the password manager.  
    2. GUI tool for the password manager. This will allow the user to use the password manager from the GUI.  
    3. Password manager for multiple users. This will allow the user to use the password manager for multiple users.  
    4. Create Password's file in specific location. This will allow the user to create the password file in specific location.  
    5. Create Password's file in secret location. This will prevent the user from accessing the password and encryption files.  