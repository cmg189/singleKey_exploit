import os

msgs = [ "It was the best of times it was the worst of times it was th",
         "e age of wisdom it was the age of foolishness it was the epo",
         "ch of belief it was the epoch of incredulity it was the seas",
         "on of Light it was the season of Darkness it was the spring ",
         "of hope it was the winter of despair we had everything befor",
         "e us we had nothing before us we were all going direct to He",
         "aven we were all going direct the other way in short the per",
         "iod was so far like the present period that some of its nois",
         "iest authorities insisted on its being received for good or ",
         "for evil in the superlative degree of comparison only The op",
         "ening paragraph from A Tale Of Two Cities by Charles Dickens" ]

def encrypt(pad, msg):
    return bytes([x ^ ord(y) for (x, y) in zip(pad, msg)]).hex()

pad = os.urandom(60)
ctxts = [encrypt(pad, m) for m in msgs]
print('\n'.join(ctxts))
