'''Week 09 Data Structure'''
import csv


def read_csv(filename, index):
    '''Reads csv file and creates a dictionary'''
    # Create a dictionary to hold the education level counts
    education = {}

    # Open file, read line by line, splits line base on comma (comma split is default)
    with open(filename, 'rt') as census_file:
        reader = csv.reader(census_file)

        # row = line. Reads each row
        for row in reader:
            key = row[index]
            education[key] = row[3]

    return(education)  # ex: {'bachelors': 'bachelor'}


def main():
    EDUCATION_LEVEL = 3
    # Reads content
    education = read_csv('census.csv', EDUCATION_LEVEL)

    # If education level is not in dictionary
    count = 0
    if EDUCATION_LEVEL not in education:
        # add = education.append(EDUCATION_LEVEL)
        count += 1
        return count

    # If education level is in dictionary
    elif EDUCATION_LEVEL in education:
        print(EDUCATION_LEVEL)
        # education[EDUCATION_LEVEL] = EDUCATION_LEVEL + 1
        # return education[EDUCATION_LEVEL]

    # Loops through each key and print key: value pair
    for EDUCATION_LEVEL in education.keys():
        print(f'{count} -- {education[EDUCATION_LEVEL]}')


if __name__ == "__main__":
    main()
