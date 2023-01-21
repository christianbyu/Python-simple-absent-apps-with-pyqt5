# Simple-absent-apps-with-pyqt5

# Dependencies

- python 3.9.13
- pyqt5
- sqlite3

# Tools
- Visual Studio Code
- QT Designer
- Dbeaver

# Installation

1. Install the pyqt5 using pip

```
pip install pyqt5
```

2. Install pyqt5-tools using pip

```
pip install pyqt5-tools
```

3. Install pyqt5 Extension on VSCode

![image](https://user-images.githubusercontent.com/53118499/209476849-88f2b062-e953-493b-a76e-880390ebe19c.png)

# How to Use

1. run ```main.py``` file, and you can get display like this ....

![image](https://user-images.githubusercontent.com/53118499/210570072-3ed3c886-8302-4477-9d07-1dc49fbf1c2c.png)

2. Login with default username and Password ```Admin@google.com``` and ```Admin```.

![image](https://user-images.githubusercontent.com/53118499/210569546-02f08d4c-71f1-4480-9f8e-207b24996d40.png)


3. Choose ```Absen Masuk``` or ```Absen Masuk```, then fullfil the data.

![image](https://user-images.githubusercontent.com/53118499/210569598-ed1f10c6-fc59-4211-a2ec-1a8cc5bad0a2.png)

![image](https://user-images.githubusercontent.com/53118499/210569720-4a2c0ebb-6e96-4471-b212-6b36bd004ebb.png)

- Result on database :

![image](https://user-images.githubusercontent.com/53118499/210569924-af6d6edb-9631-4760-a801-f00195652190.png)

Data succesfully submitted!

4. Choose ```Submit``` to input data to the database,  then choose ```KembaliLogin``` for Logout.

![image](https://user-images.githubusercontent.com/53118499/210569788-16a00e5e-7808-428f-9a75-d77c215211c9.png)


5. If you want to add new account go to ```Sign Up``` Menu, after you logout or close the apps the run again the ```main.py```.

![image](https://user-images.githubusercontent.com/53118499/210570148-f2f15968-f9e9-4caf-822c-e0edf730a2eb.png)

- Fullfill data for login information, then ```Sign Up```. And you will back to login menu.

![image](https://user-images.githubusercontent.com/53118499/210570214-412abacd-cdc9-4ebb-8f08-9c82c4860141.png)

- Result on database :

![image](https://user-images.githubusercontent.com/53118499/210570455-f593f72a-c067-4ea4-b084-bdad8fbc1c88.png)

Data succesfully submitted!



# How to See the Data

1. To see ```Absen Masuk``` data .. check it on table ```db_absen_masuk```. or use this query :

```
SELECT * FROM db_absen_masuk;
```

2. To see ```Absen Keluar``` data .. check it on table ```db_absen_keluar```. or use this query :

```
SELECT * FROM db_absen_keluar;
```

3. To see ```Sign Up``` data or data for ```log In``` .. check it on table ```db_user```. or use this query :

```
SELECT * FROM db_user;
```

# How to Update the Data

1. Install dbeaver first.

2. Connect to Database.

2. See data table on menu ```data```. Update the data then save with choose ```save``` or ```ctrl + s```.

    Example :
    
    - Before
    
    ![before_1](https://user-images.githubusercontent.com/53118499/210569316-63ee87a5-b046-4f39-938f-9ed2a209a92a.png)

    - After

    ![image](https://user-images.githubusercontent.com/53118499/210569240-e8754782-c382-48f2-84ad-c87e595202d0.png)
