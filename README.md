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

![image](https://user-images.githubusercontent.com/53118499/210207478-86a55911-d2c5-467b-bf60-4b8a5f53507d.png)

2. Login with default username and Password ```Admin@google.com``` and ```Admin```.

3. Choose ```Absen Masuk```, the fullfil the data.

Example :

4. Choose ```Submit``` to input data to the database,  then choose ```KembaliLogin``` for Logout.

# How to See the Data

1. To see ```Absen Masuk``` data .. check it on table ```db_absen_masuk```. or use this query :

```
SELECT * FROM db_absen_masuk;
```

2. To see ```Absen Kelur``` data .. check it on table ```db_absen_keluar```. or use this query :

```
SELECT * FROM db_absen_keluar;
```

3. To see ```Sign Up``` data or data for ```log In``` .. check it on table ```db_user```. or use this query :

```
SELECT * FROM db_user;
```

# How to Update the Data

1. Install dbeaver first

2. See data table on menu ```data```. Update the data then save with choose ```save``` or ```ctrl + s```.