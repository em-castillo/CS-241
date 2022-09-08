'''W02 Prove Assignment'''

'''Write a program that can read an input file. Determine average commercial rate, '''
'''and display info for highest and lowest rates'''


'''Prompts user for file name'''


def prompt_filename():
    file = input('Please enter the data file: ')
    return file


'''Opens and reads through file'''


def parse_file(file):
    # opens file to read it
    read_file = open(file, 'r')

    rate = []
    average = 0
    highest_comm = 99999
    lowest_comm = 0
    total_lines = 0
    max_lines = ''
    min_lines = ''

    # next(read_file)
    for line in read_file:
        try:
            if(total_lines > 0):
                line = line.strip()
                parts = line.split(',')
                rate = float(parts[6])

                # calculating average, highest, and lowest rate.
                average += rate
                if (highest_comm > rate):
                    highest_comm = rate
                    max_lines = line

                if (lowest_comm < rate):
                    lowest_comm = rate
                    min_lines = line

            total_lines += 1  # reads next line
        except:
            return 0.0
    average = average / float(total_lines - 1)

    # closes file
    read_file.close()
    return average, max_lines, min_lines


'''Executes program'''


def main():
    # creating new object
    data_file = prompt_filename()
    print()

    average, minLine, maxLine = parse_file(data_file)

    # displaying average, highest, and lowest rate
    print(f'The average commercial rate is: {average}')
    print()

    print('The highest rate is:')
    max_output = maxLine.split(',')  # spliting line
    print(
        f'{max_output[2]} ({max_output[0]}, {max_output[3]}) - ${float(max_output[6])}')
    print()

    print('The lowest rate is:')
    min_output = minLine.split(',')
    print(
        f'{min_output[2]} ({min_output[0]}, {min_output[3]}) - ${float(min_output[6])}')


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
