import logging
from typing import Any

from tronapi import Tron


class TronClient:
    """
    访问tron 链客户端
    """

    def __init__(self):
        full_node = 'https://api.trongrid.io'
        solidity_node = 'https://api.trongrid.io'
        event_server = 'https://api.trongrid.io'
        self.tron = Tron(full_node=full_node,
                         solidity_node=solidity_node,
                         event_server=event_server)

    def get_block_hash(self, block_height: Any = None):
        """
        根据区块高度查询区块 id

        :param block_height:  区块高度
        :return: 区块hash
        """
        if block_height is None:
            block = self.tron.trx.get_current_block()
        else:
            block = self.tron.trx.get_block(block_height)

        block_id = block['blockID']
        block_height = block['block_header']['raw_data']['number']
        logging.info('block:%s', block_id)
        logging.info('block:%s', block_height)
        return block_id


if __name__ == '__main__':
    tc = TronClient()
    print(tc.get_block_hash(42775311))
