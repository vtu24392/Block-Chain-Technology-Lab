// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ErrorDemo {
    uint public balance;

    function deposit(uint amount) public {
        require(amount > 0, "Amount must be > 0");
        balance += amount;
    }

    function validate() public view {
        assert(balance >= 0);
    }

    function withdraw(uint amount) public {
        if (amount > balance) {
            revert("Insufficient balance");
        }
        balance -= amount;
    }
}
