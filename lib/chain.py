#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# 本项目由@Ryuchen开发维护，使用Python3.7
# ==================================================

from lib.block import Block
from lib.transaction import Transaction

from lib.core.exception import OSTIBCException


class OpenSourceThreatIntelligenceBlockChain:

    def __init__(self):
        """
        constructor the OpenSourceThreatIntelligenceBlockChain(OSTIBC)
        """
        self.current_transactions = []
        self.chain = []
        self.target = 1
        self.reward = 100

    def genesis_block(self):
        """
        create the genesis block of our blockchain
        :return:
        """
        block = Block(target=self.target, transactions=[])
        self.current_transactions.append(block)

    def last_block(self):
        """
        get the last block of this chain
        :return:
        """
        return self.chain[len(self.chain) - 1]

    def add_transactions(self, transaction):
        if not transaction.walletoffrom or not transaction.walletofto:
            raise OSTIBCException("Not a valid transaction")

        if transaction.valid():
            raise OSTIBCException("Not a valid transaction")

        if transaction.amount <= 0:
            raise OSTIBCException("Not a valid transaction")

        # Making sure that the amount of walletoffrom is not greater than have
        if self.balance_of_address(transaction.walletoffrom) < transaction.amount:
            raise OSTIBCException("Not a valid transaction")

        self.current_transactions.append(transaction)

    def mine_transactions(self, address):
        """
        mine current transactions to store in a block of this chain
        at same time give the address of package reward
        :param address:
        :return:
        """
        transaction = Transaction(walletoffrom=None, walletofto=address, amount=self.reward)
        self.current_transactions.append(transaction)

        block = Block(target=self.target, transactions=self.current_transactions, previoushash=self.last_block().__hash__())


        self.chain.append(block)
        self.current_transactions = []
        
    def balance_of_address(self, address):
        """
        get the balance of the wallet address
        :param address:
        :return:
        """
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.walletoffrom == address:
                    balance -= transaction.amount

                if transaction.walletofto == address:
                    balance += transaction.amount
        return balance
