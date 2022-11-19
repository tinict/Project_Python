from googletrans import Translator

# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',
#     ])
# translator.translate('안녕하세요');

def text_translator(Text):
    translator = Translator();
    translated = translator.translate(Text, src='ko');
    translated = translator.translate(Text, dest='en');
    return translated.text;

print(text_translator('안녕하세요'));

