# SIP - The markup language for Tk
SIP is a python interpreter that turns your xml into a Tk window. It also includes MySQL and some logic, as well as the
ability to write python code.
# Getting started
This is a tutorial on how to get started with SIP.
## Dependencies
You will need python 3.0 or newer, SIP CLI (duh!) and these packages:
1. xml
2. json
3. tkinter
4. mysql-connector-python

To get these packages, follow these steps:
1. (MacOS X and Windows): Download the python package for your system
2. Download the SIP CLI version for your system from the releases page
3. (Linux): Open a terminal in the CLI directory, and run `sudo cp . /bin/`
    * (MacOS X): Open a terminal in the CLI directory, and run `sudo cp . /usr/bin`
4. (MacOS X and Linux): Run `sip install` in a terminal
    * (Windows): Run `[Path-to-CLI]/sip.bat install`

You're all set!
## Example
The example (in master/example/) is an example of a SIP app with just about all of the features in use. Download it, play with it,
and use the docs for help. To run it, run `python3 sip.py`
## Time to start!
To start, run "sip init" on MacOS X and Linux, or "[Path-to-CLI]/sip.bat init" on Windows. Fill in the name of your project,
in this case tutorialapp, its parent directory and the path to the executable of your favorite code editor. It will make you
two nice, empty files: index.xml and config.json. Let's start with config.json. It will specify the location of your entry file.
Here is what it should look like:
```
{
  "path": "index.xml"
}
```
Now, index.xml. That is where all of your view code goes, and some of your logic. That should look like this to start:
```
<!DOCTYPE sip>
<window width="500" height="500">
  <info>
    <title>An app</title>
  </info>
  <view>
    
  </view>
  <logic>
    
  </logic>
</window>
```
First, let me explain what these tags mean. `<!DOCTYPE sip>` just means that this is a SIP document. The window does just
what it says. It makes a window. It is necessary to create an app. Then, the categories: info, view and logic. Info contains
all the info about the window; View contains any view components; And logic contains the logic like executing bash files,
connecting to sql databases and running python files and functions. Now, let's get into coding! Let's just add a button:
```
<Button name="button1" side="left">Click Me!</Button>
```
and run the app with `sip run [path-to-project]` or `[path-to-CLI]/sip.bat run [path-to-project]`. You should see a button
that says "Click Me!" Good job! You made your first project! Now go read the docs, and learn SIP!
