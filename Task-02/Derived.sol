// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./Base.sol";

contract Derived is Base {
    string public data;

    function setData(string memory _data) public onlyOwner {
        data = _data;
    }
}
