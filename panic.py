phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# transform the phrase into 'on tap'
plist.pop(0)
plist.pop(2)
plist.remove(' ')
for i in range(4):
    plist.pop()
plist.insert(2, ' ')
plist.insert(4, plist.pop())
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)