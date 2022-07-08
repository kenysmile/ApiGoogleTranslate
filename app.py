
import time
from google.cloud import translate
count = 0
file = open('file.txt', 'rb')
elapsed_time = 0
while True:
    st = time.time()
    chunk = file.read(30000)
    if len(chunk) == 0:
        break
    project_id="eminent-cache-354603"
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [chunk],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "vi",
        }
    )
    count = 0 
    if response:
    # Display the translation for each input text provided
        for translation in response.translations:
            print("Translated text {}: {}".format(count, translation.translated_text))
    et = time.time()
    elapsed_time += et - st
    print('Execution time:', elapsed_time, 'seconds')