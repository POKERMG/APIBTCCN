#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
MG
"""
from __future__ import unicode_literals
from python.oauth import RequestClient


def get_account():
    request_client = RequestClient(
            api_key='7DA46FDC6137469AA66F7D290DD20EB588',
            secret_key='8E43321141D8EE9D4C6E9A65BA827A441CCB2D05B9FF21CD809A57A'
    )
    result = request_client.request('GET', 'https://www.viabtc.cn/api/v1/balance/')
    return result


if __name__ == '__main__':
    get_account()
