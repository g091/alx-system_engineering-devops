# Web Server README.

### Mandatory Tasks

***0. Write a Bash script that transfers a file from our client to a server:***

	- Requirements:

		* Accepts 4 parameters
			i. The path to the file to be transferred
			ii. The IP of the server we want to transfer the file to
			iii. The username scp connects with
			iv. The path to the SSH private key that scp uses
		* Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
		* scp must transfer the file to the user home directory ~/
		* Strict host key checking must be disabled when using scp

***1. Install nginx web server***

	- Requirements:

		* Install nginx on your web-01
		* server
		* Nginx should be listening on port 80
		* When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
		* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
		* Don’t use systemctl for restarting nginx

	### Server terminal:

	root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
	root@sy-web-01$
	root@sy-web-01$ curl localhost
	Hello World!
	root@sy-web-01$

	### Local terminal:

	sylvain@ubuntu$ curl 34.198.248.145/
	Hello World!
	sylvain@ubuntu$ curl -sI 34.198.248.145/
	HTTP/1.1 200 OK
	Server: nginx/1.4.6 (Ubuntu)
	Date: Tue, 21 Feb 2017 23:43:22 GMT
	Content-Type: text/html
	Content-Length: 30
	Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
	Connection: keep-alive
	ETag: "58abea7c-1e"
	Accept-Ranges: bytes

	sylvain@ubuntu$

***2. Setup a domain name***

	- Requirement:

		* provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
		* configure your DNS records with an A entry so that your root domain points to your web-01 IP address
		* go to your profile and enter your domain in the Project website url field

***3. Configure your Nginx server so that /redirect_me is redirecting to another page.***

	- Requirements:

		* The redirection must be a “301 Moved Permanently”
		* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
		* Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

***4. Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.***

	- Requirements:

		* The page must return an HTTP 404 error code
		* The page must contain the string Ceci n'est pas une page
		* Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task
