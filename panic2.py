phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# transform the phrase into 'on tap'
plist = plist[1:-4]
plist.remove("'")
plist = plist[:2] + plist[-3:-5:-1] + plist[:-3:-1]

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)