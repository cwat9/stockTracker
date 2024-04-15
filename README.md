# stockTracker

This is a project assigned during my CSE 111 Database Systems course
at the University of California, Merced. This program is a flask
website with a sqlite database attached.

## Installation

You will need Python 3.x.x or later. Was written in 3.8.x and tested until 3.9.x, 
but should support any Python 3 version.

To install, clone or download repo. Then in terminal run:
```
pip install -r requirements.txt
```

## Usage

To run, in terminal enter:
```
cd project-v2
```
then enter:
```
python app.py
```

This will run the main website with the current data (approx. Nov 2023)
To get the current or the latest stock data, you will need to run the
```generateStocks.py``` file. Then you will need to run 
the ```load-tpch.sql```

To modify the database, you will need to modify the ```create-schemal.sql```.
You may need to modify ```load-tpch.sql```.