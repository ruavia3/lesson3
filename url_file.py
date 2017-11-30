import urllib
text = urllib.request.urlopen("www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt").read()
print(text)


#with open ('referat.txt','r', encoding ='utf-8') as f:
#    content = f.read()
#    words_qty = len(content.split())
#    print(words_qty)
