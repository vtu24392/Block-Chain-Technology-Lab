// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract VariableDemo {
    uint public number = 10;
    string private name = "Blockchain";
    bool internal status;

    function getName() public view returns(string memory) {
        return name;
    }
}
