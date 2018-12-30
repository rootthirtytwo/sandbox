import re
import os

# read the html file that has the list of boys and girls name with their ranking, need to parse them and make a
# combined list with year as a top entry followed by Name & their rank(combined) in alphabetical orders

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "Exercise_001_Data")
file_name_path = os.path.join(FILE_PATH, 'baby1990.html')

# function to parse the given file
def extract_data(file):
    with open(file, 'r') as f:
        text = f.read()

    header_match = re.search(r'Popularity in\s(\d\d\d\d)', text)
    if header_match is not None:
        year = header_match.group(1)

    tuples = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    return tuples, year

data, year = extract_data(file_name_path)
# call extract data and produce final result
def main():


    if data is not None:
        male = [t[1]+' '+t[0] for t in data]
        female = [t[2]+' '+t[0] for t in data]
        names = sorted(male + female)
        names.insert(0, year)
        print('\n'.join(names), sep='\n')

if __name__=="__main__":
    main()