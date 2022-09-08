'''W04 Data Structure'''
'''Use a LINKED LIST (deque) to keep track of a playlist of songs.'''


# creating songs linked list




from collections import deque
class Song:
    # initialize. Title and artist variables
    def __init__(self):
        self.title = ''
        self.artist = ''

    # asks the user for the title and artist
    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")
        return

    # displays the title and the artist to the screen
    def display(self):
        print(f'{self.title} by {self.artist}')


def main():
    # Create a deque of songs for your playlist.
    song_list = deque()
    # songs = Song() / object does not work if is global inside this function
    # otherwise it updates the song each time

    selection = 0

    # loop for options to do
    while selection != 4:
        print('Options: ')
        print('1. Add a new song to the end of the playlist')
        print('2. Insert a new song to the beginning of the playlist')
        print('3. Play the next song')
        print('4. Quit')
        selection = int(input('Enter selection: '))
        print()

        if selection == 1:
            songs = Song()  # updates new song inserted
            songs.prompt()
            song_list.append(songs)
            # append: adds at the end of list, needs a variable
            print()

        elif selection == 2:
            songs = Song()  # updates new song inserted
            songs.prompt()
            song_list.appendleft(songs)
            # append: adds at the beginning of list, needs a variable
            print()

        elif selection == 3:

            if not len(song_list):  # empty list condition
                print('The playlist is currently empty.')
                print()

            else:
                song_left = song_list.popleft()  # variable made for song left to be later displayed
                # popleft: removes at the beginning of list, doesn't need a variable
                # pop: removes last one
                print('Playing song:')
                song_left.display()
                print()

        else:
            print('Goodbye')


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()

# 3 hours
