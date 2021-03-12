import speech_recognition as sr
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.pause_threshold = 0.5
        print('Listening(Speak Close Consent to close)...')
        audio = r.listen(source)
        try: 
            print("Recognizing")
            query = r.recognize_google(audio, language="en-US")
            print("You Speaked: {}".format(query))
            if str(query).lower() == 'close content':
                file.close()
                print("Terminated! Thanks For Using")
                exit()
            else:
                return query
        except Exception:
            print('Cannot be Listenning')
if __name__ == '__main__':
    file = open("{}.txt".format(input("Filename: ")), 'w')
    file.write('__________________Data___________________\n')
    while True:
        query = takeCommand()
        file.write(f'{query}\n')