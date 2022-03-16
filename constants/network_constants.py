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
    bsc_provider_uri = 'https://nd-384-319-366.p2pify.com/7e49b20f53222da5f0b4517cd1da43ef'
    ethereum_provider_uri = 'https://nd-892-894-739.p2pify.com/175a62ad96c3a9422c55f877b9ab366e'
    ftm_provider_uri = 'https://nd-805-726-483.p2pify.com/d0a55e92a30ac535e1334e1f74196736'

    mapping = {
        Chain.bsc: bsc_provider_uri,
        Chain.ethereum: ethereum_provider_uri,
        Chain.ftm: ftm_provider_uri
    }
