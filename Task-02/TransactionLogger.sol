// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransactionLogger {
    struct Transaction {
        address from;
        address to;
        uint amount;
    }

    mapping(uint => Transaction) public transactions;
    uint public txCount;

    function logTransaction(address _to, uint _amount) public {
        transactions[txCount] = Transaction(msg.sender, _to, _amount);
        txCount++;
    }
}
