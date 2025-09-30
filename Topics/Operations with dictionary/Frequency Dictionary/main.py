# put your python code here
def words_count(sentence):
    new_dict = {word: sentence.count(word) for word in sentence}
    for word, appearance in new_dict.items():
        print(word, appearance)


words_count(input().lower().split())
