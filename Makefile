PROG=test
CC=clang -emit-llvm

.SUFFIXES: .c .bc .ll

.c.bc:
	$(CC) -c $< 

.c.ll:
	$(CC) -c -S $<

all:
	make $(PROG).bc

clean:
	rm -rf *.bc *.ll

