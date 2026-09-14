# Day 17 14/9/26!

def main():
  print("=== Text Analyzer ===")
  text = get_string("Enter your text: \n\n")
  chars_count = characters(text)
  chars_no_space_count = characters_without_spaces(text)
  words_count = words(text)
  sentences_count = sentences(text)
  common_word, counter = most_common_word(text)
  print(f"\n\n=== Text Analysis ===\n\nCharacters (with spaces): {chars_count}\nCharacters (without spaces): {chars_no_space_count}\nWords: {words_count}\nSentences: {sentences_count}\n")
  print(f"Most common word: '{common_word}' ({counter} times)") if counter > 1 else print(f"Most common word: '{common_word}' ({counter} time)")

def get_string(prompt):
  while True:
    var = input(prompt)
    if not var.strip() or (var == '.' or var =='?' or var == '!' or var == ':' or var == ','):
      print("You need to type something!")
      continue
    break
    
  new_var = ' '.join(var.split())
  return new_var

def characters(txt):
  sum = 0
  
  for c in txt:
    sum += 1
    
  return sum

def characters_without_spaces(txt):
  sum = 0
  
  for c in txt:
    if c == ' ':
      continue
    sum += 1

  return sum

def words(txt):
  sum = len(txt.split())
  return sum

def sentences(txt):
  sum = 0

  for c in txt:
    if c in ['.', '?', '!']:
      sum += 1

  if txt[-1] not in ['.', '?', '!']:
    sum += 1
  
  return sum

def most_common_word(txt):
  new_txt = ""
  
  for c in txt:
    if c in ['.', '?', '!', ',', ':']:
      c = c.replace(c, "")
    new_txt += c

  new_txt = new_txt.lower()
  txt_list = list(new_txt.split())
  temp_dict = {}

  for i in range(len(txt_list)):
    if txt_list[i] not in temp_dict:
      temp_dict[f"{txt_list[i]}"] = 1
    else:
      temp_dict[f"{txt_list[i]}"] += 1

  max = 0
  common = ""

  for word, pop in temp_dict.items():
    if pop > max:
      max = pop
      common = word

  return common, max
  
main()