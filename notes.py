import json
import hashlib

proof = 0
def make_a_proof(block_hash):
    while hashlib.sha256(f'{firstHash}{proof}'.encode()).hexdigest()[:4] != '0000':
        proof += 1
    return proof


firstTransaction = {
    'tim': -10,
    'steve' : 10
}

firstHash = hash(json.dumps(firstTransaction))

## make lots of guesses
# until we find the pattern we want

secondTransaction = {
    'javier': -20,
    'arpita': 20,
    'proof': make_a_proof(firstHash),
    'previous_hash': firstHash
}

secondHash = hash(json.dumps(secondTransaction))

thirdTransaction = {
    'joshua': -30,
    'jonathan': 30,
    'proof': make_a_proof(secondHash),
    'previous_hash': secondHash
}

thirdHash = hash(json.dumps(thirdTransaction))

# hashing functions aren't magin
# we look for a pattern by random tries
# we can quickly check for the pattern
# we can chain these blocks together to form a history
# a con artist has to do all that guesswork over again
# meanwhile the chain keeps growing
