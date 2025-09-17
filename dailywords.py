#me and my brother decided to learn 5 words of our interested languages every day. mine is Italian.
#the code should print out the 5 italian words with their meanings.
#the words might not repeat if they've been learnt previous time.
#my guess for now is to create a dictionary of the italian words with English meanings, but it could be created with a bit of more complex way:
#for example, look out for the words in internet, and also find their meaning, and if the worls has already been leanrt, skip it.
import random

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
learn_words=[]

#remaining words
remaining_words = {k:v for k, v in words_dict.items() if k not in learn_words}

#pick 5 new words every time:
new_words=random.sample(list(remaining_words))
print(learn_words)
#ok, recheck tomorrow!