\\\\\\\\\\TEAM MEMBERS\\\\\\\\\\
Mogammed Ra-Eez Zardad
Mughtaar Gool

\\\\\\\\\\AIRBNB CLONE PROJECT\\\\\\\\\\
0x00. Airbnb clone - the console

In this project we will write a command interpreter to manage our Airbnb objects.

\\\\\\\\\\The following tasks will help and link our console by:\\\\\\\\\\

-put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization
of your future instances

-create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

-create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

-create the first abstracted storage engine of the project: File storage.
 
-create all unittests to validate all our classes and storage engine.

\\\\\\\\\\EXECUTION\\\\\\\\\\

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
But also in non-interactive mode: (like the Shell project in C)

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

