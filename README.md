## Introduction :scroll:
This is a updated version of my equation solver GUI (click [ here ](https://github.com/gsc2001/Equation_solver_GUI-beta)).
I was not at all happy with the old style look of tkinter.

![old](/images/old.png)

Therefore decided to make a better GUI so I updated that to this

![new](/images/newg.png)

## Making :hammer:
I was just lazy to write the c++ implemented base code to write again in python :grin:. So surfed about it and got to know about **SWIG**.
Surfed about it a lot and finally was able to convert my c++ based code to a python library.

After that i created a disgusting GUI using tkinter ([ link ](https://github.com/gsc2001/Equation_solver_GUI-beta) to repository).

Wanted to create modern day GUI.
So, learnt a bit about **ElectronJS** and combined it with flask in python to create this GUI.

## Installation of dependicies :file_folder:
This GUI works smoothly on Linux/MacOS only till now. Will update it soon to run on windows.

Just download and extract the whole repository . Go there in terminal and type following commands

```bash
  $ bash install.sh
```
This script will install all the dependicies

##### Note:

You need to have nodejs and python3 installed on your system.    
* To install nodejs go [ here ](https://nodejs.org/en/download/)
* Linux usually comes installed with python3. Type following to check
  ```bash
  $ python3 --version
  ```
  if version >= 3.6 its good to go :+1:.
  Else if less or no version is shown install/update python3.   
  To install python3 type following
  ```bash
  $ sudo apt-get update
  $ sudo apt-get install python3
  ```


## Running :runner:
To start application, just type this in terminal after going to the extracted folder

```bash
  $ bash run.sh
```

### Contact :pencil2:
Your suggestion/issues are welcome at

:email: gurkirat.singh@students.iiit.ac.in
