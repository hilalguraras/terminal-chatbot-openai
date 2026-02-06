# Terminal Chatbot (OpenAI GPT-4o-mini)

Bu proje, terminal (konsol) üzerinden kullanıcıdan girdi alarak OpenAI'nin **gpt-4o-mini** modeli ile etkileşimli sohbet gerçekleştiren basit bir chatbot uygulamasıdır.

## Projenin Amacı
- OpenAI API kullanımını öğrenmek
- Terminal üzerinden etkileşimli bir Python uygulaması geliştirmek
- Ortam değişkenleri (.env) ile güvenli API anahtarı yönetimini uygulamak
- Mesaj geçmişi (conversation history) mantığını kavramak

## Kullanılan Teknolojiler
- Python
- OpenAI Python SDK
- python-dotenv
- uv (virtual environment & dependency management)

## Proje Yapısı
terminal-chatbot-openai/
│── main.py
│── .gitignore
│── .env.example
│── README.md


## Kurulum

### 1. Gerekli paketler
```bash
pip install uv
uv venv
.venv\Scripts\activate
uv add openai python-dotenv

#### 2. API Key Tanımlama

Proje dizininde .env dosyası oluşturun ve aşağıdaki gibi API anahtarınızı ekleyin:
OPENAI_API_KEY=YOUR_API_KEY
Not: Güvenlik sebebiyle .env dosyası GitHub reposuna eklenmemektedir.

### Çalıştırma
Uygulamayı başlatmak için:
python main.py

### Uygulamadan çıkmak için terminale:
exit
veya
quit

 
### Nasıl Çalışır?

Uygulama terminalden kullanıcı girdisi alır

Kullanıcı ve asistan mesajları bir liste içinde saklanır

Her yeni mesaj, önceki konuşma geçmişiyle birlikte modele gönderilir

Modelden alınan cevap terminalde gösterilir ve geçmişe eklenir

Bu sayede sohbet bağlamı korunur

### Geliştirme Fikirleri

Streaming (parça parça) cevap alma

Konuşma geçmişini sıfırlama komutu

Token ve mesaj uzunluğu kontrolü

Sohbet kayıtlarını dosyaya yazma

















