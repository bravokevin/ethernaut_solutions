pragma solidity 0.8.8;

interface IDelegation {
    function owner() view external returns(address);
    function pwn() external;
}