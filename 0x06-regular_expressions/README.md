# Regular Expression README.

# Background Context

Build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default.
The Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

sylvain@ubuntu$ cat example.rb
\#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a


**Mandatory Tasks**

***0. Create a Ruby script that accepts one argument and pass it to a regular expression matching method***

	- The regular expression must match School

***1. Create a Ruby script that accepts one argument and pass it to a regular expression matching method***

	- Find the regular expression that will match
		hbn
		hbtn
		hbttn
		hbtttn
		hbttttn
		hbtttttn
		hbttttttn

***2. Create a Ruby script that accepts one argument and pass it to a regular expression matching method***

	- Find the regular expression that will match
		htn
		hbtn
		hbbtn
		hbbbtn

***3. Create a Ruby script that accepts one argument and pass it to a regular expression matching method***

	- Find the regular expression that will match
		hbn
		hbtn
		hbttn
		hbtttn
		hbttttn

***4. Create a Ruby script that accepts one argument and pass it to a regular expression matching method***

	- Find the regular expression that will match
		hbn
		hbon
		hbtn
		hbttn
		hbtttn
		hbttttn

***5. Create a Ruby script that accepts one argument and pass it to a regular expression matching method***

	- The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between

***6. This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.***

	- The regular expression must match a 10 digit phone number

		sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
		4155049898$
		sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
		$
		sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
		$
		sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
		$
		sylvain@ubuntu$

***7. 7. OMG WHY ARE YOU SHOUTING?***

	- The regular expression must be only matching: capital letters

		sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
		ILOVESYSADMIN$
		sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
		WHATSAY$
		sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
		$
		sylvain@ubuntu$
