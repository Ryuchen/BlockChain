#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# 本项目由@Ryuchen开发维护，使用Python3.7
# ==================================================

import time
import json
import hashlib

from lib.core.exception import OSTIBCException


class Transaction:

    def __init__(self, walletoffrom, walletofto, amount):
        """
        constructor of the transactions entity
        :param walletoffrom: the wallet address of coin from
        :param walletofto: the wallet address of coin to
        :param amount:
        """
        self.walletoffrom = walletoffrom
        self.walletofto = walletofto
        self.amount = amount
        self.timestamp = time.time()
        self.signature = ''

    def __hash__(self):
        """
        overwrite the default hash method
        :return: the current hash of the transaction
        """
        string = json.dumps(self.__dict__(), sort_keys=True).encode()
        return hashlib.sha256(string).hexdigest()

    def __dict__(self):
        """
        overwrite the default dict method
        :return: the necessary params of the transaction
        """
        return {
            "walletoffrom": self.walletoffrom,
            "walletofto": self.walletofto,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

    def sign(self, key):
        """
        use the public key of the from to sign this transaction
        :return:
        """
        if key != self.walletoffrom:
            raise OSTIBCException("You cannot sign this transaction")

        self.signature = key.sign(self.__hash__(), 'base64')

    def valid(self):
        if not self.signature:
            raise OSTIBCException("No signature in this transaction")
        
        
