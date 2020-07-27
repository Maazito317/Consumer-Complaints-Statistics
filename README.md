# Consumer-Complaints-Insight
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies.

**For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

## Summary

 - Dictionary with composite key used to implement solution as it takes O(1) time for search and insert operations
 - Dictionary is further processed to produce required statistics
 - On the provided large data set, runtime amounts to ~3 min

## Solution
My solution consists of using a dictionary with a composite key. The key that I've used is of the form (Product, Year) as the problem was concerned with finding out statistics for each financial product and year. I chose this data structure as it takes O(1) time on average to store and search a key. To implement the code, I used the csv, argparse, pathlib, decimal, and collections built-in libraries. The structure of the dictionary is as follows:

```
comp_dict = {
             ('Product A', 'Year'): {'company1': 3; 'company2': 2; 'num_complaints': 5; 'num_companies': 2},
	     ('Product B', 'Year'): {'company3': 5; 'company2': 2; 'num_complaints': 7; 'num_companies': 2},
	    }
``` 
The dictionary stores number of complaints to a single company, total number of complaints, and the total number of companies.

## Installation

Run the solution using [run.sh](https://github.com/Maazito317/Consumer-Complaints-Insight/blob/master/run.sh) in the pharmacy_counting directory. The bash file runs the [complaints_count.py](https://github.com/Maazito317/Consumer-Complaints-Insight/tree/master/src/complaints_count.py) with [complaints.csv](https://github.com/Maazito317/Consumer-Complaints-Insight/blob/master/input/complaints.csv) as input and [output.csv](https://github.com/Maazito317/Consumer-Complaints-Insight/blob/master/output/report.csv) as output.

## Testing
A sample test is given with input `complaints.csv` 

The sample output given in `output.csv` is

```
credit reporting, credit repair services, or other personal consumer reports, 2019, 2, 3, 66
credit reporting, credit repair services, or other personal consumer reports, 2020, 1, 1, 100
debt collection, 2019, 1, 1, 100

```

## Unit Tests
The unit tests are developed for testing the functions manipulating the data

 - collect_complaints_count: uses a dictionary data structure with a composite key containing (Product, Year) with value
    entries of 'Company name', 'Number of complaints', and 'number of companies'
    
 - process_complaints: processes complaint stats by iterating through the items of the dictionary to find
    the company with the highest number of complaints and generating the required Statistics and returns output to be stored in report

