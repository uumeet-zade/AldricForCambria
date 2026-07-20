import json
import urllib.request
import urllib.parse
import time

lang_map = {
    'ga': 'fr',
    'ac': 'es',
    'ra': 'da',
    'my': 'cy',
    'au': 'lv',
    'le': 'de'
}

def batch_translate(texts, target_lang):
    if not texts:
        return []
    
    # Google Translate has limits on POST body size (usually ~5000 chars), so we might need to chunk
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t"
    
    translated_texts = []
    
    # Chunk texts to avoid URI too long / POST body too big
    chunk_size = 20
    for i in range(0, len(texts), chunk_size):
        chunk = texts[i:i+chunk_size]
        
        # Build POST data with multiple q parameters
        qs = "&".join([f"q={urllib.parse.quote(t)}" for t in chunk])
        
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, data=qs.encode('utf-8'), headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    result = json.loads(response.read().decode('utf-8'))
                    
                    # Google returns an array of arrays. Sometimes grouped weirdly.
                    # Usually result[0] contains the translations.
                    # If multiple q params were passed, result[0] has multiple items, each corresponding to a chunk of text.
                    # Wait, if a single 'q' is long, it splits it into multiple sentences.
                    # So passing multiple 'q's actually mixes them up if we're not careful.
                    # A safer batch method: join with a unique separator.
                    break
            except Exception as e:
                print(f"Error: {e}, retrying...")
                time.sleep(2)
                
    return translated_texts

# Since multiple 'q' params can be unreliable to parse back, we will join with a separator.
def separator_translate(texts, target_lang):
    separator = " |~| "
    translated_texts = []
    
    chunk_size = 15
    for i in range(0, len(texts), chunk_size):
        chunk = texts[i:i+chunk_size]
        combined = separator.join(chunk)
        
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t"
        qs = f"q={urllib.parse.quote(combined)}"
        
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, data=qs.encode('utf-8'), headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    result = json.loads(response.read().decode('utf-8'))
                    translated_combined = "".join([sentence[0] for sentence in result[0]])
                    
                    # Split back
                    parts = translated_combined.split(" |~| ")
                    if len(parts) == len(chunk):
                        translated_texts.extend([p.strip().replace('—', '-') for p in parts])
                    else:
                        # Fallback: if separator gets mangled, split using a regex or fallback to 1-by-1
                        print("Separator mangled! Falling back to 1-by-1 for this chunk.")
                        for t in chunk:
                            translated_texts.append(single_translate(t, target_lang))
                    break
            except Exception as e:
                print(f"Error: {e}, retrying...")
                time.sleep(2)
                
    return translated_texts

def single_translate(text, target_lang):
    if not text.strip(): return text
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t&q={urllib.parse.quote(text)}"
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                result = json.loads(response.read().decode('utf-8'))
                translated = "".join([sentence[0] for sentence in result[0]])
                return translated.replace('—', '-')
        except:
            time.sleep(1)
    return text

print("Loading source dictionary...")
with open('data/new_source.json', 'r', encoding='utf-8') as f:
    source_dict = json.load(f)

final_data = {'al': source_dict}
keys = list(source_dict.keys())
values = [source_dict[k] for k in keys]

for target_key, lang_code in lang_map.items():
    print(f"Translating to {target_key} ({lang_code})...")
    final_data[target_key] = {}
    
    translated_values = separator_translate(values, lang_code)
    
    for k, v in zip(keys, translated_values):
        final_data[target_key][k] = v

print("Writing new_translations.json...")
with open('data/new_translations.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, indent=2, ensure_ascii=False)

print("Translations complete!")
