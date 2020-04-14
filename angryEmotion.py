import webbrowser
def open_songs():
    webbrowser.open('https://www.youtube.com/watch?v=bzSTpdcs-EI', new=0, autoraise=True)
    return

def angry_run():
    while True:
        print('1. Try these apps to calm a bit')
        print('2. Try reading these best books')
        print('3. Try listening to these podcast ')
        print('4. Try listening to these songs')
        print('5. Back to main menu ')

        opt = int(input())
        if opt == 1:
            webbrowser.open('http://dementiatalk.net/eight-apps-to-guide-you-about-dementia-and-anger/', new=0, autoraise=True)

        elif opt == 2:
            webbrowser.open('https://www.goodreads.com/shelf/show/anger-management', new=0, autoraise=True)

        elif opt == 3:
            webbrowser.open('https://player.fm/podcasts/Anger-Management', new=0, autoraise=True)

        elif opt == 4:
            webbrowser.open('https://open.spotify.com/playlist/54eyA9DewdUPaWRhvY7xYQ', new=0, autoraise=True)

        elif opt == 5:
            return
        else:
            print('wrong option')