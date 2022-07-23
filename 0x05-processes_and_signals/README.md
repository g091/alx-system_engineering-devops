# Processes & signals README.

**Mandatory Tasks**

***0. Write a Bash script that displays its own PID.***

***1. Write a Bash script that displays a list of currently running processes.***

	- Must show all processes, for all users, including those which might not have a TTY
	- Display in a user-oriented format
	- Show process hierarchy

***2. Using the prev. cmd, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.***

	- You cannot use pgrep
	- The third line of your script must be # shellcheck disable=SC2009

***3. Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.***

	- Can't use ps

***4. Write a Bash script that displays To infinity and beyond indefinitely.***

	- In between each iteration of the loop, add a sleep 2

***5. Write a Bash script that stops 4-to_infinity_and_beyond process.***

	- Use kill

	- Terminal #0
		sylvain@ubuntu$ ./4-to_infinity_and_beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		Terminated
		sylvain@ubuntu$

	- Terminal #1
		sylvain@ubuntu$ ./5-dont_stop_me_now
		sylvain@ubuntu$

	- 2 terminals are started by  running my 4-to_infinity_and_beyond Bash script in terminal #0 and then moved on terminal #1 to run 5-dont_stop_me_now. We can then see in terminal #0 that my process has been terminated.

***6. Write a Bash script that stops 4-to_infinity_and_beyond process***

	- Can't use kill or killall

***7. Write a Bash script that displays:***

	- To infinity and beyond indefinitely
	- With a sleep 2 in between each iteration
	- I am invincible!!! when receiving a SIGTERM signal

	* Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

	* Start 7-highlander in Terminal #0 and then run 67-stop_me_if_you_can in terminal #1. for every iteration we should see I am invincible!!! appearing in terminal #0.

***8. Write a Bash script that kills the process 7-highlander.***


**Advanced tasks**

***9. Write a Bash script that:***

	- Creates the file /var/run/myscript.pid containing its PID
	- Displays To infinity and beyond indefinitely
	- Displays I hate the kill command when receiving a SIGTERM signal
	- Displays Y U no love me?! when receiving a SIGINT signal
	- Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

		sylvain@ubuntu$ sudo ./100-process_and_pid_file
		To infinity and beyond
		To infinity and beyond
		^CY U no love me?!

	* Executing the 100-process_and_pid_file script and killing it with ctrl+c.


Terminal #0

		sylvain@ubuntu$ sudo ./100-process_and_pid_file
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		To infinity and beyond
		I hate the kill command
		sylvain@ubuntu$

Terminal #1

		sylvain@ubuntu$ sudo pkill -f 100-process_and_pid_file
		sylvain@ubuntu$
