funcmain() {
	bc := NewBlockchain()

	fmt.Println("Mining block 1...")
	bc.AddBlock("Block 1 Data")

	fmt.Println("Mining block 2...")
	bc.AddBlock("Block 2 Data")

	fmt.Println("\nBlockchain:")
	for _, block := range bc.Blocks {
		fmt.Printf("Timestamp: %d\n", block.Timestamp)
		fmt.Printf("Data: %s\n", block.Data)
		fmt.Printf("PrevHash: %x\n", block.PrevHash)
		fmt.Printf("Hash: %x\n", block.Hash)
		fmt.Printf("Nonce: %d\n\n", block.Nonce)
	}
}
