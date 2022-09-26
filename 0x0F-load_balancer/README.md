# Load Balancer README.

### Mandatory Tasks.

***0. Double the number of webservers***

	* Configure web-02 to be identical to web-01. Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works.

	* Requirements:

		- Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
			* The name of the custom HTTP header must be X-Served-By
			* The value of the custom HTTP header must be the hostname of the server Nginx is running on
		- Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine.
			* Ignore SC2154 for shellcheck
				- Ignore: https://github.com/koalaman/shellcheck/wiki/Ignore
				- SC2154: https://github.com/koalaman/shellcheck/wiki/SC2154

***1. Install and configure HAproxy on your lb-01 server.***

	* Requirements:

		- Configure HAproxy so that it send traffic to web-01 and web-02
		- Distribute requests using a roundrobin algorithm
		- Make sure that HAproxy can be managed via an init script
		- Servers should be configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.

	- Write a Bash script that configures a new Ubuntu machine to respect above requirements

	Example:

	sylvain@ubuntu$ curl -Is 54.210.47.110
	HTTP/1.1 200 OK
	Server: nginx/1.4.6 (Ubuntu)
	Date: Mon, 27 Feb 2017 06:12:17 GMT
	Content-Type: text/html
	Content-Length: 30
	Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
	Connection: keep-alive
	ETag: "58abea7c-1e"
	X-Served-By: 03-web-01
	Accept-Ranges: bytes

	sylvain@ubuntu$ curl -Is 54.210.47.110
	HTTP/1.1 200 OK
	Server: nginx/1.4.6 (Ubuntu)
	Date: Mon, 27 Feb 2017 06:12:19 GMT
	Content-Type: text/html
	Content-Length: 612
	Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
	Connection: keep-alive
	ETag: "5315bd25-264"
	X-Served-By: 03-web-02
	Accept-Ranges: bytes

	sylvain@ubuntu$
