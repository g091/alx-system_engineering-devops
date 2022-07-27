# Networking Basics #0 README.

**6 Mandatory Tasks**

***0. OSI Model***

	* OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

	* It is organized from the lowest level to the highest level:

		- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
		- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

	Questions:

	* What is the OSI model?
	i) Set of specifications that network hardware manufacturers must respect
	ii) The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
	iii) The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

	How is the OSI model organized?
	i) Alphabetically
	ii) From the lowest to the highest level
	iii) Randomly

***1. Types of network***

	* LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

	Questions:
	- What type of network a computer in local is connected to?
		i) Internet
		ii) WAN
		iii) LAN

	- What type of network could connect an office in one building to another office in a building a few streets away?
		i) Internet
		ii) WAN
		iii) LAN

	- What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?
		i) Internet
		ii) WAN
		iii) LAN

***2. MAC and IP address***

	Questions:
	- What is a MAC address?
		i) The name of anetwork interface
		ii) The unique identifier of a network interface
		iii) A network interface

	- What is an IP address?
		i) Is to devices connected to a network what postal address is to houses
		ii) The unique identifier of a network interface
		iii) Is a number that network devices use to connect to networks

***3. UDP and TCP***

	Questions:
	- Which statement is correct for the TCP box:
		i) It is a protocol that is transferring data in a slow way but surely
		ii) It is a protocol that is transferring data in a fast way and might loss data along in the process

	- Which statement is correct for the UDP box:
		i) It is a protocol that is transferring data in a slow way but surely
		ii) It is a protocol that is transferring data in a fast way and might loss data along in the process

	- Which statement is correct for the TCP worker:
		i) Have you received boxes x, y, z?
		ii) May I increase the rate at which I am sending you boxes?

***4. TCP and UDP ports***

	Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

	If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

	While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

		- 22 for SSH
		- 80 for HTTP
		- 443 for HTTPS

	Note that a specific IP + port = socket.

	* Write a Bash script that displays listening ports:
		- That only shows listening sockets
		- That shows the PID and name of the program to which each socket belongs

***5. Is the host on the network***

	The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

	* Write a Bash script that pings an IP address passed as an argument.
		- Accepts a string as an argument
		- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
		- Ping the IP 5 times

	It is interesting to look at the time value, which is the time that it took for the ICMP request to go to the 8.8.8.8 IP and come back to my host. The IP 8.8.8.8 is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.
