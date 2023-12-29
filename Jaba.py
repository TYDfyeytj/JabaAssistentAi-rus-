import re
import os
import time
import webbrowser
import random
import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

thanks = ["Спасибо!", "Незачто!"]

default_browser = "https://www.example.com"
assistant_name = "жаба"

phonk_urls = [
    "https://www.youtube.com/watch?v=8WtRKHwVROs",
    "https://www.youtube.com/watch?v=8JkVaqlV5b4",
    "https://www.youtube.com/watch?v=j4htIC8C83U",
    "https://www.youtube.com/watch?v=EZ0PjxkDZiY",
    "https://www.youtube.com/watch?v=TwXfCAtctEs",
    "https://www.youtube.com/watch?v=WsvYqR3OGhw",
    "https://www.youtube.com/watch?v=A0JgsYz99BE",
    "https://www.youtube.com/watch?v=k9RU4uW0kSY",
    "https://www.youtube.com/watch?v=9MzJMUquCIU"
]

relaxing_music_urls = [
    "https://www.youtube.com/watch?v=6EtUqdynZkM",
    "https://www.youtube.com/watch?v=4xDzrJKXOOY",
    "https://www.youtube.com/watch?v=jfKfPfyJRdk",
    "https://www.youtube.com/watch?v=lPCeCDnvzxM",
    "https://www.youtube.com/watch?v=t33pTfQYvRY",
    "https://www.youtube.com/watch?v=D4itjdUC4IM",
    "https://www.youtube.com/watch?v=sWPV1eMS2xA",
    "https://www.youtube.com/watch?v=akBFTyfKTrA",
    "https://www.youtube.com/watch?v=HkE_TxlNSA4"
]

commands = {
    "пока": ["пока", "пака", "бб", "удачи", "удачки"],
    "Открой браузер": ["открой браузер", "браузер открой", "аткрой браузер", "открой браузэр", "вруби браузер", "запусти браузер", "старт браузер"],
    "Включи фонк": ["включи фонк", "вруби фонк", "фонк включи", "запусти фонк", "загрузи фонк", "фонк вруби", "старт фонк", "запусти phonk", "включи phonk"],
    "Расслабляющая музыка": ["включи расслабляющую музыку", "расслабляющая музыка", "вруби расслабляющую музыку", "расслабляющую музыку вруби", "включи чил музыку", "чил музыка", "вруби успокаивающую музыку", "успокаивающаяся музыка", "расслабляющая музыка"], 
    "Молодец": ["молодец", "спасибо", "большое спасибо", "спс"],
    "Привет": ["привет", "здравствуй", "здравствуйте", "добрый день", "добрый вечер"],
    "Включи фонк и привет": ["включи фонк и привет", "фонк включи и привет", "запусти фонк и скажи привет", "включи phonk и привет"],
    "Как дела": ["как дела", "как ты", "как у тебя"],
    "Спасибо": ["спасибо", "благодарю", "благодарствую"],
    "Помощь": ["помощь", "чем можешь помочь", "что ты умеешь"],
    "Пожалуйста, жаба": ["пожалуйста, жаба", "пожалуйста", "пожалуйста, помоги"],
    "Перемотай видео до конца": ["перемотай видео до конца", "перемотай до конца", "перемотай видео в конец"],
    "Перемотай видео к середине": ["перемотай видео к середине", "перемотай к середине", "перемотай видео в середину"],
    "Перемотай видео к началу": ["перемотай видео к началу", "перемотай к началу", "перемотай видео в начало"],
    "Открой консоль": ["открой консоль", "запусти консоль", "командная строка"],
    "Открой проводник": ["открой проводник", "запусти проводник", "файловый менеджер"],
    "Сверни окна" : ["сверни все окна", "сверни окна"]

}

def match_command(text, keywords):
    for keyword in keywords:
        if re.search(rf'\b{keyword}\b', text):
            return True
    return False

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        recognizer.adjust_for_ambient_noise(source)
        recognizer.energy_threshold = 500  # Устанавливаем порог чувствительности
        source.timeout = 0.1  # Устанавливаем минимальное время ожидания ввода звука
        audio = recognizer.listen(source)

    try:
        print("Распознавание...")
        text = recognizer.recognize_google(audio, language="ru-RU").lower()
        
        # Проверка на наличие ключевого слова "жаба"
        if "жаба" in text:
            # Удаляем ключевое слово "жаба" из текста переданной команды
            text = text.replace("жаба", "").strip()

            print(f"Вы сказали: {text}")
            return text
        else:
            print("Прошу прощения, вы забыли сказать 'жаба'. Повторите команду.")
            return None
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь.")
        return None
    except sr.RequestError as e:
        print(f"Ошибка запроса к сервису распознавания: {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def rewind_youtube_to_start():
    # Use the actual path to your ChromeDriver executable
    chrome_driver_path = r"C:\Users\user\.wdm\drivers\chromedriver\win64\119.0.6045.105\chromedriver-win32"
    browser = webdriver.Chrome(executable_path=chrome_driver_path)
    browser.get("https://www.youtube.com")  # Open YouTube
    time.sleep(2)  # Wait for the page to load

    # Send key press to move to the beginning of the video
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.HOME)

def execute_command(action):
    if action == "пока":
        speak("Удачи!")
        return
    elif action == "Открой браузер":
        speak("Ок, открываю.")
        webbrowser.open(default_browser)
    elif action == "Включи фонк":
        speak("Включаю фонк!")
        webbrowser.open(random.choice(phonk_urls))
    elif action == "Расслабляющая музыка":
        speak("Давай разслабимся!")
        webbrowser.open(random.choice(relaxing_music_urls))
    elif action == "Молодец":
        speak(random.choice(thanks))
    elif action == "Привет":
        speak("Привет! Чем могу помочь?")
    elif action == "Включи фонк и привет":
        speak("Включаю фонк и говорю привет!")
        webbrowser.open(random.choice(phonk_urls))
        speak("Привет!")
    elif action == "Как дела":
        speak("У меня все отлично, спасибо! Как у вас?")
    elif action == "Спасибо":
        speak("Пожалуйста! Если у вас есть еще вопросы, спрашивайте.")
    elif action == "Помощь":
        speak("Я могу открывать браузер, включать фонк и расслабляющую музыку, могу открывать проводник, консоль, сворачивать все окна. Просто скажите, чем я могу вам помочь.")
    elif action == "Пожалуйста, жаба":
        speak("Пожалуйста! Чем могу еще помочь, жаба?")
    elif action == "Перемотай видео до конца":
        speak("Перематываю видео до конца.")
        rewind_youtube_to_start()
    elif action == "Перемотай видео к середине":
        speak("Перематываю видео к середине.")
        # Implement code to move to the middle of the video
    elif action == "Перемотай видео к началу":
        speak("Перематываю видео к началу.")
        # Implement code to move to the beginning of the video
    elif action == "Открой консоль":
        speak("Открываю консоль.")
        os.system("start cmd")
    elif action == "Открой проводник":
        speak("Открываю проводник.")
        os.system("start explorer")
    elif action == "Сверни окна":
        speak("Сворачиваю окна...")
        pyautogui.hotkey('winleft', 'd')
        

def process_general_command(command):
    # Process general commands based on key terms
    if "пожалуйста" in command and ("включи" in command or "запусти" in command) and ("фонк" in command or "расслабляющая музыка" in command):
        speak("Конечно! Включаю прикольный фонк.")
        webbrowser.open(random.choice(phonk_urls))
    else:
        speak("Простите, жаба вас не поняла")

def main():
    speak(f"Привет! Я ваш голосовой ассистент {assistant_name}. Как я могу вам помочь?")

    while True:
        command = listen()
        if command:
            command_matched = False  # Флаг для проверки совпадения команды

            # Проверьте, соответствует ли команда какой-либо явной команде
            for action, keywords in commands.items():
                if match_command(command, keywords):
                    command_matched = True  # Установите флаг в True
                    execute_command(action)
                    break  # Выйдите из цикла после первой совпавшей команды

            # Если явная команда не совпадает, реагируйте на общие шаблоны
            if not command_matched:
                process_general_command(command)

if __name__ == "__main__":
    main()
