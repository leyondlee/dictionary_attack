import hashlib
import uuid

global hashes
hashes = {}

#Usage: hashWord(<word>,<salt (optional)>)
#Return: hash value (String)
def hashWord(w,salt=''):
    w = w.lower() #Make all lowercase
    h = hashlib.sha512(salt + w).hexdigest()

    return h

#Usage: findHash(<word>)
#Return: hash (String)
def findHash(w):
    if hashes.has_key(w):
        print 'Hash for %s is %s' % (w,hashes[w])
    else:
        print 'Hash not found'

#Usage: findWord(<hash>)
#Return: word (String)
def findWord(h):
    word = ''

    #Find word associated with hash
    for w in hashes:
        if hashes[w] == h:
            word = w

    if word:
        print 'Word for %s is %s' % (h,word)
    else:
        print 'Word not found'

#Usage: getSalt()
#Return: salt (String)
def getSalt():
    salt = uuid.uuid4().hex
    
    return salt

#Usage: getSalt()
#Return: NIL
def generateTable(filename):
    f = None
    try:
        f = open(filename,'r')
    except:
        print 'Invalid file'
        exit()
        
    #Generate dictionary hashes
    count = 0
    for line in f:
        line = line.strip()
        h = hashWord(line)
        hashes[line] = h
        count = count + 1

    print '%d hashes generated and stored' % (count)

    f.close()
