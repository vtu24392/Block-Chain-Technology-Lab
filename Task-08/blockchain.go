type Blockchain struct {
	Blocks []*Block
}

funcNewBlockchain() *Blockchain {
	genesisBlock := NewBlock("Genesis Block", []byte{})
	pow := NewProofOfWork(genesisBlock)
	nonce, hash := pow.Run()
	genesisBlock.Hash = hash
	genesisBlock.Nonce = nonce
	return&Blockchain{[]*Block{genesisBlock}}
}

func(bc *Blockchain) AddBlock(data string) {
	prevBlock := bc.Blocks[len(bc.Blocks)-1]
	newBlock := NewBlock(data, prevBlock.Hash)
	pow := NewProofOfWork(newBlock)
	nonce, hash := pow.Run()
	newBlock.Hash = hash
	newBlock.Nonce = nonce
	bc.Blocks = append(bc.Blocks, newBlock)
}
