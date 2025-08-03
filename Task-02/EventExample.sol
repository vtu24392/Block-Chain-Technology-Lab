// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EventExample {
    event Transfer(address indexed from, address indexed to, uint amount);

    function send(address to, uint amount) public returns (bool success, uint timestamp) {
        emit Transfer(msg.sender, to, amount);
        return (true, block.timestamp);
    }
}
