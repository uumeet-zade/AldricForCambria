import json
from deep_translator import GoogleTranslator
import time

lang_map = {
    'ga': 'fr',
    'ac': 'es',
    'ra': 'da',
    'my': 'cy',
    'au': 'lv',
    'le': 'de'
}

print("Loading source dictionary...")
with open('data/new_source.json', 'r', encoding='utf-8') as f:
    source_dict = json.load(f)

final_data = {'al': source_dict}
keys = list(source_dict.keys())
values = list(source_dict.values())

for target_key, lang_code in lang_map.items():
    print(f"Translating to {target_key} ({lang_code})...")
    final_data[target_key] = {}
    
    translator = GoogleTranslator(source='en', target=lang_code)
    
    # We can batch translate in chunks to avoid HTTP errors
    chunk_size = 20
    translated_values = []
    
    for i in range(0, len(values), chunk_size):
        chunk = values[i:i+chunk_size]
        try:
            # deep-translator supports translate_batch
            t_chunk = translator.translate_batch(chunk)
            translated_values.extend(t_chunk)
            time.sleep(1)  # tiny sleep to prevent immediate rate limit
        except Exception as e:
            print(f"Error on chunk {i}: {e}")
            # If rate limited, just return the original English text
            for v in chunk:
                translated_values.append(f"[{lang_code.upper()}] {v}")
    
    for k, v in zip(keys, translated_values):
        # Apply the no em-dash rule
        if v: v = v.replace('—', '-')
        final_data[target_key][k] = v

print("Writing new_translations.json...")
with open('data/new_translations.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, indent=2, ensure_ascii=False)

print("Translations complete!")
