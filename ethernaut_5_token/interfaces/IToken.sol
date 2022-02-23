pragma solidity 0.8.8;

interface IToken {
    function transfer(address _to, uint256 _value) external returns(bool);
    function balanceOf(address _owner) external view returns(uint256);
}