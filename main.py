import os
# from fugashi import Tagger
from janome.tokenizer import Tokenizer


def get_dialogues_ass(file_name):
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


def get_dialogues_srt(file_name):
    dialogues = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0].isdigit():
                continue
            dialogues.append(line)
    return dialogues[1:]


# fugashi_tagger = Tagger("-Owakati")
janome_t = Tokenizer()


# def analyze_fugashi(phrase):
#     print(phrase)
#     for word in fugashi_tagger(phrase):
#         print(word)
#         print("Type:", word.feature.pos1)
#         print("Goshu:", word.feature.goshu)
#         # SHOW ALL FEATURES
#         # print(word.feature)
#         print()


def analyze_janome(phrase):
    print(phrase)
    for token in janome_t.tokenize(phrase):
        print(token)


animes = {
    "contemporain": {
        "nichijou": {
            "files": [(i, os.path.join(
                os.getcwd(),
                "nichijou",
                f"sub{str(i).zfill(3)}.srt",
            )) for i in range(1, 12 + 1)],
            "extractor": get_dialogues_srt,
        },
        "barakamon": {
            "files": [(i, os.path.join(
                os.getcwd(),
                "barakamon",
                f"[Kamigami] Barakamon - {str(i).zfill(2)} [1280×720 x264 AAC Sub(Chs,Jap)].ass",
            )) for i in range(1, 12 + 1)],
            "extractor": get_dialogues_ass,
        },
    },
    "edo": {},
    "contemporain_edo": {
        "inuyasha": {
            "files": [(i, os.path.join(
                os.getcwd(),
                "inuyasha",
                f"sub{str(i).zfill(3)}.srt",
            )) for i in range(1, 12 + 1)],
            "extractor": get_dialogues_srt,
        },
    },
}

with open("corpus.txt", "w") as f:
    for category, cat_animes in animes.items():
        f.write(f"<{category}>" + "\n\n")
        for anime, data in cat_animes.items():
            f.write(f"<{anime}>" + "\n\n")
            files = data["files"]
            get_dialogues = data["extractor"]
            for i, file in files:
                dialogues = get_dialogues(file)
                f.write(f"<episode{i}>" + "\n")
                for dialogue in dialogues:
                    f.write(dialogue + "\n")
                f.write(f"</episode{i}>" + "\n\n")
            f.write(f"</{anime}>" + "\n\n")
        f.write(f"</{category}>" + "\n\n")


# analyze_fugashi(dialogues[1])
