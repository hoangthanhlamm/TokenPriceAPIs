class NetworkType:
    bsc = 'bsc'
    ethereum = 'ethereum'
    ftm = 'ftm'


class Chain:
    bsc = '0x38'
    ethereum = '0x1'
    ftm = '0xfa'

    mapping = {
        NetworkType.bsc: bsc,
        NetworkType.ethereum: ethereum,
        NetworkType.ftm: ftm
    }


class ProviderURI:
    bsc_provider_uri = 'https://bsc-dataseed.binance.org/'
    ethereum_provider_uri = 'https://mainnet.infura.io/v3/'
    ftm_provider_uri = 'https://rpc.ftm.tools/'

    mapping = {
        Chain.bsc: bsc_provider_uri,
        Chain.ethereum: ethereum_provider_uri,
        Chain.ftm: ftm_provider_uri
    }
