def prompt_filename():
    file = input('Please enter a file name: ')
    return file


def word_chosen():
    user_word = input('Enter a word: ').lower()
    return user_word


def parse_file(file, user_word):
    read_file = open(file, 'r')

    num_word = 0

    for line in read_file:
        line = line.strip('/n')
        words = line.split(' ')

        for key_word in words:
            if key_word == user_word:
                num_word += 1

    # outside word loop so it can read all the lines
    return num_word

    read_file.close()


def main():
    file = prompt_filename()
    print(f'Opening file {file}')

    user_word = word_chosen()
    num_word = parse_file(file, user_word)
    print(
        f'The word {user_word} occurs {num_word} times in this file.')


if __name__ == "__main__":
    main()
