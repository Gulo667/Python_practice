#me and my brother decided to learn 5 words of our interested languages every day. mine is Italian.
#the code should print out the 5 italian words with their meanings.
#the words might not repeat if they've been learnt previous time.
#my guess for now is to create a dictionary of the italian words with English meanings, but it could be created with a bit of more complex way:
#for example, look out for the words in internet, and also find their meaning, and if the worls has already been leanrt, skip it.
import random
import os


words_dict={
    'Guarriera':'fighter',
    'zelante':'earnest',
    'preziosi':'precious',
    'filli di rame':'copper wires',
    'campana':'bell',
    'vedrai':"you'll see",
    'avanti':'forward',
    'diviso':'devided',
    'metà':'part',
    'un peso':'a weight',
    'spezzzre':'sweeping up-cleaning',
    'non vale niente':'its not worth it',
    'neanche':'neither',
    'misera':'miserable',
    'crescere':'drowing up',
    'mostro':'monster',
    'la tiene':'she holds',
    'gabbia':'cage',
    'ricoprire':'to cover',
    'la strada':'street',
    'la strada di mine':'the streets of mine',
    'vorrebbe':'would like',
    'sparire':'disappear',
    "l'ansia":'anxiety',
    'dentro':'inside',
    "un'ascia":'the axe',
    'un taglio':'a cut',
    'la schiena':'the back',
    'una zattera':'a raft - tivi qart',
    'un fiume in piena':'a raging river',
    'il fuoco':'the fire',
    'riparare':'repair',
    "riparo d'inverno":"winter shelter",
    "riparo":'shelter',
    "ciò che respiri":"what you breath",
    'il significato':"the meaning",
    "il significato del bene":'the meaning of good',
    'un soldato':"a soldier",
    "soltanto":"only",
    "lacrima":"tear",
    "sopra":"above",
    "vessillo":"banner-flag",
    "scudo":"shield",
    "la spada":"the sword",
    "la spada d'argento":"the silver sword",
    'ventre':"womb",
    'un padre che  di padre ha niente':"the father who has nothing of a father",
    "mura":"walls",
    "talmente":"so+very",
    "potenti":"powerful",
    "colpire":"hit",
    "colpirti":"hit you",
            }
#for the learnt words
LEARNED_FILE="learned.txt"

#load learned words from file if file exists
learn_words=[]
if os.path.exists(LEARNED_FILE):
    with open(LEARNED_FILE, 'r') as f:
        learn_words=[line.strip() for line in f if line.strip()]
#remaining words
remaining_words = [w for w in words_dict if w not in learn_words]

#pick 5 new words every time:
new_words=to_pick=min(5, len(remaining_words))
if to_pick==0:
    print("baby, you've already learned all the words, add more words and continue")
else:
    new_words=random.sample(remaining_words, to_pick)

#show the words and append to the file & list

print("Today's new words:")
with open(LEARNED_FILE, 'a') as opened_file:
    for i, w in enumerate(new_words, start=1):
        print(f"{i}. {w} - {words_dict[w]}")
        opened_file.write(w + "\n")
        learn_words.append(w)

print("\nUpdated leaned words count:", len(learn_words))