import whisper

# 5 farklı model bulunmakta
# tiny - base - small - medium - large
# soldan sağa gidildikçe metnin yazıya çevrilmesinin doğruluk oranı artıyor
# soldan sağa Ram kullanımı artıyor ve bağıl hız azalıyor
model = whisper.load_model("medium")

# Ses dosyasının tam yolunu belirtin
audio_path = "C:/Users/Muhammed Fatih/Desktop/audio.mp3"

# Ses kaydını yazıya çeviriyoruz
result = model.transcribe(audio_path)

# Ses kaydını ekrana bastırıyoruz
print(result["text"])

# Ses kaydını farklı bir dile çeviriyoruz (örneğin, İngilizce)
result2 = model.transcribe(audio_path, language='en')
print(result2["text"])

# Ses kaydının hangi dilde olduğunu buluyoruz
dil = result['language']
print(dil)
