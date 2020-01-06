# -*- coding: utf-8 -*-

class Blockchain(object):
        def valid_proof(prev_metrics, curr_metrics):
        """
        Validates the metrics: Does curr_metrics has a better or equal result?
        Returns: <bool> True if it does, False if not.
        """

        return curr_metrics >= prev_metrics
    
    def chain_valid(self, chain):
        """
        Returns: <bool> True if it is a valid chain, False if not.
        -------
        None.
        
        """

        prev_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            curr_block = chain[current_index]
            print(f'{prev_block}')
            print(f'{curr_block}')
            print("\n-----------\n")
            # Check the hash of the blocks are correct
            if block['previous_hash'] != self.hash(prev_block):
                return False

            # Check the Proof of Work is correct
            if not self.valid_proof(prev_block['metrics'], curr_block['metrics']):
                return False

            prev_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        Finding longest chain in the network

        Returns <bool> True if find one, then use this one as valid chain,
        return False if not.
        -------
        None.

        """

