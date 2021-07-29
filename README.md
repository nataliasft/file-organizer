# Simple File Organizer
*Created using python 3.9.2*

## About
A simple python script that organizes files to folders by their name. 

![image](https://user-images.githubusercontent.com/63284781/127433328-cada252f-8e4c-4b7d-a5be-c32b73f80962.png)

For the example, I have files like this and want to organize them into a folder by their name. That is Lesson 1, Lesson 2,..., Lesson 25. 

## Library
This code requires [python](http://www.python.org/) 3.6+ installed and the following Python libraries is used:
* [RegEx](https://docs.python.org/3/library/re.html)
* [pathlib](https://docs.python.org/3/library/pathlib.html)
* [os](https://docs.python.org/3/library/pathlib.html)

## How to Use
#### Modify the file path
Modify the code in line 5 based of the directory of your file.
```python 
files_path = Path('YOUR_FILE_PATH')
```

Example:
```python 
files_path = Path('/Users/natal/Documents/Cakap Intermediate Business English')
```

#### Modify folder name.
Based on your file, you can change the folder name by modifying these code in line 13. 
```python
folder_name = re.split(r'YOUR_REGEX', name)[0]
```

In this example, the files named with pattern "Lesson X.X. XXX", and the folder I want to create is "Lesson X". 
```python
folder_name = re.split(r'\.', name)[0]
```

#### Run and Execute
Finally save the file, then run and execute the script. For example in the command prompt run:
```cmd
python file-organizer.py
```

## Example Result
![image](https://user-images.githubusercontent.com/63284781/127435041-6b06866a-7c71-41af-b021-5e1a76526d98.png)
