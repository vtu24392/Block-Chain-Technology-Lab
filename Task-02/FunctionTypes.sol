// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FunctionTypes {
    uint public x = 100;
    mapping(address => uint) public balances;
    uint public fallbackCalls;

    event Received(address indexed sender, uint amount);
    event FallbackCalled(address indexed sender, bytes data);

    function getX() public view returns (uint) {
        return x;
    }

    function calculate(uint a, uint b) public pure returns (uint) {
        return a + b;
    }

    receive() external payable {
        require(msg.value > 0, "No ETH sent");
        balances[msg.sender] += msg.value;
        emit Received(msg.sender, msg.value);
    }

    fallback() external payable {
        fallbackCalls += 1;
        emit FallbackCalled(msg.sender, msg.data);

        if (msg.value > 0) {
            payable(msg.sender).transfer(msg.value);
        }
    }
}
