from utils import speak,emotionPredict,openSongs,openMovieList
from happyEmotion import happy_run
from sadEmotion import  sad_run
from angryEmotion import angry_run
from  calmEmotion import  calm_run
#from audioRecorder import  record

print("Welcome to the voice emotion recognition system")
speak("Welcome to the voice emotion recognition system")
speak("press 1 to start recording")
speak("press 2 to exit")
option=int(input())
if option==1:
    while option == 1:
        speak('Predicting the emotion')
        #emotion=emotionPredict()
        speak('happy')
        emotion='happy'
        if emotion =='happy':
            happy_run()
        elif emotion =='sad':
            sad_run()
        elif emotion =='angry':
            angry_run()
        elif emotion == 'calm':
            calm_run()

    print('Want to Continue ? press 1 ')
    i = int(input())
    if i == 1:
        pass
    else:
        print('Good Bye !!')
        exit()
else:
    exit()
