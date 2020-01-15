#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# 本项目由@Ryuchen开发维护，使用Python3.7
# ==================================================

import time
import json
import hashlib

from lib.core.define import GenesisDifficulty


class Block:

    def __init__(self, target, transactions, previoushash=''):
        """
        constructor the block entity
        :param target:
        :param transactions:
        :param previoushash:
        """
        self.target = target
        self.previoushash = previoushash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.valid = False

    def __hash__(self):
        """
        overwrite the default hash method
        :return: the current hash of the block
        """
        block_string = json.dumps(self.__dict__(), sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __dict__(self):
        """
        overwrite the default dict method
        :return: the necessary params of the block
        """
        return {
            "timestamp": self.timestamp,
            "previoushash": self.previoushash,
            "transactions": self.transactions,
            "nonce": self.nonce
        }

    def __str__(self):
        """
        overwrite the default str method
        :return: the customize str format of current block
        """
        return json.dumps(
            {
                "timestamp": self.timestamp,
                "previoushash": self.previoushash,
                "transactions": self.transactions,
                "nonce": self.nonce,
                "hash": self.__hash__(),
                "valid": self.valid
            }
        )

    def __difficulty__(self):
        """
        according the block index to get the current work of difficulty
        :return:
        """
        return GenesisDifficulty / self.target


    def valid_proof(self):
        """
         Validates the Proof: Does self block hash contain the difficulty
        """
        guess_hash = self.__hash__()[8:]
        return guess_hash[:self.__difficulty__()] == "F" * self.__difficulty__()

    def proof_of_work(self):
        """
        Simple Proof of Work Algorithm:
        - Find a number nonce so that self block hash contains the difficulty
        :return: <int>
        """
        while self.valid_proof() is False:
            self.nonce += 1
        return self.nonce

