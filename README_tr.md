# 🎬 ASKTube: YouTube ile Sohbet!

YouTube videoları ile etkileşimli sohbet edebileceğiniz, video transkriptlerinden yapay zeka destekli yanıtlar alabileceğiniz bir Streamlit uygulaması.

![Banner](./img/app_banner.png)

## 🚀 Özellikler

- 🎤 YouTube videosunun transkriptini otomatik çıkarır (Whisper kullanır).
- 🤖 Kullanıcının sorduğu soruya, videodan elde edilen bilgilerle RAG (Retrieval Augmented Generation) yöntemiyle yanıt verir.
- 🔎 YouTube üzerinde anahtar kelime ile video arama desteği.
- 🌐 Gemini Pro ve OpenAI entegrasyonu.
- 🖥️ Modern ve kolay kullanımlı arayüz.

## 🛠️ Kurulum

1. **Depoyu klonlayın:**
   ```sh
git clone <repo-url>
cd vidChat
```
2. **Gerekli Python paketlerini yükleyin:**
   ```sh
pip install -r requirements.txt
```
3. **API anahtarlarınızı `.env` dosyasına ekleyin:**
   ```
openai_apikey=YOUR_OPENAI_API_KEY
google_apikey=YOUR_GOOGLE_API_KEY
```

## ▶️ Kullanım

```sh
streamlit run app.py
```

- **URL** sekmesinden bir YouTube video linki girin, sorunuzu yazın ve "Sor" butonuna tıklayın.
- Uygulama, videodan sesi indirip transkripte çevirir, ardından sorunuza videodan elde edilen bilgilerle yanıt verir.
- Yanıtın yanında, ilgili referans metinleri ve kaynakları da görebilirsiniz.

## 📁 Dosya Yapısı

- `app.py`: Streamlit arayüzü ve uygulama akışı.
- `videohelper.py`: Video transkript çıkarma ve YouTube arama fonksiyonları.
- `raghelper.py`: RAG ve LLM (Gemini Pro) ile yanıt üretimi.
- `youtubevideo.py`: YouTube video nesnesi tanımı.
- `requirements.txt`: Gerekli Python paketleri.

## 📋 Gereksinimler

- Python 3.8+
- OpenAI ve Google API anahtarları

## 🤝 Katkı

Katkıda bulunmak için lütfen bir pull request açın veya issue oluşturun.
