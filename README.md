## *0x00. AirBnB clone - The console*

`Group project`   `Python`   `OOP`

By: Guillaume

![65f4a1dd9c51265f49d0](https://github.com/mohammedchakir/AirBnB_clone/assets/129831433/3374971c-c9b8-4f63-a03f-50a340f7d699)

## *Description of the project:*

In the initial phase of the Airbnb clone project, we developed the backend, integrating it with a Python console application using the cmd module. 
Data, represented as Python objects, is stored in a `json` file and retrievable through the `json` module.

## *Description of the command interpreter:*

The application's interface closely resembles the `Bash shell`, with the key distinction being that it only recognizes a specific set of commands designed exclusively for interacting with the AirBnB website.

The command line interpreter functions as the user interface for the web application, allowing users to engage with the backend, which was crafted using Python's object-oriented programming principles. Some of the commands available are:

- `show`
- `create`
- `update`
- `destroy`
- `count`

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

## *How to start it:*

These guidelines will assist you in obtaining and setting up a version of the project on your local machine, intended for development and testing purposes.

## *Installing:*

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```
git clone https://github.com/mohammedchakir/AirBnB_clone.git)
```

After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.
As:

> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a `JSON` file and deserializes `JSON` file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from `BaseModel`
> 
>models/state.py: State class that inherits from `BaseModel`
>
>models/city.py: City class that inherits from `BaseModel`
>
>models/amenity.py: Amenity class that inherits from `BaseModel`
>
>models/place.py: Place class that inherits from `BaseModel`
>
>models/review.py: Review class that inherits from `BaseModel`


## *How to use it:*

It may work in two different modes:

1- Interactive mode:

The console will present a prompt (hbnb), signaling that the user can input and execute a command, Once the command is executed, the prompt reappears, awaiting a new command. This cycle can continue indefinitely unless the user chooses to exit the program.
```
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

2- Non-interactive mode:

The `shell` will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.
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

## *Format of Command Input:*

In order to give `commands` to the console, these will need to be piped through an echo in case of  **Non-interactive mode**.

In  **Interactive Mode**  Commands are entered using the keyboard when the prompt is displayed and are recognized upon pressing the enter key (new line). Upon doing so, the console will endeavor to execute the command through various methods or will display an error message if the command fails. To exit this mode, you can use the `CTRL + D` combination, `CTRL + C`, or enter the commands `quit` or `EOF`.

## *Arguments:*

Most `commands` have several options or arguments that can be used when executing the program. In order for the `Shell` to recognize those parameters, the user must separate everything with `spaces`.

Example:

```

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

```

or

```
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
```

## *Available commands and what they do:*

The recognizable `commands` by the interpreter are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |








-----------------
## Collaborators:

[MOHAMMED CHAKIR](https://github.com/mohammedchakir) & [SALEH ELMOUINY](https://github.com/Elmouinysaleh)
