# NXOpen-CAE-python

>NOTE: Please look at the python package [nxopentse](https://github.com/theScriptingEngineer/nxopentse). It allows to use the code directly as an import.

>I'm no longer adding new stuff and will delete this repository in the future, when all code has been tranferred to nxopentse

This is a repository with NXOpen code for Siemens Simcenter3D (aka NX CAE) in python.
At this moment it mirrors the [C# repository](https://github.com/theScriptingEngineer/NXOpen-CAE)

If you’re using my scripts in your daily work, saving you a lot of work and time, buy me a coffe so I can continue developing awesome scripts.
[Buy me a coffe](https://www.buymeacoffee.com/theScriptingEngineer)

## Learning NXOpen

If you are interested in learning NXOpen, please check out my course on Udemy:

[Siemens NX beginner NXOpen course (Python)](https://www.udemy.com/course/siemens-nx-beginner-nxopen-course-python/?referralCode=DEE8FAB445765802FEDC)

[SimCenter 3D basic NXOpen course (C#)](https://www.udemy.com/course/simcenter3d-basic-nxopen-course/?referralCode=4ABC27CFD7D2C57D220B%20)

**use NXOPEN_PYTHON_JUL24 or NXOPEN_SIMCENT_JUL24 for discount on my Udemy courses (valid till July 30th 2024)**
>Note this course is in C#, but will teach you the basics, which you can also apply to python
>The difficulty with learning NXOpen is understanding the NX objects structure, not the language in which the code is written.
>Moreover, Siemens advises agains using Python if you are starting with NXOpen.


## Using intelligent code completion (aka intellisense) for NXOpen in python

One of the advantages of python is that it is dynamically typed. The consequence is that the IDE (eg. PyCharm, VSCode) does not know
the object type of the variable.
While writing NXOpen code in python I found this a huge disadvantage, because during coding I rely heavily on code completion (aka intellisense)
to know the available methods on the objects.
Apart from an older document from siemens explaining how to get this to work with Eclipse and PyDev add-on, which only works partially, I'm not aware of any other resource to get code completion to work.

This is why I created my own stub files for the NXOpen libraries. 

### Visual Studio Code

Demo: [Code completion in python (VSCode)](https://youtu.be/ODsZF7x7UoQ)

From [this blog](https://www.emmanuelgautier.com/blog/enable-vscode-python-type-checking)

In VSCode go to settings.json (ctrl + P -> settings.json) 
or locate settings.json under the folder .vscode an add the following entry:
*"python.analysis.typeCheckingMode": "basic"*

In VSCode go to settings.json (ctrl + P -> settings.json) 
or locate settings.json under the folder .vscode an add the following entry:

**"python.analysis.stubPath": "path_to_the_stub_files/Release2023/"**

Please contact me for a copy of the stub files.

Successful configuration should give no errors after opening **intellisense.py** (might need to restart VSCode)

### PyCharm

Demo: [Code completion in python (PyCharm)](https://youtu.be/468SGBALQQM)

Add the location of the stub files to the interpreter path. Instructions on how to do this can be found [here](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-reloading-interpreter-paths.html)

Please contact me for a copy of the stub files.

## Local python environment

### Create a local environment

*python3 -m venv .venv*


### Activate local environment

*source .venv/bin/activate*


### set the vs code interpreter to local environment, so locally installed packages are visible and work with intellisense

locate settings.json under the folder .vscode an add the following entry:
*"python.defaultInterpreterPath": ".venv/bin/python"*