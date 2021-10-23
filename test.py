input_texts = []
target_texts = []
input_characters = set()
target_characters = set()

with open('french.txt', 'r', encoding='utf-8') as f:
    rows = f.read().split('\n')
# read first 10,000 rows from dataset
for row in rows[:20000]:
    # split input and target by '\t'=tab
    input_text, target_text = row.split('\t')
    print(input_text)
    print(target_text)
    # add '\t' at start and '\n' at end of text.
    target_text = '\t' + target_text + '\n'
    input_texts.append(input_text.lower())
    target_texts.append(target_text.lower())
    # split character from text and add in respective sets
    input_characters.update(list(input_text.lower()))
    target_characters.update(list(target_text.lower()))