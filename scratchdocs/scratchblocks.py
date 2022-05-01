def generate_input(blocks: dict, start: str) -> str:
	block = blocks[start]
	for inp in  block['inputs'].values():
		if inp[0] == 1:
			if inp[1][0] in (4,5):
				return f'{inp[1][1]}'
		elif inp[0] == 3:
			return generate_input(blocks, inp[1])

def generate_all(blocks: dict, start: str) -> str:
	out = ''
	block = blocks[start]
	if block['opcode'] == 'event_whenflagclicked':
		out = 'when flag clicked'
	elif block['opcode'] == 'control_wait':
		inp = generate_input(blocks, start)
		out = f'wait ({inp}) seconds'
	if block['next'] is not None:
		return out + '\n' + generate_all(blocks, block['next'])
	return out