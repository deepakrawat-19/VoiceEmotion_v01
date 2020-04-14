import webbrowser

def sad_run():
    while True:
        print('1. Understand why you are sad')
        print('2. A list of great podcasts you might like')
        print('3. Here is a list of best hollywood movies of all time to boost your mood')
        print('4. Try reading these books might change your opinion ')
        print('5. Back to main menu ')

        opt = int(input())
        if opt == 1:
            webbrowser.open('https://www.youtube.com/watch?v=GOK1tKFFIQI', new=0, autoraise=True)

        elif opt == 2:
            webbrowser.open('https://www.bustle.com/p/12-podcasts-to-help-anxiety-depression-whether-you-want-to-laugh-cry-find-a-way-to-unwind-15909570', new=0, autoraise=True)

        elif opt == 3:
            webbrowser.open('https://fmovies.wtf/filter?sort=imdb%3Adesc&type%5B%5D=movie&subtitle%5B%5D=1', new=0, autoraise=True)

        elif opt == 4:
            webbrowser.open('https://reedsy.com/discovery/blog/best-books-to-read-in-a-lifetime', new=0,autoraise=True)

        elif opt == 5:
            return
        else:
            print('wrong option')
