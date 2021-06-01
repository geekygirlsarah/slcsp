# 1. Read in zips.csv into dict (by zip code)
# 2. Read in plans.csv into dict (by plan_id), add to list (dedup set?)
# 2a. Map plan_id to rate_area (dict?)
# 3. Read in slcsp.csv line by line
# 3a. Look up zipcode in Zips, get state, county, name, rate
# 3b. Look up plan by rate area, get all rates
# 3c. Sort rates
# 3d. Get item 2
# 3e. Return stdout of full slcsp line
# 4. close any open files.
import sys
from Zips import Zips
from Plans import Plans


def main():
    all_zips = Zips()
    all_plans = Plans()
    try:
        with open("zips.csv", "rt") as file_zips:
            # ignore the first CSV line
            file_zips.readline()

            for line in file_zips:
                if line == "":
                    continue
                # Trip ending newline char, then split on the comma
                line = line.rstrip().split(",")
                all_zips.add(line[0], line[1], line[2], line[3], line[4])

    except FileNotFoundError:
        sys.exit("Can't find the zips.csv file!")
    except IOError:
        sys.exit("Other unknown file read error!")

    try:
        with open("plans.csv", "rt") as file_plans:
            # ignore the first CSV line
            file_plans.readline()

            for line in file_plans:
                if line == "":
                    continue
                # Trip ending newline char, then split on the comma
                line = line.rstrip().split(",")
                all_plans.add(line[0], line[1], line[2], line[3], line[4])

    except FileNotFoundError:
        sys.exit("Can't find the zips.csv file!")
    except IOError:
        sys.exit("Other unknown file read error!")

    print("hiiiii")

if __name__ == "__main__":
    main()
