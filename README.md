# back_door
Python back door for persistence

This script was written as part of the Red Siege python project. It provides a reverse shell or bind shell for use on a Linux or Windows target to establish persistence. After compromising a target copy the python script over and set it to run automatically at desired interval or on system bootup to reestablish shell.

Options are -l for Linux, -w for Windows, -r for reverse shell, and -b for bind shell.

Set RHOST and RPORT variables in script for reverse shell. Set LHOST and LPORT variables for bind shell.

useage: python bd.py -l -r
        python bd.py -l -b
        python bd.py -w -r
        python bd.py -w -b
        
Linux reverse shell  
![image](https://user-images.githubusercontent.com/84335647/160510454-061317ad-4335-4de5-8d0c-8c1c97149c2c.png)

![image](https://user-images.githubusercontent.com/84335647/160510522-141938e7-5d9f-4d64-ace8-0b1457d0e9ad.png)

Linux Bind shell  
![image](https://user-images.githubusercontent.com/84335647/160510581-1b4b1732-c21b-4a0f-b30e-9c94d06dca0e.png)

![image](https://user-images.githubusercontent.com/84335647/160510606-06c8cd61-a79d-462d-9145-fe9de5cd5756.png)

Windows reverse shell  
![image](https://user-images.githubusercontent.com/84335647/160510672-ac8843ca-46b9-4d25-b88f-009c2b71069c.png)

![image](https://user-images.githubusercontent.com/84335647/160510709-528af2eb-0c87-4a48-8aac-b6a25ac7a5bc.png)

Windows bind shell  
![image](https://user-images.githubusercontent.com/84335647/160510755-ca03abc4-d0c1-4e07-a9d4-abccb94a0318.png)

![image](https://user-images.githubusercontent.com/84335647/160510792-0b358ce2-f3de-4544-8fa2-1395f0c2d0af.png)


To do:
add functionality for Windows API calls and encrypted shellcode
