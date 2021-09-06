PACKAGE = Hello
MAINFILE = main

ifndef ANTLR4
abort:
	$(error variable ANTLR4 is not set)
endif

all: $(PACKAGE).g4
	$(ANTLR4) $^ -Dlanguage=Python3

run: $(MAINFILE).py
	python3 $^

clean:
	find . \( -iname "~" -or -iname "*.cache*" -or -iname "*.diff" -or -iname "log.txt" -or -iname "__pycache*" -or -iname "*.tokens" -or -iname "*.interp" \) -exec rm -rf '{}' \;
	rm -rf *~ $(PACKAGE)*.py $(PACKAGE)*.pyc
