import sys,json

def read_in():
	lines = sys.stdin.readlines()
	if(len(lines) == 0):
		return "/noinput"
	return json.loads(lines[0])


def main():
	lines = read_in()
	while(lines != '/close'):
		if(lines != '/noinput'):
			print("You said: " + str(lines))
		lines = read_in()

if __name__ == '__main__':
	main()	