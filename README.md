# rewardapi
""" Name : readme.md.py. Author : Nirav """ 

A retailer offers a rewards program to its customers, awarding points based on each recorded purchase. A customer receives 2 points for every dollar spent over $100 in each transaction, plus 1 point for every dollar spent over $50 in each transaction (e.g. a $120 purchase = 2x$20 + 1x$50 = 90 points). Given a record of every transaction during a three month period, calculate the reward points earned for each customer per month and total.

Change directory to parent directory of the new environment

cd <environment_parent_git_repo>

Create virtual environment

virtualenv <environment_name>

Activate the new virutal environment

source <environment_name>/bin/activate

On Windows, the equivalent activate script (https://virtualenv.pypa.io/en/stable/userguide/) is <environment_name>\Scripts\activate

For other Linux flavors, macOS and Windows, packages are available at [https://www.python.org/]

The requirements.txt file should list all Python libraries that your notebooks depend on, and they will be installed using

pip install -r requirements.txt **

Need to run Django APP server using:

python mange.py runsever 8080

you see following screen after running application:

Starting development server at http://127.0.0.1:8080/ Quit the server with CTRL-BREAK. "GET /store/rewardapi/ HTTP/1.1" 200 9186 "GET /store/rewardapi/?field_value=Customer HTTP/1.1" 200 9299

Need to hit API then return the details of customers and earned reward.

http://127.0.0.1:8080/store/rewardapi/

Return Result :

[{"Customer": "Bob", "Date": "3/12/2019", "Purchase Amount": 87, "Reward Points": 37}, {"Customer": "Bob", "Date": "3/3/2019", "Purchase Amount": 65, "Reward Points": 15}, {"Customer": "Bob", "Date": "4/23/2019", "Purchase Amount": 872, "Reward Points": 1594}, {"Customer": "Bob", "Date": "5/14/2019", "Purchase Amount": 671, "Reward Points": 1192}, {"Customer": "Bill", "Date": "3/29/2019", "Purchase Amount": 3, "Reward Points": 0}, {"Customer": "Bill", "Date": "4/8/2019", "Purchase Amount": 9, "Reward Points": 0}, {"Customer": "Bill", "Date": "4/22/2019", "Purchase Amount": 120, "Reward Points": 90}, {"Customer": "Bill", "Date": "5/18/2019", "Purchase Amount": 111, "Reward Points": 72}, {"Customer": "Joe", "Date": "3/5/2019", "Purchase Amount": 225, "Reward Points": 300}, {"Customer": "Joe", "Date": "4/15/2019", "Purchase Amount": 104, "Reward Points": 58}, {"Customer": "Joe", "Date": "5/2/2019", "Purchase Amount": 21, "Reward Points": 0}, {"Customer": "Joe", "Date": "5/24/2019", "Purchase Amount": 92, "Reward Points": 42}, {"Customer": "Brent", "Date": "3/14/2019", "Purchase Amount": 148, "Reward Points": 146}, {"Customer": "Brent", "Date": "3/16/2019", "Purchase Amount": 776, "Reward Points": 1402}, {"Customer": "Brent", "Date": "4/7/2018", "Purchase Amount": 431, "Reward Points": 712}, {"Customer": "Brent", "Date": "5/8/2019", "Purchase Amount": 226, "Reward Points": 302}, {"Customer": "Connor", "Date": "3/5/2019", "Purchase Amount": 367, "Reward Points": 584}, {"Customer": "Connor", "Date": "4/23/2019", "Purchase Amount": 21, "Reward Points": 0}, {"Customer": "Connor", "Date": "4/30/2019", "Purchase Amount": 54, "Reward Points": 4}, {"Customer": "Connor", "Date": "5/11/2019", "Purchase Amount": 106, "Reward Points": 62}, {"Customer": "Jacob", "Date": "3/17/2019", "Purchase Amount": 431, "Reward Points": 712}, {"Customer": "Jacob", "Date": "4/26/2019", "Purchase Amount": 217, "Reward Points": 284}, {"Customer": "Jacob", "Date": "5/19/2019", "Purchase Amount": 51, "Reward Points": 1}, {"Customer": "Jacob", "Date": "5/30/2019", "Purchase Amount": 27, "Reward Points": 0}]"

In order to return data based on sorting fields like Customer,Date,Purchase Amount,Reward Points.

call API this way: http://127.0.0.1:8080/store/rewardapi/?field_value=Customer

Ideas for the future Implementation:

Write more efficent code and make it look cleaner

data could be loaded into django model (I created model but not returning data from model,currently I am returning data from txt file in testdata folder)

More functionalities could be added in APIs like paginations,increse API response by adding multithreding, API logger,etc.

there will require more APIs and data model designing to get run Application by effectively way.

conclusion: with more time and effort I think this project could look a lot nicer then its current form.
