# SLCSP problem
# From https://homework.adhoc.team/slcsp/
# Sarah Withee's solution

import sys
from Zips import Zips
from SilverPlans import SilverPlans


def main():
    # Where all zip and plan read in data will go
    all_zips = Zips()
    all_silver_plans = SilverPlans()

    # Read in all zip and plan info from file
    read_zip_file(all_zips)
    read_plans_file(all_silver_plans)

    # Parse SLCSP file and get the correct rate
    try:
        with open("slcsp.csv", "rt") as file_slcsp:
            # output the first line
            print(file_slcsp.readline().strip())

            for line in file_slcsp:
                # If there's a blank line in the file, skip it
                if line == "":
                    continue
                # Zipcode is the first number before the comma. There should be nothing else
                zipcode = line.split(",")[0]

                # Look up zip code, then look up all rates from that state/rate area
                zip_state, zip_rate_area = all_zips.get_state_and_rate_area(zipcode)
                all_rates = all_silver_plans.get_all_plan_rates(zip_state, zip_rate_area)

                # Find how many rates there, are, then grab 2nd to last. If no rates or 1 rate, print
                # nothing (per directions)
                num_rates = len(all_rates)
                if num_rates < 2:
                    print("{0},".format(zipcode))
                    continue
                else:
                    slcsp = float(all_rates[num_rates - 2])
                    # Fancy way of printing zipcode, comma, then proper amount with two decimals
                    print("{0},{1:.2f}".format(zipcode, slcsp))

    except FileNotFoundError:
        sys.exit("Can't find the zips.csv file!")
    except IOError:
        sys.exit("Other unknown file read error!")


def read_plans_file(all_plans):
    try:
        with open("plans.csv", "rt") as file_plans:
            # ignore the first CSV line
            file_plans.readline()

            # If there's a blank line, skip over it
            for line in file_plans:
                if line == "":
                    continue
                # Trip ending newline char, then split on the comma
                line = line.rstrip().split(",")

                all_plans.add(line[0], line[1], line[2], line[3], line[4])

    except FileNotFoundError:
        sys.exit("Can't find the plans.csv file!")
    except IOError:
        sys.exit("Other unknown file read error!")


def read_zip_file(all_zips):
    try:
        with open("zips.csv", "rt") as file_zips:
            # ignore the first CSV line
            file_zips.readline()

            for line in file_zips:
                # If there's an empty line, ignore it
                if line == "":
                    continue
                # Trip ending newline char, then split on the comma
                line = line.rstrip().split(",")

                all_zips.add(line[0], line[1], line[2], line[3], line[4])

    except FileNotFoundError:
        sys.exit("Can't find the zips.csv file!")
    except IOError:
        sys.exit("Other unknown file read error!")


# Main function
if __name__ == "__main__":
    main()
