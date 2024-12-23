import openai
import speech_recognition as sr
import os
import webbrowser
import pyttsx3

# Настройка OpenAI API
openai.api_key = "API"  # Замените на ваш API-ключ

# Настройка синтезатора речи
engine = pyttsx3.init()

# Функция для воспроизведения текста голосом
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция для общения с GPT-4
def gpt4_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Ошибка GPT-4: {e}")
        speak("Произошла ошибка при обработке вашего запроса.")
        return "Произошла ошибка при обработке вашего запроса."

# Функция для распознавания речи с микрофона по умолчанию
def listen_command():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:  # Используется микрофон по умолчанию
            print("Слушаю...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Не удалось распознать голос.")
        speak("Не удалось распознать голос.")
        return ""
    except sr.RequestError:
        print("Ошибка сервиса.")
        speak("Ошибка сервиса.")
        return ""
    except Exception as e:
        print(f"Ошибка при доступе к микрофону: {e}")
        speak("Ошибка при доступе к микрофону.")
        return ""

# Открытие Chrome
def open_chrome():
    webbrowser.open("https://www.google.com")
    print("Открываю браузер Chrome...")
    speak("Открываю браузер Chrome.")

# Запуск Spotify с заранее заданным плейлистом
def open_spotify_playlist():
    playlist_url = "https://open.spotify.com/playlist/.... " # Сдесь должна быть ссылка на ваш плейлист
    webbrowser.open(playlist_url)
    print(f"Открываю Spotify и запускаю плейлист: {playlist_url}")
    speak("Открываю Spotify и запускаю плейлист.")

# Запуск файла по пути
def launch_file(path):
    if os.path.exists(path):
        os.startfile(path)
        print(f"Запускаю файл: {path}")
        speak(f"Запускаю файл: {path}")
    else:
        print("Файл не найден.")
        speak("Файл не найден.")

# Функция для выполнения команд
def execute_command():
    command = listen_command()
    if "хром" in command:
        open_chrome()
    elif "спотифай" in command:
        open_spotify_playlist()
    elif "дискорд" in command:
        path = command.replace("запуск файла", "").strip()
        launch_file(path)
    else:
        response = gpt4_response(command)
        print(f"GPT-4: {response}")
        speak(response)

# Основной цикл для прослушивания команд
if __name__ == "__main__":
    print("Ассистент Mitaro запущен.")
    speak("Ассистент Mitaro запущен.")
    while True:
        execute_command()
