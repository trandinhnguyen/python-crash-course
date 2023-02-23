from pathlib import Path

path = Path('text/alice_in_wonderland.txt')


def common_word_count(word, content):
    print(f'"{word}": {content.lower().count(word)}')


def word_count(content):
    words = content.split(" ")
    print(f'Total: {len(words)}')


try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
else:
    word_count(content=content)
    common_word_count('the', content=content)
    common_word_count(' the', content=content)
    common_word_count('the ', content=content)
    common_word_count(' the ', content=content)
