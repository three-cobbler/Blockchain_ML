# -*- coding: utf-8 -*-
def addBlock(self, block):
    if self.chaincodeID != chaincodeID:
        raise Exception('block info should have been {0} but was {1}'\
                        .format(self.chaincodeID, chaincodeID))
         
    if self.block.nonHashData.PreviousHash != bcInfo.CurrentBlockHash:
        raise Exception('unexpected Previous block hash. Expected PreviousHash {0},\
                       PreviousHash referred in the latest block= {1}'\
                       .format(block.nonHashData.PreviousHash,bcInfo.CurrentBlockHash))

   # hash
   blockHash := block.HashData.Hash()
   
   #check block size before add new one
   def check_block_size():
   
   #update checkpoint info
   def update_checkpoint():
   #save the checkpoint info to database, update block index in database, update checkpoint info to manager node
   def save()

Class Trasaction:
    def __init__(self,):
    
    transactions_type = {'UNDEFINED' : 0,
                    # deploy a chaincode to the network
                    'CHAINCODE_DEPLOY' : 1,
                    # call a invoke function as a transaction initialization
                    'CHAINCODE_INVOKE' = 2,
                    # call a chaincode query function
                    'CHAINCODE_QUERY' = 3,
                    # terminate a chaincode, stash it, may implement at later time
                    'CHAINCODE_TERMINATE' = 4;
            }

    #store ChaincodeID for encryption
    chaincodeID = 2;
    metadata = 4;
    uuid = 5;
    google.protobuf.Timestamp timestamp = 6;
    ConfidentialityLevel confidentialityLevel = 7;
    confidentialityProtocolVersion = 8;
    nonce = 9;
    toValidators = 10;
    cert = 11;
    signature = 12;
    
Class nonHashData()
    def __init__(self,localCommitTimestamp = '', nanos = 0, seconds = 0):
        self.localCommitTimestamp = localCommitTimestamp
        self.nanos = nanos
        self.seconds = seconds

Class compare():
    def __init__():
    
    def get_diff(commit1, commit2):
    
    def get_evaluate(score1, score2):

       
Class Block:
    def __init__(self, nonHashData, results, uuid, previousBlockHash, stateHash):
        self.nonHashData = nonHashData
        self.results = results
        self.uuid = uuid
        self.previousBlockHash = previousBlockHash
        self.stateHash = stateHash
    #deployment
    def get_chaincodeID():
    
    #including code changs, metric, and metadata
    def get_metadata():
    
    def get_deploy_timestep():
        return timestamp, nanos, seconds, transactions_type, uuid

Class Message:
    def __init__():
    
    UNDEFINED = 0
    DISC_HELLO = 1
    DISC_DISCONNECT = 2
    DISC_GET_PEERS = 3
    DISC_PEERS = 4
    DISC_NEWMSG = 5
    CHAIN_STATUS = 6
    CHAIN_TRANSACTION = 7
    CHAIN_GET_TRANSACTIONS = 8
    CHAIN_QUERY = 9
    SYNC_GET_BLOCKS = 11
    SYNC_BLOCKS = 12
    SYNC_BLOCK_ADDED = 13
    SYNC_STATE_GET_SNAPSHOT = 14
    SYNC_STATE_SNAPSHOT = 15
    SYNC_STATE_GET_DELTAS = 16
    SYNC_STATE_DELTAS = 17
    RESPONSE = 20
    CONSENSUS = 21
    
    transactions_type = 1
    timestamp = 3;
}
