"""
Created By:  Peter Maynard <pete@port22.co.uk>
Created On:  2020 May 27th
Description: Linux Application Firewall
License:     BSD-3-Clause
"""

from bcc import BPF

with open('bpf/getpid.bpf', 'r') as f:
	bpf_text = f.read()

print("----BPF----\n{}\n----BPF----".format(bpf_text))

print("Compiling to BPF code...")
b = BPF(text=bpf_text)
print("..compile good.")

b.trace_print()
