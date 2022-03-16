// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PriceConsumerV3 {

    AggregatorV3Interface internal priceFeed;

    /**
     * Network: Binance Smart Chain
     * Aggregator: BNB/USD
     * Address: 0x137924D7C36816E0DcAF016eB617Cc2C92C05782
     */
    constructor() {
        priceFeed = AggregatorV3Interface(0x137924D7C36816E0DcAF016eB617Cc2C92C05782);
    }

    /**
     * Returns the latest price
     */
    function getLatestPrice() public view returns (int) {
        (
            /*uint80 roundID*/,
            int price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();
        return price;
    }
}
