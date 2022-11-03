# API Advanced README.


### Mandatory Tasks

***0. Function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.***

	- Requirements:
		* Prototype: def number_of_subscribers(subreddit)
		* If not a valid subreddit, return 0.

***1. Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.***

	- Requirements:
		* Prototype: def top_ten(subreddit)
		* If not a valid subreddit, print None.

***2. A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.***

	- Requirements:
		* Prototype: def recurse(subreddit, hot_list=[])
		* You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
		* If not a valid subreddit, return None.
	- The code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function.
