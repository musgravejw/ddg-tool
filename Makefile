install:
	@mkdir -p /usr/local/bin
	@mkdir -p /tmp/ddg/asm
	@mkdir -p /tmp/ddg/blocks
	@chmod 777 /tmp/ddg/asm
	@cp ./src/main.py /usr/local/bin/cfg
