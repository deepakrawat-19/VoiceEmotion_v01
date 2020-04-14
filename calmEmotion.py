import webbrowser

def calm_run():
    while True:
        print('1. A playlist you should try  to remain this way')
        print('2. Watch Best bollywood movies of all time')
        print('3. Try listening to something productive')
        print('4. Back to main menu ')
        opt = int(input())
        if opt == 1:
            webbrowser.open('https://open.spotify.com/playlist/7FmeUPFHkwT5RzkYVHtTJ2', new=0, autoraise=True)

        elif opt == 2:
            webbrowser.open('https://www.scoopwhoop.com/feel-good-movies/', new=0, autoraise=True)

        elif opt == 3:
            webbrowser.open('https://www.inc.com/rhett-power/10-inspirational-podcasts-that-will-make-you-better.html', new=0, autoraise=True)

        elif opt == 4:
            return
        else:
            print('wrong option')