# Python_HeidelTime
This projects implements a Python Wrapper for the temporal tagger [HeidelTime](https://github.com/HeidelTime/heideltime). To achieve that, it makes use of the HeidelTime-standalone program.

## Installation
To use Python_HeidelTime, it is necessary to install HeidelTime-standalone first. A current download can be found on their [releases page](https://github.com/HeidelTime/heideltime/releases). At the point of the development of this project, version 2.2.1 was the most current one. Support for newer or older versions is not guaranteed. An detailed description of the installation process is found in the [HeidelTime Standalone Manual](https://gate.ac.uk/gate/plugins/Tagger_GATE-Time/doc/HeidelTime-Standalone-Manual.pdf)

For usage in Python, it is sufficient to specify the installation directory of HeidelTime-standalone in the config_Heideltime.py. Please notice that the path to Heideltime-standalone has to specified as a string object.

When using Python_HeidelTime, please cite also HeidelTime itself as stated on their [project page](https://github.com/HeidelTime/heideltime).

## Usage
The main class of Python_HeidelTime is simply called Heideltime and is initialized without any parameters.
All paramaters x can be specified by the set_x methods. Typically, they are named as described in the [HeidelTime Standalone Manual](https://gate.ac.uk/gate/plugins/Tagger_GATE-Time/doc/HeidelTime-Standalone-Manual.pdf). The correct use of all parameters is also given in the manual. When certain parameters are renamed, it is stated so in the source code.

After initialization, a text can be parsed by the parse function by passing the argument as a string object.

The following code snippet works a simple example.

'''python
heideltime_parser = Heideltime()
heideltime_parser.set_document_type('NEWS')
print(heideltime_parser.parse('Yesterday, I bought a cat! It was born earlier this year.'))
'''

Which should result in the following output.

'''
<?xml version="1.0"?>
<!DOCTYPE TimeML SYSTEM "TimeML.dtd">
<TimeML>
<TIMEX3 tid="t1" type="DATE" value="2019-06-13">Yesterday</TIMEX3>, I bought a cat! It was born <TIMEX3 tid="t3" type="DATE" value="2019" mod="START">earlier this year</TIMEX3>.
</TimeML>
'''
