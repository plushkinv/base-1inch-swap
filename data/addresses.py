
ADDRESSES = {
    'ethereum': {
        'type': 2,
        'chainId': 1,
        'rpc': 'https://rpc.ankr.com/eth',
        "scan": "https://etherscan.io/tx",
        'ETH': 'native',
        'native': 'ETH',
        'TOKENS' : {
        }       

    },

    'polygon': {
        'type': 2,
        'chainId': 137,
        'rpc': 'https://polygon-rpc.com/',
        "scan": "https://polygonscan.com/tx",
        'MATIC': 'native',
        'native': 'MATIC',
        'lzChainId': 109,
        'TOKENS' : {
            'WMATIC': '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270',
            'USDC': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
            'USDT': '0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
        }       

    },

    'arbitrum': {
        'type': 2,
        'chainId': 42161,
        'rpc': 'https://arb1.arbitrum.io/rpc',
        "scan": "https://arbiscan.io/tx",
        'ETH': 'native',
        'native': 'ETH',
        'lzChainId': 110,
        'TOKENS' : {
            'WETH': '0x82af49447d8a07e3bd95bd0d56f35241523fbab1',
            'USDC': '0xff970a61a04b1ca14834a43f5de4533ebddb5cc8',
            'USDT': '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
        }          

    },
    'optimism': {
        'type': 2,
        'chainId': 10,
        'rpc': 'https://rpc.ankr.com/optimism',
        "scan": "https://optimistic.etherscan.io/tx",
        'ETH': 'native',
        'native': 'ETH',
        'lzChainId': 111,
        'TOKENS' : {
            'WETH': '0x4200000000000000000000000000000000000006',
            'USDC': '0x7f5c764cbc14f9669b88837ca1490cca17c31607',
        }          

    },
    'bsc': {
        'type': 0,
        'chainId': 56,
        'rpc': 'https://bscrpc.com',
        "scan": "https://bscscan.com/tx",
        'BNB': 'native',
        'native': 'BNB',
        'lzChainId': 102,
        'TOKENS' : {
            'WBNB': '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c',
            'BUSD': '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56',
            'USDT': '0x55d398326f99059ff775485246999027b3197955',
        }          

    },
    'fantom': {
        'type': 2,
        'rpc': 'https://rpc.ftm.tools/',
        "scan": "https://ftmscan.com/tx",
        'FTM': 'native',
        'native': 'FTM',
        'lzChainId': 112,
        'TOKENS' : {
            'FTM': "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
            'WFTM': '0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83',
            'USDC': '0x04068DA6C83AFCFA0e13ba15A6696662335D5B75',
        }

    },
    'avax': {
        'type': 2,    
        'chainId': 43114,    
        'rpc': 'https://api.avax.network/ext/bc/C/rpc',
        'scan': "https://snowtrace.io/tx",
        'AVAX': 'native',
        'native': 'AVAX',
        'lzChainId': 106,
        'TOKENS' : {
            'WAVAX': '0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7',
            'USDC': '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E',
            'USDT': '0x9702230a8ea53601f5cd2dc00fdbc13d4df4a8c7',
        }

    },
    'aptos': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 108,
        'ghost_contract': '',
        'TOKENS' : {
        }

    },
    'dfk': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 115,
        'ghost_contract': '',
        'TOKENS' : {
        }

    },
    'harmony': {
        'type': 2,        
        'rpc': 'https://api.harmony.one',
        'ONE': 'native',
        'native': 'ONE',         
        'lzChainId': 116,
        'TOKENS' : {
        }

    },
    'dexalot': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 118,
        'ghost_contract': '',
        'TOKENS' : {
        }

    },
    'celo': {
        'type': 0,  
        'chainId': 42220,       
        'rpc': 'https://rpc.ankr.com/celo',
        'scan': "https://explorer.celo.org/mainnet/tx",
        'CELO': 'native',
        'native': 'CELO',          
        'lzChainId': 125,
        'TOKENS' : {
        }

    },
    'moonbeam': {
        'type': 2,
        'chainId': 1284,     
        'rpc': 'https://rpc.api.moonbeam.network',
        'scan': "https://moonscan.io/tx",
        'GLMR': 'native',
        'native': 'GLMR',          
        'lzChainId': 126,
        'TOKENS' : {
        }

    },
    'fuse': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 138,
        'ghost_contract': '',
        'TOKENS' : {
        }

    },
    'gnosis': {
        'type': 2,  
        'chainId': 100,        
        'rpc': 'https://1rpc.io/gnosis',
        'scan': 'https://gnosisscan.io/tx',
        'XDAI': 'native',
        'native': 'XDAI',          
        'lzChainId': 145,
        'TOKENS' : {
        }

    },
    'klaytn': {
        'type': 2,
        'chainId': 8217,   
        'rpc': 'https://rpc.ankr.com/klaytn',
        'scan': 'https://klaytnscope.com/tx',
        'KLAY': 'native',
        'native': 'KLAY',          
        'lzChainId': 150,
        'TOKENS' : {
        }

    },
    'metis': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 151,
        'TOKENS' : {
        }

    },
    'coredao': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 153,
        'TOKENS' : {
        }

    },
    'okt': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 155,
        'TOKENS' : {
        }

    },
    'canto': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 159,
        'TOKENS' : {
        }

    },
    'zkevm': {
        'type': 0,   
        'chainId': 1101,      
        'rpc': 'https://rpc.ankr.com/polygon_zkevm',
        'scan': 'https://zkevm.polygonscan.com/tx/',
        'ETH': 'native',
        'native': 'ETH',          
        'lzChainId': 158,
        'TOKENS' : {
        }

    },
    'zksyncera': {
        'type': 0,  
        'chainId': 324,
        'rpc': 'https://rpc.ankr.com/zksync_era',
        'scan': 'https://explorer.zksync.io/tx/',
        'ETH': 'native',
        'native': 'ETH',
        'lzChainId': 165,
        'TOKENS' : {
            "ETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
            "WETH": "0x5aea5775959fbc2557cc8789bc1bf90a239d9a91",
            "USDC": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4",
            "USDT": "0x493257fd37edb34451f62edf8d2a0c418852ba4c",
            "BUSD": "0x2039bb4116b4efc145ec4f0e2ea75012d6c0f181",
        }

    },
    'base': {
        'type': 2,        
        'chainId': 8453,
        'rpc': 'https://rpc.ankr.com/base',
        "scan": "https://basescan.org/tx",
        'ETH': 'native',
        'native': 'ETH',        
        'lzChainId': 184,
        'TOKENS' : {
        }

    },
    'linea': {
        'type': 2,        
        'rpc': 'https://rpc.linea.build',
        "scan": "https://lineascan.build/tx",
        'ETH': 'native',
        'native': 'ETH',        
        'lzChainId': 183,
        'TOKENS' : {
        }

    },
    'scroll': {
        'type': 0,    
        'chainId': 534352,    
        'rpc': 'https://rpc.ankr.com/scroll',
        "scan": "https://scrollscan.com/tx",
        'ETH': 'native',
        'native': 'ETH',        
        'lzChainId': 214,
        'TOKENS' : {
        }

    },
    'moonriver': {
        'type': 2,        
        'rpc': 'https://moonriver.publicnode.com',
        'scan': "https://moonriver.moonscan.io/tx",
        'MOVR': 'native',
        'native': 'MOVR',          
        'lzChainId': 167,
        'TOKENS' : {
        }

    },
    'tenet': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 173,
        'TOKENS' : {
        }

    },

    'meter': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 176,
        'TOKENS' : {
        }

    },
    'sepolia': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 161,
        'TOKENS' : {
        }

    },
    'kava': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 177,
        'TOKENS' : {
        }

    },
    'XPLA': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 216,
        'TOKENS' : {
        }

    },
    'Horizen': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 215,
        'TOKENS' : {
        }

    },
    'Orderly': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 213,
        'TOKENS' : {
        }

    },
    'Telos': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 199,
        'TOKENS' : {
        }

    },
    'Conflux': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 212,
        'TOKENS' : {
        }

    },
    'Aurora': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 211,
        'TOKENS' : {
        }

    },
    'Astar': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 210,
        'TOKENS' : {
        }

    },
    'opBNB': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 202,
        'TOKENS' : {
        }

    },
    'TomoChain': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 196,
        'TOKENS' : {
        }

    },
    'zora': {
        'type': 0,        
        'rpc': 'https://rpc.zora.energy',
        "scan": "https://zora.superscan.network/tx",
        'ETH': 'native',
        'native': 'ETH',           
        'lzChainId': 195,
        'TOKENS' : {
        }

    },
    'Loot': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 197,
        'TOKENS' : {
        }

    },
    'mantle': {
        'type': 0,        
        'rpc': 'https://mantle-mainnet.public.blastapi.io',
        "scan": "https://explorer.mantle.xyz/tx",
        'MNT': 'native',
        'native': 'MNT',        
        'lzChainId': 181,
        'TOKENS' : {
        }

    },

    'blast': {
        'type': 0,        
        'rpc': 'https://blast.blockpi.network/v1/rpc/public',
        "scan": "https://blastscan.io/tx",
        'ETH': 'native',
        'native': 'ETH',        
        'lzChainId': 243,
        'TOKENS' : {
        }

    },

    'nova': {
        'type': 2,        
        'rpc': 'https://arbitrum-nova.drpc.org',
        "scan": "https://nova.arbiscan.io/tx",
        'ETH': 'native',
        'native': 'ETH',        
        'lzChainId': 42170,
        'TOKENS' : {
        }
    },

    'mode': {
        'type': 0,        
        'rpc': 'https://1rpc.io/mode',
        "scan": "https://modescan.io/tx",
        'ETH': 'native',
        'native': 'ETH',        
        'lzChainId': 34443,
        'TOKENS' : {
        }
    },

}





ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'
