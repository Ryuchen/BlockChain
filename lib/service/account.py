#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# 本项目由@Ryuchen开发维护，使用Python3.7
# ==================================================

from Crypto.PublicKey import RSA

from lib.core.define import GenesisCode


class Account:

    __pri_key__ = ""
    __pub_key__ = ""

    def __init__(self):
        """
        constructor the account of this node
        """
        self._pri_key = self.__pri_key__
        self._pub_key = self.__pub_key__

    @classmethod
    def generate(cls):
        key = RSA.generate(2048)
        cls.__pri_key__ = key.exportKey(passphrase=GenesisCode, pkcs=8)
        cls.__pub_key__ = key.publickey().exportKey()

    @property
    def pri_key(self):
        return self._pri_key

    @pri_key.setter
    def pri_key(self, key):
        self._pri_key = key