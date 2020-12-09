PACKAGE = MiniC
DIR = $(shell basename "$(PWD)")
# Example: stop at the first failed test:
#   make PYTEST_OPTS=-x tests
PYTEST_OPTS = 
# Run the whole test infrastructure for a subset of test files e.g.
#   make TEST_FILES='TP03/**/bad*.c' tests
ifdef TEST_FILES
export TEST_FILES
endif

PYTEST_BASE_OPTS=-vv -rs --failed-first --cov="$(PWD)" --cov-report=term --cov-report=html

ifndef ANTLR4
abort:
	$(error variable ANTLR4 is not set)
endif

all: antlr

.PHONY: antlr
antlr MiniCLexer.py MiniCParser.py: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

main-deps: MiniCLexer.py MiniCParser.py TP03/MiniCInterpretVisitor.py TP03/MiniCTypingVisitor.py

.PHONY: tests tests-interpret tests-codegen tests-regalloc

tests: tests-interpret



tests-interpret: test_interpreter.py main-deps
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) test_interpreter.py


# Test for naive allocator (also runs test_expect to check // EXPECTED directives):
tests-naive: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'naive or expect'

# Test for all but the smart allocator, i.e. everything that lab4 should pass:
tests-notsmart: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'not smart'

# Test just the smart allocation (quicker than tests)
tests-smart: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'smart'

# Complete testsuite (should pass for lab5):
tests-codegen: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py

tar: clean
	dir=$$(basename "$$PWD") && cd .. && \
	tar cvfz "$$dir.tgz" --exclude="*.riscv" --exclude=".git" --exclude=".pytest_cache"  \
	--exclude="htmlcov" "$$dir"
	@echo "Created ../$$(basename "$$PWD").tgz"

clean:
	find . \( -iname "*~" -or -iname ".cache*" -or -iname "*.diff" -or -iname "log*.txt" -or -iname "__pycache__" -or -iname "*.tokens" -or -iname "*.interp" \) -print0 | xargs -0 rm -rf \;
	rm -rf *~ $(PACKAGE)Parser.py $(PACKAGE)Lexer.py $(PACKAGE)Visitor.py
