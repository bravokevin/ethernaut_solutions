pragma solidity 0.8.8;

interface IVault {
    function unlock(bytes32 _password) external;
    function locked() view external returns(bool);
}