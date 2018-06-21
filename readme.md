

# TICT-V1IPASS-15


A simple log file analyser written for the IPASS project at the Hogeschool Utrecht, The Netherlands.

Functions of the log analyser:

- Show failed downloads due missing file
- Show a top 10 of the most downloaded files on the server
- Show a list of different clients who have connected, including:
    - The amount of connections
    - The amount of downloaded bytes per client
    - Used anonymous password (if username was anonymous)

- Using the log analyser in interactive and non interactive mode
    - Non interactive mode will use command line arguments for navigating 

## Getting Started


### Prerequisites


The script is written in Python 3.6 and uses only one module that is not included with Python by default. 
The script wil attempt to download and install this module if it is not installed yet.

The list below will indicate the used modules that are needed to run the log analyser correctly.
```
PIP                    Used for installing optional module if not presisdent
OS                     Used for clearing the terminal window.
RE                     Used for finding data in the log file
Argepasre              Used for command line arguments
Sys                    Used to exit the script
importlib.util         Used to determine currect path
Configparser           Used to read config file
Counter                Used to count specific objects
Datetime               Used to retrieve current time and date
Platform               Used to determine current platform
Prettytable            Used to create pretty tables*

*Non default module
```

### Config file

The config file below is used to configure the filepaths and de command line letters.

The file needs to be placed in the same directory as the Python script and be named "config.ini"

The config.ini and the vsftpd.log will be included in the repo.


Arguments in config.ini:
```
[logpath]
AnalysatieLogfile = E:/Downloads/vsftpd.log         
Resultaatfile = E:/Downloads/results.txt            

[CliLetters]
Missing = -m                                        
Top10 = -t
Connected = -c

```


## Built With

* [Jetbrains Pycharm](https://www.jetbrains.com/pycharm/) - The IDE used
* [Python 3](https://www.python.org/download/releases/3.0/) - Programming language used
* [Prettytable](https://pypi.org/project/PrettyTable/) - Used to generate pretty ASCII tables




## Authors

* **Jesse Jagers** - Author and Developer


