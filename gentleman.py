import sys
import os

def load_config():
	list_of_wordlists = []
	with open("config.list") as f:
		list_of_wordlists = [line for line in f.read().splitlines()]
	return list_of_wordlists


def load_wordlist(wordlist_path):
	wordlist = []
	with open(wordlist_path, "rb") as f:
		wordlist = [line for line in f.read().splitlines()]
	return wordlist

def log(msg):
	print(f"[*] {msg}")

def main():
	config = load_config()
	loaded_wordlists = []
	final_wordlist = []
	for wordlist in config:
		loaded_wordlists.append(load_wordlist(wordlist))
	log("loaded wordlists from config.list")

	# Begin parsing process
	wordlist_pointer = 0
	log("starting to process wordlists")
	while loaded_wordlists:
		if len(loaded_wordlists[wordlist_pointer]) > 0:
			
			current_word = loaded_wordlists[wordlist_pointer].pop(0)
			if current_word:
				# Remove slash in the beginning (happens on some wordlists and screws with duplicate filtering)
				if current_word[0] == b'/':
					current_word = current_word[1:]

				if current_word not in final_wordlist:
					final_wordlist.append(current_word)


				# Go to the next wordlist, or if in the end reset pointer to the start.
				if wordlist_pointer == len(loaded_wordlists)-1:
					wordlist_pointer = 0
				else:
					wordlist_pointer += 1


		else:
			log(f"Reached end of wordlist {wordlist_pointer}.")
			loaded_wordlists.pop(wordlist_pointer)
			wordlist_pointer = 0
	log(f"Final wordlist is ready, with {len(final_wordlist)} entries.")
	with open("output.txt", "wb") as f:
		log("Writing to output.txt")
		f.write(b"\n".join(final_wordlist))

	# Final wordlist is ready, printing some info.






if __name__ == '__main__':
	main()
# load_wordlist("/usr/share/seclists/Discovery/Web-Content/raft-small-words.txt")