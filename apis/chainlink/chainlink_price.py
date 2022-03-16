from web3 import Web3

from artifacts.abi.data_feed_abi import DATA_FEED_ABI
from constants.network_constants import ProviderURI, Chain


def chain_link_price(data_feed_address, provider_uri=None, chain_id=None, block_number=None):
    if block_number is None:
        block_number = 'latest'

    if not provider_uri:
        provider_uri = ProviderURI.mapping[chain_id]

    w3 = Web3(Web3.HTTPProvider(provider_uri))
    contract = w3.eth.contract(w3.toChecksumAddress(data_feed_address), abi=DATA_FEED_ABI)
    latest_data = contract.functions.latestRoundData().call(block_identifier=block_number)

    decimals = contract.functions.decimals().call()

    price = latest_data[1] / 10 ** decimals
    updated_at = latest_data[3]
    return {'price': price, 'updated_at': updated_at}


if __name__ == '__main__':
    data = chain_link_price('0x137924D7C36816E0DcAF016eB617Cc2C92C05782', chain_id=Chain.bsc, block_number=16058215)
    print(data)
