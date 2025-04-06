# Speech Recognition with Whisper

Bu proje, OpenAI'nin Whisper modeli kullanılarak ses dosyalarını yazıya çevirmek için geliştirilmiştir.

## Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- `whisper`
- `torch`
- `ffmpeg`

Bu kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install openai-whisper torch ffmpeg-python
```

## Modelin Yüklenmesi
Whisper, farklı boyutlarda modeller sunmaktadır:
- `tiny`
- `base`
- `small`
- `medium`
- `large`

Bu projede varsayılan olarak `medium` modeli kullanılmaktadır. Farklı bir model kullanmak için aşağıdaki satırı değiştirebilirsiniz:

```python
model = whisper.load_model("medium")
```

Örneğin, daha hızlı ama düşük doğruluk oranına sahip bir model istiyorsanız:

```python
model = whisper.load_model("small")
```

## Kullanım
1. `speech_recognition.py` dosyasını açın.
2. `audio_path` değişkenini kendi ses dosyanızın tam yolu ile değiştirin:
   
   ```python
   audio_path = "C:/Users/Muhammed Fatih/Desktop/audio.mp3"
   ```

3. Python dosyasını çalıştırın:

   ```bash
   python speech_recognition.py
   ```

4. Çıktılar konsolda görüntülenecektir.
   - Ses kaydının yazıya dökülmüş hali
   - Alternatif olarak İngilizceye çevirilmiş hali
   - Ses kaydının dili

## Çıktı Örneği
```text
Bu bir test ses kaydıdır.
This is a test audio recording.
tr
```

## Ekstra Özellikler
- Ses kaydını farklı bir dile çevirebilirsiniz:
  ```python
  result2 = model.transcribe(audio_path, language='en')
  ```
- Ses kaydının dilini otomatik olarak algılamak için:
  ```python
  dil = result['language']
  ```

## Whisper Hakkında
Whisper, OpenAI tarafından geliştirilmiş geniş kapsamlı bir konuşma tanıma modelidir. Çok dilli konuşma tanıma, konuşma çevirisi ve dil tanımlama gibi görevleri gerçekleştirebilir. Model, büyük ölçekli denetimli ve zayıf denetimli veri kümeleri kullanılarak eğitilmiştir ve geniş bir konuşma işleme yeteneğine sahiptir.

Daha fazla bilgi ve güncellemeler için Whisper'ın resmi GitHub sayfasını ziyaret edebilirsiniz: [https://github.com/openai/whisper](https://github.com/openai/whisper)

