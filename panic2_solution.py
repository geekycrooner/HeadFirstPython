phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# transform the phrase into 'on tap'
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)