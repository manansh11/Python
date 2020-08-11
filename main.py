from Block import Block



genesis_block = Block("Chancellor on the brink...", ["Satoshi sent 1 BTC to Sam",
                                                     "Maria sent 5 BTC to Jen", 
                                                     "Satoshi sent 10 BTC to Fin"])

second_block = Block(genesis_block.block_hash, ["Manansh sent 5 BTC to Max",
                                                "John sent 10 BTC to Arnold"])

third_block = Block(second_block.block_hash, ["Alex sent 2 BTC to Siakam",
                                                "Arthur sent 10 BTC to Merlin",
                                                "Mac sent 0.22 BTC to Alice"])


print("Block Hash: Genesis Block\n")
print(genesis_block.block_hash + "\n")


print("Block hash: Second Block\n")
print(second_block.block_hash + "\n")


print("Block hash: Third Block\n")
print(third_block.block_hash + "\n")