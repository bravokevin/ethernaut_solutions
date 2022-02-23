pragma solidity 0.8.8;

interface ITelephone {
    function changeOwner(address _owner) external;
    function owner() view external;
}