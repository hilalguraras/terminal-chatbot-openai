from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # .env dosyasındaki API key'i yükler
client = OpenAI()

print("Sohbet Başlatıldı!!")

# Konuşma geçmişi
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("Kullanıcı: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Sohbet sonlandırıldı.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)

    messages.append({"role": "assistant", "content": reply})
