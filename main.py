import os
from fugashi import Tagger
from janome.tokenizer import Tokenizer


def get_dialogues(file_name):
    dialogues = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.startswith("Dialogue:"):
                continue
            if "{" in line:
                continue
            dialogue = line.split(",")[-1].strip()
            if dialogue == "":
                continue
            dialogues.append(dialogue)
    return dialogues


fugashi_tagger = Tagger("-Owakati")
janome_t = Tokenizer()


def analyze_fugashi(phrase):
    print(phrase)
    for word in fugashi_tagger(phrase):
        print(word)
        print("Type:", word.feature.pos1)
        print("Goshu:", word.feature.goshu)
        # SHOW ALL FEATURES
        # print(word.feature)
        print()


def analyze_janome(phrase):
    print(phrase)
    for token in janome_t.tokenize(phrase):
        print(token)


file_name = os.path.join(
    os.getcwd(),
    "ass",
    "snk01.ass",
)

dialogues = get_dialogues(file_name)
# for dialogue in dialogues:
#     print(dialogue)

analyze_fugashi(dialogues[1])
