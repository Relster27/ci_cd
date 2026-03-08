#!/usr/bin/env python3

from pwn import *

TARGET = './vuln'
HOST = ''
PORT = 1337

elf = ELF(TARGET)

context.arch = 'amd64'
gdb_script = f"""
  b *main
  c
  c
"""
# context.log_level = 'DEBUG'
context.log_level = 'ERROR'

if args.GDB:
  context.terminal = [
    'wt.exe', '-w', '0', 'new-tab', '--', 'bash', '-lc'
  ]
  p = gdb.debug(TARGET, gdbscript=gdb_script)
elif not args.REMOTE:
  p = process(TARGET)
else:
  p = remote(HOST, PORT)

# ===================================== #

p.sendline(b'A' * 16 + b'B' * 8 + b'C' * 8)

p.interactive()
