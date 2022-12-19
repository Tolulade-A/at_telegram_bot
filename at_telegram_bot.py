from flask import Flask, request, Response
import requests
import json
import numpy as np


# token that we get from the BotFather
TOKEN = "put your token here"

app = Flask(__name__)

# Reading the JSON message when the user send any type of file to the bot and extracting the chat id of the user and the file id for the file that user send to the bot
def tel_parse_get_message(message):
    print("message-->", message)

    try:  # if the file is an image
        g_chat_id = message['message']['chat']['id']
        g_file_id = message['message']['photo'][0]['file_id']
        print("g_chat_id-->", g_chat_id)
        print("g_image_id-->", g_file_id)

        return g_file_id
    except:
        try:  # if the file is a video
            g_chat_id = message['message']['chat']['id']
            g_file_id = message['message']['video']['file_id']
            print("g_chat_id-->", g_chat_id)
            print("g_video_id-->", g_file_id)

            return g_file_id
        except:
            try:  # if the file is an audio
                g_chat_id = message['message']['chat']['id']
                g_file_id = message['message']['audio']['file_id']
                print("g_chat_id-->", g_chat_id)
                print("g_audio_id-->", g_file_id)

                return g_file_id
            except:
                try:  # if the file is a document
                    g_chat_id = message['message']['chat']['id']
                    g_file_id = message['message']['document']['file_id']
                    print("g_chat_id-->", g_chat_id)
                    print("g_file_id-->", g_file_id)

                    return g_file_id
                except:
                    print("NO file found found-->>")


# Reading the JSON format when we send the text message and extracting the chat id of the user and the text that user send to the bot
def tel_parse_message(message):
    print("message-->", message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)

        return chat_id, txt
    except:
        print("NO text found-->>")

    try:
        cha_id = message['callback_query']['from']['id']
        i_txt = message['callback_query']['data']
        print("cha_id-->", cha_id)
        print("i_txt-->", i_txt)

        return cha_id, i_txt
    except:
        pass


# Get the Text message response from the bot
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, json=payload)
    return r


# Get the Image response from the bot by providing the image link
def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg"
    }
    r = requests.post(url, json=payload)
    return r


# Get the Poll response from the bot
def tel_send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    payload = {
        'chat_id': chat_id,
        "question": "Who owns Twitter?",
        # options are provided in json format
        "options": json.dumps(["Bill Gates", "Steve Jobs", "Elon Musk", "Aliko Dangote"]),
        "is_anonymous": False,
        "type": "quiz",
        # Here we are providing the index for the correct option(i.e. indexing starts from 0)
        "correct_option_id": 3
    }
    r = requests.post(url, json=payload)
    return r


# Get the Button response in the keyboard section
def tel_send_button(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "What is this?",    # button should be in the proper format as described
        'reply_markup': {
            'keyboard': [[
                {
                    'text': 'supa'
                },
                {
                    'text': 'mario'
                }
            ]]
        }
    }
    r = requests.post(url, json=payload)
    return r


# Get the Inline button response
def tel_send_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "What is this?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "A",
                    "callback_data": "ic_A"
                },
                {
                    "text": "B",
                    "callback_data": "ic_B"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r


# Get the Button response from the bot with the redirected URL
def tel_send_inlineurl(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "Which link would you like to visit?",
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "google", "url": "http://www.google.com/"},
                    {"text": "youtube", "url": "http://www.youtube.com/"}
                ]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r


# Get the Audio response from the bot by providing the URL for the audio
def tel_send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'

    payload = {
        'chat_id': chat_id,
        "audio": "http://www.largesound.com/ashborytour/sound/brobob.mp3",
    }
    r = requests.post(url, json=payload)
    return r


# Get the Document response from the bot by providing the URL for the Document
def tel_send_document(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

    payload = {
        'chat_id': chat_id,
        "document": "http://www.africau.edu/images/default/sample.pdf",
    }
    r = requests.post(url, json=payload)
    return r


# Get the Video response from the bot by providing the URL for the Video
def tel_send_video(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'

    payload = {
        'chat_id': chat_id,
        "video": "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4",
    }
    r = requests.post(url, json=payload)
    return r


# Get the url for the file through the file id
def tel_upload_file(file_id):
    # Getting the url for the file
    url = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}'
    a = requests.post(url)
    json_resp = json.loads(a.content)
    print("json_resp-->", json_resp)
    file_pathh = json_resp['result']['file_path']
    print("file_pathh-->", file_pathh)

    # saving the file to our computer
    url_1 = f'https://api.telegram.org/file/bot{TOKEN}/{file_pathh}'
    b = requests.get(url_1)
    file_content_bot = b.content
    with open(file_pathh, "wb") as f:
        f.write(file_content_bot)


# Reading the response from the user and responding to it accordingly
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        try:
            chat_id, txt = tel_parse_message(msg)
            if txt == "Hi":
                tel_send_message(chat_id, "Hello, I am AT Bot, what can I do for you?")
            # Add a greeting response for various greetings
            elif txt in ["hi", "hey", "Hey", "hello", "Hello", "halo", "Halo", "Hi there", "hi there"]:
                res = np.random.choice(
                    ["How are you today?", "Hello, you are welcome to AT Bot",
                     "What can I do for you today? Please reply with short phrases (e.g help, lawyer, I need help with a case etc)",
                     "How are you today?", "Hello, I'm doing good!", "Wadup?", "Nice to have you here!", "Cool!",
                     "I'm here if you need me!"
                     ])
                tel_send_message(chat_id, res)
            elif txt in ["I'm good","i'm good", "how are you?","How are you?", "How are you", "howdy", "Howdy", "How are you doing today?", "Are you hungry?",
                         "hungry", "Hungry", "Hungry?", "hungry?", "how are you feeling?", "How are you feeling?"
                         "How are you doing?", 'how are you doing?', "how are you doing"]:
                res = np.random.choice(
                    [ "Good",
                     "I've never been better, thanks", "I'm good",
                     "I'm okay, thank you.",
                     "Thanks for asking, i'm fine"])
                tel_send_message(chat_id, res)
            elif txt in ["i need help","I need help", "I'm not doing well","It's not a good day", "Yeah"]:
                res = np.random.choice(
                    ["How can i make your day better?",
                     "Would you like to book a session?!",
                     "I'm here if you need me!",
                     "I'm here for you"])
                tel_send_message(chat_id, res)
            elif txt in ["Who is a Lawyer?", "Who is a lawyer", "who is a lawyer", "who is a lawyer?", "Who is a lawyer?", "Who is a Lawyer"]:
                tel_send_message(chat_id, "A lawyer is a professional who is qualified to give legal advice "
                                          "and represent individuals and organizations in legal matters.")
            # Add a response for when the user asks about barristers
            elif txt in ["Who is a Barrister?", "who is a barrister", "who is a barrister?", "Who is a barrister?", "Who is a Barrister"]:
                tel_send_message(chat_id, "A barrister is a lawyer who is qualified to represent "
                                          "clients in legal proceedings, including in court.")
            elif txt in ["I need a lawyer", "i need a lawyer","legal", "Legal", "Help", "help", "I need help with a case", "i need help with a case", "Lawyer", "lawyer"]:
                res = np.random.choice(
                    ["Is there a case I could help you with?", "How would you like us to help you?",
                     "Would you like to book a session?!", "Okay!",
                     "I'm here if you need me!"])
                tel_send_message(chat_id, res)
            elif txt in ["Please book me a session", "Lawyer", "lawyer", "I need a Lawyer", "I need a lawyer", "yes", "Yes", "book", "Book", "Session", "session", "Counsel", "talk", "Talk", "I need help"]:
                res = np.random.choice(
                    ["Here, please book a legal session with our team https://calendly.com/toluladeademisoye_reispar!"])
                tel_send_message(chat_id, res)
            elif txt in ["thanks", "Thanks", "thank you", "thanks a lot", "Thanks a lot", "Great", "great", "grateful", "Grateful"]:
                res = np.random.choice(
                    ["You're welcome", "My pleasure", "The pleasure is mine :)", "Don't mention", "Happy I could be of help"])
                tel_send_message(chat_id, res)
            elif txt in ["bye", "Bye", "Good bye", "good bye", "see you later", "See you later", "It was nice chatting with you"]:
                res = np.random.choice(
                    ["Stay blessed", "See ya", "Be good, cheers!", "Byeee :)", "See you latter"])
                tel_send_message(chat_id, res)
            elif txt in ["What's your name?", "what's your name", "what's your name?", "What is your name",
                         "what is your name", "what is your name?", "What is your name?"]:
                tel_send_message(chat_id, "I am AT BOT with an handle yemir_bot developed by "
                                          "Tolulade Ademisoye!")
            elif txt in ["How can I contact you again?", "Will i see you again?", "Will I see you again?", "I'm going to miss you"]:
                tel_send_message(chat_id, "The same way you reached out to me now on Telegram. Search for my handle yemir_bot and start a convo, I'll reply if I'm online")
            elif txt == "image":
                tel_send_image(chat_id)
            elif txt == "poll":
                tel_send_poll(chat_id)
            elif txt == "button":
                tel_send_button(chat_id)
            elif txt == "audio":
                tel_send_audio(chat_id)
            elif txt == "file":
                tel_send_document(chat_id)
            elif txt == "video":
                tel_send_video(chat_id)
            elif txt == "inline":
                tel_send_inlinebutton(chat_id)
            elif txt == "inlineurl":
                tel_send_inlineurl(chat_id)
            elif txt == "ic_A":
                tel_send_message(chat_id, "You have clicked A")
            elif txt == "ic_B":
                tel_send_message(chat_id, "You have clicked B")
            else:
                tel_send_message(chat_id, 'Ooops!...I dont have that response yet. '
                                          'Also, I am case sensitive. You could ask--> Who is a Lawyer? or Who is a Barrister?')
        except:
            print("fromindex-->")

        try:
            file_id = tel_parse_get_message(msg)
            tel_upload_file(file_id)
        except:
            print("No file from index-->")

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"



if __name__ == '__main__':
    app.run(threaded=True)

