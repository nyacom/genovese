#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import llvm
import llvm.core
import llvm.ee

#------------------------------------------------------------------------------
class genovese:

	def __init__(self):
		self.filename = ""

	def argument(self):
		argv = sys.argv
		argc = len(argv)

		if (argc < 2 or argv[1] == ''):
			return

		self.filename = argv[1]

	def bitloader(self):
	#	mod = llvm.core.Module.new('hogehoge')
		f = open(self.filename, 'r')
		module = llvm.core.Module.from_bitcode(f)

		entfunc = module.get_function_named('main')

		print entfunc

#------------------------------------------------------------------------------
if __name__ == "__main__":

	g = genovese()	# new

	g.argument()
	g.bitloader()

