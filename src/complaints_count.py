import math
import copy
import csv
import argparse
from pathlib import Path
from decimal import Decimal
from collections import defaultdict


def read_complaint_entries_from_file(fname):
    """
    Simple function to read data from csv file to generate a list of relevant data entries

    param fname: path to complaint File
    return: list of relevant data entries
    """

    data = []
    try:
        with open(fname,encoding="utf8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Move past the header
            for row in reader:
                year = row[0:1][0][0:4]
                entry = [str.lower(row[1:2][0]), year, str.lower(row[7:8][0])]
                data.append(entry)
    except FileNotFoundError:
        print("File not found at {}".format(str(fname)))
    except Exception as err:
        print("Error reading data from file at {}".format(err))
    return data


def collect_complaints_count(data):
    """
    uses a dictionary data structure with a composite key containing (Product, Year) with value
    entries of 'Company name', 'Number of complaints', and 'number of companies'

    param data: list of relevant data
    return: dictionary with computed statistics
    """

    comp_dict = defaultdict(dict)
    default_details_dict = defaultdict(int)
    default_details_dict['num_companies'] = 0
    default_details_dict['num_complaints'] = 0

    for entry in data:
        key = (entry[0], entry[1])
        if key not in comp_dict:
            comp_dict[key] = copy.deepcopy(default_details_dict)
        details_dict = comp_dict[key]
        company = entry[2]
        details_dict[company] += 1
        details_dict['num_complaints'] += 1
        details_dict['num_companies'] = len(details_dict.keys()) - 2

    return comp_dict


def process_complaints(data):
    """
    processes complaint stats by iterating through the items of the dictionary to find
    the company with the highest number of complaints and generating the required Statistics

    param data: list of relevant data generate using read_complaint_entries_from_file
    return: sorted output to be printed
    """

    record_dict = collect_complaints_count(data)

    # Collect complaint-date stats
    output = []
    for k, v in record_dict.items():
        o_entry = [k[0], k[1], v["num_companies"], v["num_complaints"]]
        max_num_complaints_for_single_company = 0
        companies = v
        for company in (
                set(companies.keys()) - set(
                    ["num_companies", "num_complaints"])):
            if companies[company] > max_num_complaints_for_single_company:
                max_num_complaints_for_single_company = companies[company]
        percent = math.floor(
            100 * Decimal(
                max_num_complaints_for_single_company / v["num_complaints"]
            )
        )
        o_entry.append(percent)
        output.append(o_entry)

    output = sorted(output, key=lambda e: (e[0], e[1]))
    return output


def write_report_to_file(to_write, outfile):
    """
    Outputs required data to a csv file

    param to_write: output to be printed
    param outfile: path to output File
    """

    with open(outfile, "w") as csvfile:
        writer = csv.writer(csvfile)
        for row in to_write:
            writer.writerow([str(e) for e in row])


def main(args):
    data = read_complaint_entries_from_file(Path(args.input_file))
    processed_report = process_complaints(data)
    write_report_to_file(processed_report, args.outfile)


if __name__ == "__main__":
    """
    input: comma seperated file of [Date received, Product, Sub-product, Issue, Sub-issue, Consumer complaint narrative,
        Company public response, Company, State, ZIP code, Tags, Consumer consent provided?, Submitted via, Date sent to company,
        Company response to consumer, Timely response?, Consumer disputed?, Complaint ID]

    output: comma seperated file of [Product, Year, Total number of complaints, Total number of companies, Highest percentage]

    method: Statistics calculated using a dictionary that takes in a composite key of the form (Product, Year) and value entry which
        contains the companies and their respective complaints, number of companies, and number of total complaints. The highest percentage
        is then calculated by finding the company with the highest number of complaints by checking through the dictionary and output to the file.
    """

    parser = argparse.ArgumentParser(
        description="Collect Statistics for Complaint-Year Pairs")

    parser.add_argument("--input-file", required=True,
                        type=str, dest="input_file", help="Input dataset")
    parser.add_argument("--output-file", required=True,
                        type=str, dest="outfile",
                        help="File of the name to write results to")

    args = parser.parse_args()

    main(args)
