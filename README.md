# stockTracker

This is a project assigned during my CSE 111 Database Systems course
at the University of California, Merced. This program is a flask
website with a sqlite database attached.

Analytics powered by Facebook's Data Analytics FBProphet:
http://facebook.github.io/prophet/

## Installation

You will need Python 3.x.x or later. Was written and tested in 3.9.x, 
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

## Issues

As of Apr 2024, program has ```string argument without an encoding``` error
When looking up stocks