# Configuration Management README.

#### Mandatory Tasks

***0. Create a file***

- Using Puppet, create a file in /tmp.
	- Requirements:
		* File path is /tmp/school
		* File permission is 0744
		* File owner is www-data
		* File group is www-data
		* File contains I love Puppet

***1. Install a package***

- Using Puppet, install flask from pip3.
	- Requirements:
		* Install flask
		* Version must be 2.1.0

	Example:

	root@9665f0a47391:/# puppet apply 1-install_a_package.pp
	Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
	Notice: /Stage[main]/Main/Package[Flask]/ensure: created
	Notice: Applied catalog in 0.20 seconds
	root@9665f0a47391:/# flask --version
	Python 3.8.10
	Flask 2.1.0
	Werkzeug 2.1.1

***2. Execute a command***

- Using Puppet, create a manifest that kills a process named killmenow.
	- Requirements:
		* Must use the exec Puppet resource
		* Must use pkill

	Example:

	Terminal #0 - starting my process

	root@d391259bf577:/# cat killmenow
	#!/bin/bash
	while [[ true ]]
	do
	    sleep 2
	done

	root@d391259bf577:/# ./killmenow

	Terminal #1 - executing my manifest

	root@d391259bf577:/# puppet apply 2-execute_a_command.pp
	Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
	Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
	Notice: Finished catalog run in 0.10 seconds
	root@d391259bf577:/#

	Terminal #0 - process has been terminated

	root@d391259bf577:/# ./killmenow
	Terminated
	root@d391259bf577:/#
