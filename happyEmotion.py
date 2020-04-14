import webbrowser
def open_songs():
    print('1. list of songs that might suits your expression of happiness [spotify]')
    print('2. list of song you can dance to express')
    print('3. list of best melody Bollywood songs')
    x = int(input())
    if x == 1:
        webbrowser.open('https://open.spotify.com/playlist/1llkez7kiZtBeOw5UjFlJq#login', new=0, autoraise=True)
        return
    elif x == 2:
        webbrowser.open('https://www.youtube.com/watch?v=8LZgzAZ2lpQ&list=RDQMIYvFMcwkOvU&start_radio=1', new=0, autoraise=True)
        return
    elif x == 3:
        webbrowser.open('https://www.youtube.com/watch?v=inEu2qQuGZ8&list=PLjity7Lwv-zoCXwWAyH5093HL_XRPiLwz&index=13', new=0, autoraise=True)
        return

def happy_run():
    while True:
        print('1. Would you like knowing the chemistry of happiness !')
        print('2. Songs that might suits your expression of happiness')
        print('3. Donate some help and make someone else happy too,here is how')
        print('4. Back to main menu ')
        opt = int(input())
        if opt == 1:
            webbrowser.open('https://www.youtube.com/watch?v=5rzR69NZv_k', new=0, autoraise=True)
        elif opt == 2:
            open_songs()
        elif opt == 3:
            webbrowser.open('https://www.indiatoday.in/information/story/coronavirus-pm-cares-fund-donation-how-to-transfer-money-to-pm-cares-fund-from-paytm-bank-account-1660900-2020-03-29', new=0, autoraise=True)
        elif opt == 4:
            return
        else:
            print('wrong option')