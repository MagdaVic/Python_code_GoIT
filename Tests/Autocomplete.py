from fast_autocomplete import AutoComplete

words = {'book': {}, 'burrito': {}, 'pizza': {}, 'pasta':{}}
autocomplete = AutoComplete(words=words)
print(autocomplete.search(word='b', max_cost=3, size=3))






from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

command_completer = WordCompleter(['add file', 'add', 'save', 'save file'],ignore_case=True)
text = prompt('Enter HTML: ', completer=command_completer)
# print('You said: %s' % text)

print(text)

