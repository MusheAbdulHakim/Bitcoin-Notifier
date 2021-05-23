# DeskTop-Notifier-with-python-

A simple python script to give you notification on the current bitcoin price in us dollars after every one minute(Ofcourse you can change it by passing the time you want in the terminal).



# Install requirements
1.  `pip3 install notify-py`
2. `pip3 install schedule`
3. `pip3 install pycoingecko`

4. Or use  `pip3 install -r requirements.txt`

5. After installing the requirements, run main.py in the terminal and wait for 1 minute.You should get notification.

# Usage
1. `python3 main.py`.This will run the script and give you notification after every one minute.

2. `python3 main.py --help`.all the commands you can use to run the script.

2 . `python3 main.py 2 `.This will run the script and give you notifications after every two minute.You can pass any number of minutes you want it to notify you on the bitcoin price in the process of running the script in the terminal.

 # Note
 This project is still under development.



 # API
 https://www.coingecko.com/en/api

You can use the following techniques here to make the script run on your computer startup if you want.
https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu#
