package main

import (
	"bytes"
	"crypto/sha256"
	"fmt"
	"strconv"
	"time"
	)
const difficulty = 2

type ProofOfWork struct {
	Block  *Block
	Target []byte
			}

funcNewProofOfWork(b *Block) *ProofOfWork {
	target := bytes.Repeat([]byte{0}, difficulty)
	return&ProofOfWork{b, target}
			}

func(pow *ProofOfWork) Run() (int, []byte) {
	var hash [32]byte
	var nonce int
	for {
		data := bytes.Join([][]byte{
			pow.Block.PrevHash,
			pow.Block.Data,
			[]byte(strconv.Itoa(int(pow.Block.Timestamp))),
			[]byte(strconv.Itoa(nonce)),
		}, []byte{})
		hash = sha256.Sum256(data)
		if bytes.HasPrefix(hash[:], pow.Target) {
			break
		} else {
			nonce++
		}
	}
	return nonce, hash[:]
}

func(pow *ProofOfWork) Validate() bool {
	data := bytes.Join([][]byte{
		pow.Block.PrevHash,
		pow.Block.Data,
		[]byte(strconv.Itoa(int(pow.Block.Timestamp))),
		[]byte(strconv.Itoa(pow.Block.Nonce)),
	}, []byte{})
	hash := sha256.Sum256(data)
	return bytes.HasPrefix(hash[:], pow.Target)
}
