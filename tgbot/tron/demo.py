import json
import logging

from tronapi import Tron

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)

account = tron.create_account
# is_valid = bool(tron.trx.is_address(account.address.hex))

logger.debug('Generated account: ')
logger.debug('- Private Key: ' + account.private_key)
logger.debug('- Public Key: ' + account.public_key)
logger.debug('- Address: ')
logger.debug('-- Base58: ' + account.address.base58)
# logger.debug('-- Hex: ' + account.address.hex)
logger.debug('-----------')

transaction = tron.trx.get_transaction('38d14c8b403e64ba84b7591b1c6e1fba8124b8d9e263ae403e1a64531aabc145')

logger.debug('Transaction: ')
logger.debug('- Hash: ' + transaction['txID'])
logger.debug('- Transaction: ' + json.dumps(transaction, indent=2))
logger.debug('-----------')

# Events
# event_result = tron.trx.get_event_result('TGEJj8eus46QMHPgWQe1FJ2ymBXRm96fn1', 0, 'Notify')
#
# logger.debug('Event result:')
# logger.debug('Contract Address: TGEJj8eus46QMHPgWQe1FJ2ymBXRm96fn1')
# logger.debug('Event Name: Notify')
# logger.debug('Block Number: 32162')
# logger.debug('- Events: ' + json.dumps(event_result, indent=2))
current_block = tron.trx.get_current_block()
logger.debug('block:%s', current_block['blockID'])
logger.debug('block:%s', current_block['block_header']['raw_data']['number'])

block = tron.trx.get_block(42775311)
logger.info("block - %s", block)
