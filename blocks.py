#Blockchain_Creation

import flask, jsonify
import datetime
import hashlib
import json

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')            #previous_hash is string as sha256 uses alphanumeric code. 
        
    def create_block(self, proof, previous_hash):
        block ={"index":len(self.chain) + 1,
                "timestamp": str(datetime.datetime.now()),
                "proof":proof,
                "previous_hash":previous_hash
                }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    