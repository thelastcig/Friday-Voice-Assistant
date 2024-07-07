import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
import wikipedia
from time import ctime,sleep # get time details
import webbrowser # open browser # to fetch financial data
import ssl #security protocol email
import certifi
import time
import os # to remove created audio files
import smtplib #
#from twilio.rest import Client


def send_sms(ok, num):
    account_sid = 'ACb4c5b72db166a775d609ed9b40e525e3'
    auth_token = '97a28d3fb683b83f67b22aab5d56bb1d'
    client = Client(account_sid, auth_token)
    
    message = client.messages \
                    .create(
                        body= ok,
                        from_='+19386666645',
                        to= num
                    )

    #print(message.sid)
def phone(nump, say):
    account_sid = 'ACb4c5b72db166a775d609ed9b40e525e3'
    auth_token = '97a28d3fb683b83f67b22aab5d56bb1d'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            twiml=f'<Response><Say>{say}</Say></Response>',
                            to=nump,
                            from_='+19386666645'
                        )

    #print(call.sid)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nishasxxxxxxxxx@gmail.com', 'xxxxxxx')
    server.sendmail('nishashxxxxxxxxxxx@gmail.com', to, content)
    server.close()

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

            

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
  
def record_audio(ask=False):
    
    with sr.Microphone() as source: # microphone as source
        print('Friday: Listening..')
        
        r.adjust_for_ambient_noise(source,duration=1)

        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:

            voice_data = r.recognize_google(audio)  # convert audio to text
        
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en', tld='co.uk') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'a' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Friday: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file
    





def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Friday")
        else:
            speak("my name is Friday. what's your name?")

    if there_exists(["my name is",]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    if there_exists(['pause','wait a second']):
        speak('sleeping for 20 seconds')
        sleep(20)
    # 5: search google
    
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_exists(["who is"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("is")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    
    if there_exists(["where is"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("is")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_exists(["open"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("open")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_exists(['subtitle of','download subtitle']):
        from friday_subtitle import Subtitle,search_term
        
        speak('please enter the name of the movie')
        bot=Subtitle(search_term)
        speak(f" subtitle of {search_term} downloaded successfully")
        speak('oh! I am tired,going offline!')
        exit()
    
    if there_exists(['play music']) and 'youtube' not in voice_data:
        from friday_music import Jio
        speak('what song you want to hear?')
        search = record_audio()
        bot=Jio(search)
        bot.lyrics(search)     
        speak(f'playing {search} on Jiosaavan!')
        sleep(60)
    
    
    
    if there_exists(["my folder","folder"]):
        path = "E:\\aman"
        os.startfile(path)
        speak('here is your folder wide opend')
    
    
    
    
    # 6: search youtube
    
    
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    if there_exists({'maps','find location','map'}):
        speak('Please tell me your location you want to search')
        l = record_audio()    
        speak('searching maps')
        webbrowser.get().open(f"https://www.google.com/maps/place/{l}")
        speak(f'here is what i found for {l}')

    if there_exists(['get direction','start a trip']):
        speak('please tell your starting point')
        s = record_audio()
        speak('please tell your destination')
        d = record_audio()
        speak('getting direction')
        webbrowser.get().open(f"https://www.google.com/maps/dir/{s}/{d}")
        speak(f'here is the direction from {s} to {d}, enjoy your trip')
    
    
    
    #7 : Wikipedia
   
    if there_exists(['wikipedia']):
        search_term = voice_data.split('for')[-1]
        speak('searching wikipedia..')
        result = wikipedia.summary(search_term, sentences=2)
        print(result)
        speak(f'According to wikipedia {result}')
        

    if there_exists(['send mail','email']):
        try:
                speak('Please! enter reciever email adress')
                to = input('Please enter reciever email>> ')
                speak("What should I say?")
                content = record_audio()   
                sendEmail(to, content)
                speak(f"Email has been sent! to {to}")
        except Exception as e:
            print(e)
            speak("Pardon me! Aman Sharma. I am not able to send this email") 

    if there_exists({'send sms','sms'}):
        try:
            speak("please enter the reciever's cell number")
            pre = input('Enter the the number= ')
            num = f"+91{pre}" 
            speak('what message you want to send')
            ok = record_audio()
            send_sms(ok, num)
            speak('message has been sent')
        except Exception as e:
            print(e)
            speak('pardon me i am not able to send message right now')
    
    if there_exists(['send a whatsapp message', 'whatsapp message']):
        speak('kindly input your selection and hit enter')
        print('\t\t1. Text only')
        print('\t\t2. Media only')
        print('\t\t3. Both(Text & Media)')
        ch=int(input('\t\tEnter your choice and hit enter: '))

        if ch == 1:
            from WhatApp_Text import WhatsppBot
        elif ch == 2:
            from WhatsApp_Media import WhatsppBot
        elif ch == 3:
            from Whatsapp import WhatsppBot
        else:
            print('Invalid choice')


    if there_exists({'make a call','phone','call'}):
        try:
            speak("please enter the reciever's cell number")
            pre = input('Enter the the number= ')
            nump = f"+91{pre}" 
            speak('what voice message you want to send')
            say = record_audio()
            phone(nump, say)
            speak(' voice message has been sent')
        except Exception as e:
            print(e)
            speak('pardon me i am not able to send this voice message right now')
    
    if there_exists(['tell me a joke','jokes','joke']):
        from friday_joke import jokes
        joke = jokes[random.randint(0,len(jokes)-1)] 
        speak(joke)   
    
    if there_exists(['good','good girl','nice','nice work']):
        comps = [
            'As long as you are happy, i am happy',
            'Thanks! master',
            'keep saying that!'
        ]
        comp = comps[random.randint(0,len(comps)-1)]
        speak(comp)   
    
    if there_exists(['thanks','thank you']):
        thanks = [
            "oh!, don't embarrass me by saying that!",
            "anytime fam!"
        ]
        thank = thanks[random.randint(0,len(thanks)-1)]
        speak(thank)

        
    if there_exists(['compare my followers on instagram','my instagram follower']):
        speak('please enter your username and password ')
        from Instabot import InstaBot,username,pw
        speak('automating your instagram')
        my_bot = InstaBot(username, pw)
        speak('making list of followers who are not following back')
        my_bot.get_unfollowers()
        f=open('instagram.txt','r')
        a = f.read()
        b = a.split()
        c = b[4:15]
        string=""
        for n in c:
            string+= f" ,{n}"
        length=(len(b)-4)-len(c)
        speak(f'here are the cunts who are not following you back, {string} and, {length} more')
    
    if there_exists(['download images from instagram']):
        speak('Enter your user name,password and name of the person whose image you want to download')
        from insta_download import InstaDownload,user,pw,dwuser
        speak('automating your instagram')
        bot=InstaDownload()
        speak('logged in successfully,downaloading images and opening it in few seconds')
        bot.download_user_img()
        sleep(10)
    if there_exists(['my nda website']):
        webbrowser.get().open('https://nda.netlify.com')
        speak("here is you nda website!")
    if there_exists(['my website']):
        webbrowser.get().open('https://needs.netlify.com')
        speak('here is your website!')
    if there_exists(["who made you","owner",'who is your owner']):
        speak('I was made by the great Aman Sharma!')
        os.startfile("E:\\aman\\coool.jpg")
        playsound.playsound('F:\\intro.mp3')
        webbrowser.get().open('https://www.instagram.com/the_.last_.cigarette/')    
        speak("Here is his instagram, Oh my God! he is so 'handsome'!")

    if there_exists(['coronavirus update','coronavirus']):
        speak('Getting data from worldometers please wait few seconds')
        from corona import Corona
        fr = open('corona.txt','r')
        cread = fr.read()
        speak(cread)
        

    
    
    if there_exists(['what can you do']):
        todos = [
            'I can make phone call, '
            'I can send message, '
            'I can send email, '
            'I can play music on jio saavan, '
            'I can search google, youtube and wikipedia,'
            'I can open yor Instagram and Folder, '
            'I can search map and get you direction, '
            'I can make you play games, '
            'I can search for your movie subtitle, '
            'and i am still in beta so Pardon me! for the inconvinience'
        ]
        todo = todos[random.randint(0,len(todos)-1)] 
        speak(todo)     

    if there_exists(["exit", "quit", "goodbye"]):
        speak(f"going offline, goodbye {person_obj.name}")
        exit()


time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond