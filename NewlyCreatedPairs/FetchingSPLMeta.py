import json

import requests


def get_token_meta(token):
    url = 'https://api.solscan.io/v2/token/meta'
    params = {
        'token': str(token)
    }
    
    headers = {
        'authority': 'api.solscan.io',
        'accept': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'origin': 'https://solscan.io',
        'referer': 'https://solscan.io/',
        'Au-So':
            '26YJAvze2fF53w-ofzXPE14dNm0xDiuF0ZEmiCS',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    
    response = requests.get(url, params = params, headers = headers)
    return response.json()


def get_token_metav2(token):
    url = 'https://api.solscan.io/v2/account'
    params = {
        'address': str(token)
    }
    
    headers = {
        'authority': 'api.solscan.io',
        'accept': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'origin': 'https://solscan.io',
        'referer': 'https://solscan.io/',
        'Au-So': 'WS7Zr-Avze2fFuj5jJIokTnkiqsteU4Fxz=yzqe',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    
    response = requests.get(url, params = params, headers = headers)
    return response.json()


if __name__ == '__main__':
    pass
    # 示例用法
    token = 'EKBd3r4ZYwWaA34KnMvQS827ovnyRYx2rGwWqEvf1GEb'
    token_meta = get_token_metav2(token)
    print(token_meta)
    print(json.dumps(token_meta, indent = 4))
