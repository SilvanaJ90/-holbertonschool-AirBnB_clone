# AirBnB clone - The console #

![This is an image](https://repository-images.githubusercontent.com/520063788/a91abf2d-82e3-40e6-96d7-75043c684ff3)

## Table of Contents

- [Description of the Project](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#description-of-the-project/)
- [Description of the command interpreter](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#description-of-the-command-interpreter).
- [How to Start It](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#how-to-start-it)
- [How to Use It](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#how-to-use-it)
- [Examples](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#examples)
- [Authors](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/README.md#authors).


## Description of the Project

**First step: Write a command interpreter to manage your AirBnB objects.**

This is the first step towards building your first full web application: the **AirBnB clone.** This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… 

Each task is linked and will help you to:

    - put in place a parent class (called BaseModel) to take care of the initialization, serialization and          deserialization of your future instances
    - create a simple flow of serialization/deserialization:
        - Instance <-> Dictionary <-> JSON string <-> file
    - create all classes used for AirBnB that inherit from BaseModel
        - User
        - State
        -City
        - Place ..
    - create the first abstracted storage engine of the project: 
        - File storage.
    - create all unittests to validate all our classes and storage engine

## Description of the command interpreter

The console will be used for access of the functionalities offered by our components.
In our case, we want to be able to manage the objects of our project:

    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc…
    - Do operations on objects (count, compute stats, etc…)
    - Update attributes of an object
    - Destroy an object

## How to Start It
Execution
```
Your shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

### Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:
The console

    create your data model
    manage (create, update, destroy, etc) objects via a console / command interpreter
    store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![This is an image](https://github.com/Giogap/holbertonschool-AirBnB_clone/blob/main/Img/imagen_proyect.png)

## How to Use It

| Command | Description |
| --- | --- |
| help | The help command is a command prompt,  command that's used to provide more information on another command. |
| EOF | Exit the program. |
| quit | Exit the program. |
| create | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel. |
| show | Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234. |
| destroy | Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234. |
| all | Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all. |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". |


## Examples

Commad:

help:
```
./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```


quit and EOF:
```
./console.py 
(hbnb) help quit
Quit command to exit the program
(hbnb) help EOF
Quit command to exit the program
(hbnb) quit
```

create:
```
./console.py 
(hbnb) create BaseModel
bb711919-2e80-4ce2-85aa-454484f89013
(hbnb) 
```

show:
```
./console.py 
(hbnb) show BaseModel bb711919-2e80-4ce2-85aa-454484f89013
[BaseModel] (bb711919-2e80-4ce2-85aa-454484f89013) {'id': 'bb711919-2e80-4ce2-85aa-454484f89013', 'created_at': datetime.datetime(2022, 10, 29, 18, 31, 52, 943770), 'updated_at': datetime.datetime(2022, 10, 29, 18, 31, 52, 943843)}
(hbnb)
```

destroy:
```
./console.py 
(hbnb) destroy BaseModel bb711919-2e80-4ce2-85aa-454484f89013
(hbnb)
```

all:
```
./console.py 
(hbnb) all BaseModel
["[BaseModel] (24a40c4d-d6b9-4d48-999e-033a3dcf3e59) {'id': '24a40c4d-d6b9-4d48-999e-033a3dcf3e59', 'created_at': datetime.datetime(2022, 10, 28, 15, 42, 50, 756172), 'updated_at': datetime.datetime(2022, 10, 28, 15, 42, 50, 756225)}", "[BaseModel] (5acb1f7f-386a-473a-9b45-b68a01a33fb9) {'id': '5acb1f7f-386a-473a-9b45-b68a01a33fb9', 'created_at': datetime.datetime(2022, 10, 28, 16, 8, 56, 496681), 'updated_at': datetime.datetime(2022, 10, 28, 16, 8, 56, 496725)}", "[BaseModel] (0079d3d4-9527-44ba-92be-2f15061964ad) {'id': '0079d3d4-9527-44ba-92be-2f15061964ad', 'created_at': datetime.datetime(2022, 10, 29, 18, 31, 30, 922270), 'updated_at': datetime.datetime(2022, 10, 29, 18, 31, 30, 922286)}"]
(hbnb) 
```

update:
```
./console.py 
(hbnb) create BaseModel
683382c7-0351-4249-8987-ce2c42c0f1df
(hbnb) update BaseModel 683382c7-0351-4249-8987-ce2c42c0f1df first_name "Betty"
(hbnb) show BaseModel 683382c7-0351-4249-8987-ce2c42c0f1df
[BaseModel] (683382c7-0351-4249-8987-ce2c42c0f1df) {'id': '683382c7-0351-4249-8987-ce2c42c0f1df', 'created_at': datetime.datetime(2022, 10, 29, 18, 39, 5, 144900), 'updated_at': datetime.datetime(2022, 10, 29, 18, 39, 5, 144949), 'first_name': '"Betty"'}
```


## Authors
### This file lists all individuals having contributed content to the repository.
- Giovanni Pérez <5187@holbertonstudents.com>
- Silvana Jaramillo <5211@holbertonstudents.com>

