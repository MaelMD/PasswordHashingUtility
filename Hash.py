from passlib.hash import pbkdf2_sha256
from base64 import b64decode
from passlib.utils.binary import ab64_encode

def hashAndCompare(crackedHash):
    
    crackedChain = crackedHash.split('$')   
    #crackedChainDigest = crackedChain[0]
    crackedChainRounds = crackedChain[1]
    crackedChainSalt = crackedChain[2]
    crackedChainSaltPasslibFormat = ab64_encode(crackedChainSalt.encode('utf8')).decode('utf8')
    crackedChainHashData = crackedChain[3].split(':')
    crackedChainHash = crackedChainHashData[0]
    crackedChainHashPasslibFormat = ab64_encode(b64decode(crackedChainHash)).decode('utf8')
    crackedChainData = crackedChainHashData[1]
    
    passlibHash = pbkdf2_sha256.hash(crackedChainData, rounds=crackedChainRounds, salt=crackedChainSalt.encode('utf8')) 
    passlibChain = passlibHash.split('$')
    passlibChainSalt = passlibChain[3]
    passlibChainHash = passlibChain[4]
    
    print('Passlib: Hash: {0} Salt: {1}\nCracked: Hash: {2} Salt: {3}\n'.format(passlibChainHash, passlibChainSalt, crackedChainHashPasslibFormat, crackedChainSaltPasslibFormat))

hashAndCompare('Hash=:Supected-Password')
