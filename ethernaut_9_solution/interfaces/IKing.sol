pragma solidity 0.8.8;

interface IKing {
    function _king() view external returns(address payable);
    function prize() view external returns(uint256);
}