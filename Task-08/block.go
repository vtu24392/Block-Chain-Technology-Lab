package main

import (
	"bytes"
	"crypto/sha256"
	"fmt"
	"strconv"
	"time"
	)
type Block struct {
	Timestamp     int64
	Data          []byte
	PrevHash      []byte
	Hash          []byte
	Nonce         int
		}

func(b *Block) SetHash() {
	timestamp := []byte(strconv.FormatInt(b.Timestamp, 10))
	headers := bytes.Join([][]byte{b.PrevHash, b.Data, timestamp}, []byte{})
	hash := sha256.Sum256(headers)
	b.Hash = hash[:]
}

funcNewBlock(data string, prevHash []byte) *Block {
	block := &Block{time.Now().Unix(), []byte(data), prevHash, []byte{}, 0}
	return block
}
