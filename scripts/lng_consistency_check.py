""" This script simply checks if other lng files' entries are inconsistent against core "english.lng" """

import os
from collections import defaultdict
from pathlib import Path
import chardet
from jsondiff import diff


current_path = Path(__file__).parent.resolve()
print(current_path)


if __name__ == "__main__":
    parsed = {}
    lng_files_path = current_path.parent

    for file in os.listdir(lng_files_path):
        file_name, ext = os.path.splitext(file)
        file = os.path.join(lng_files_path, file)
        if os.path.isfile(file) and ext.lower() == '.lng':
            detected_encoding = 'utf-8'
            with open(file, 'rb') as f:
                detected_encoding = chardet.detect(f.read())['encoding']
            with open(file, 'r', encoding=detected_encoding) as f:
                parsed[file_name] = parsed_file = defaultdict(list)
                current_section = ''
                for line in f.readlines():
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith('#'):
                        continue
                    if line.startswith('['):
                        current_section = line[1:-1]
                        continue
                    parsed_file[current_section].append(line.split('=', 1)[0])

    print(f"{len(parsed)} languages detected!")
    parsed_language_english = parsed['english']
    inconsistencies = []
    for language_name, parsed_language in parsed.items():
        d = diff(parsed_language, parsed_language_english)
        if d:
            inconsistencies.append((language_name, d))
            print(language_name + '.lng', d)
    if inconsistencies:
        print('Inconsistent entries found and are listed above, please fix.')
    else:
        print('All language files have consistent entries. No action needed.')
