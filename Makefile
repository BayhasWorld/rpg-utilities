MAKE := make
be-test:
	$(MAKE) -C ./backend test

be-lint:
	$(MAKE) -C ./backend lint