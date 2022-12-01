# NXOpen-CAE-python

This is a repository with NXOpen code for Siemens SimCenter 3D (aka NX CAE) in python

If you are interested in learning NXOpen, please check out my course on Udemy:
>Note this course is in C#, but will teach you the basics, which you can also apply to python
>The difficulty with learning NXOpen is understanding the NX objects structure, not the language in which the code is written.
>Moreover, Siemens advises agains using Python if you are starting with NXOpen.
[SimCenter 3D basic NXOpen course (C#)](https://www.udemy.com/course/simcenter3d-basic-nxopen-course/?referralCode=4ABC27CFD7D2C57D220B%20)


## Using code completion (aka intellisense) for NXOpen in python

One of the advantages of python is that it is dynamically typed. The consequence is that the IDE (eg. PyCharm, VSCode) does not know
the object type of the variable.
While writing NXOpen code in python I found this a huge disadvantage, because during coding I rely heavily on code completion (aka intellisense)
to know the available methods on the objects.
Apart from an older document from siemens explaining how to get this to work with Eclipse and PyDev add-on, I'm not aware of any other resource to get code completion to work.
This is why I created my own method (a work in progress, not perfect but still handy) which is  independant from the IDE you are using.
You can find more information on how to set this up using this link (coming soon)
[Code completion in python](https://youtu.be/HwKNArNo4FI)


## Type checking in VSCode
From [this blog](https://www.emmanuelgautier.com/blog/enable-vscode-python-type-checking)

In VSCode go to settings.json (ctrl + P -> settings.json) 
or locate settings.json under the folder .vscode an add the following entry:
*"python.analysis.typeCheckingMode": "basic"*

## Local python environment
### Create a local environment

*python3 -m venv .venv*

### Activate local environment

*source .venv/bin/activate*


### set the vs code interpreter to local environment, so locally installed packages are visible and work with intellisense

locate settings.json under the folder .vscode an add the following entry:
*"python.defaultInterpreterPath": "\".venv/bin/python\""*