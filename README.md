# DeskTop-Notifier-with-python-

A simple python script to give you notification on the current bitcoin price in us dollars.
This script if very dynamic and customizable. you can change the currency and the crypto coin you want to get notify on.



# Install requirements
1. Use the following commands to install required packages.
    ```
    pip3 install notify-py
    pip3 install schedule
    pip3 install pycoingecko
    ```

Or use 
```
pip3 install -r requirements.txt
```

2. After installing the requirements, run 
```
python3 Main.py
```
in the terminal and wait for 1 minute.You should get notification alert of current bitcoin price.If you had any error, you can post it in the issues tab of the repository.

# Usage
1. `python3 main.py`.This will run the script and give you notification of bitcoin price after one minute.

2. use `python3 Main.py --help` to see all the commands you can use on the script.

2 . `python3 Main.py -t 2 `.This will run the script and give you notifications of bitcoin price after two minute.You can also pass in the currency you want to use or even if you want to get notification in seconds instead of minutes.You can also set the script to repeatedly give you the notification base on the time you set using the --loop cath in the terminal.

 # Note
 This project is still under development. Your features and pull requests are welcome.

# Inspiration
![Gilfoyle](images/gilfoyle.jpg?raw=true "Gilfoyle")

 # API
 https://www.coingecko.com/en/api

You can use the following techniques here to make the script run on your computer startup if you want.
https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu#
