# Loops, conditions & parsing README.

**Mandatory Tasks**

***0. Create a SSH RSA key pair***

	- Create a RSA key pair.

		- Share your public key in your answer file 0-RSA_public_key.pub
		- Fill the SSH public key field of your intranet profile with the public key you just generated
		- Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
		- If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
SSH and RSA keys will be covered in depth in a later project.


***1. Write a Bash script that displays Best School 10 times.***

	- Use the for loop (while and until are forbidden)

***2. Write a Bash script that displays Best School 10 times.***

	- Use the while loop (for and until are forbidden)

***3. Write a Bash script that displays Best School 10 times.***

	- Use the until loop (for and while are forbidden)

***4. Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.***

	- Use the while loop (for and until are forbidden)
	- Use the if statement

***5. Write a Bash script that loops from 1 to 10 and:***

	* displays bad luck for the 4th loop iteration
	* displays good luck for the 8th loop iteration
	* displays Best School for the other iterations

	- Use the while loop (for and until are forbidden)
	- Use the if, elif and else statements

***6. Write a Bash script that displays numbers from 1 to 20 and:***

	* displays 4 and then bad luck from China for the 4th loop iteration
	* displays 9 and then bad luck from Japan for the 9th loop iteration
	* displays 17 and then bad luck from Italy for the 17th loop iteration

	- Use the while loop (for and until are forbidden)
	- Use the case statement

***7. Write a Bash script that displays the time for 12 hours and 59 minutes:***

	* display hours from 0 to 12
	* display minutes from 1 to 59

	- Use the while loop (for and until are forbidden)

***8. Write a Bash script that displays:***

	* The content of the current directory
	* In a list format
	* Where only the part of the name after the first dash is displayed

	- Use the for loop (while and until are forbidden)
	- Don't display hidden files

***9. Write a Bash script that gives you information about the school file.***

	- Use if and, else (case is forbidden)
	- The Bash script should check if the file exists and print:
		- if the file exists: school file exists
		- if the file does not exist: school file does not exist
	- If the file exists, print:
		- if the file is empty: school file is empty
		- if the file is not empty: school file is not empty
		- if the file is a regular file: school is a regular file
		- if the file is not a regular file: (nothing)

***10. Write a Bash script that displays numbers from 1 to 100.***

	- Displays FizzBuzz when the number is a multiple of 3 and 5
	- Displays Fizz when the number is multiple of 3
	- Displays Buzz when the number is a multiple of 5
	- Otherwise, displays the number
	- In a list format

**Advanced Tasks**

***11. Write a Bash script that displays the content of the file /etc/passwd.***

	- It should only display:
		- username
		- user id
		- Home directory path for the user
	* Use the while loop only (for and until are forbidden)

***12. Write a Bash script that displays the content of the file /etc/passwd, using the while loop + IFS.***

	- Format: The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO

	* Use the while loop (for and until are forbidden)

***12. Write a Bash script that displays the visitor IP along with the HTTP status code from the Apache log file.***

	- Format: IP HTTP_CODE
	- in a list format
	- Must use awk
	- Don't use while, for, until and cut
	- Download and commit the apache-access.log file along with your answers files

***13. Write a Bash script that groups visitors by IP and HTTP status code, and displays this data.***

	- The exact format must be:
	- OCCURENCE_NUMBER IP HTTP_CODE
	- In list format
	- Ordered from the greatest to the lowest number of occurrences
	- Must use awk
	- Don't use while, for, until and cut
