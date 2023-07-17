# NXOpen-CAE-python

This is a repository with NXOpen code for Siemens SimCenter 3D (aka NX CAE) in python.
At this moment it mirrors the [C# repository](https://github.com/theScriptingEngineer/NXOpen-CAE)

## Learning NXOpen

If you are interested in learning NXOpen, please check out my course on Udemy:
[SimCenter 3D basic NXOpen course (C#)](https://www.udemy.com/course/simcenter3d-basic-nxopen-course/?referralCode=4ABC27CFD7D2C57D220B%20)

**30% off with coupon code REALIZELIVE (valid till July 29th 2023)**
>Note this course is in C#, but will teach you the basics, which you can also apply to python
>The difficulty with learning NXOpen is understanding the NX objects structure, not the language in which the code is written.
>Moreover, Siemens advises agains using Python if you are starting with NXOpen.


## Using intelligent code completion (aka intellisense) for NXOpen in python

One of the advantages of python is that it is dynamically typed. The consequence is that the IDE (eg. PyCharm, VSCode) does not know
the object type of the variable.
While writing NXOpen code in python I found this a huge disadvantage, because during coding I rely heavily on code completion (aka intellisense)
to know the available methods on the objects.
Apart from an older document from siemens explaining how to get this to work with Eclipse and PyDev add-on, which only works partially, I'm not aware of any other resource to get code completion to work.

This is why I created my own method (a work in progress, not perfect but still handy) which is  independent from the IDE you are using.
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