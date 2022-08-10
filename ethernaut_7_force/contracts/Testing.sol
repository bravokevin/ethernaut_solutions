pragma solidity 0.8.0;

contract Testing {

    uint256 public myVar;

    function setMyVar(uint256 _newValue) external {
        myVar = _newValue;
    }
}
