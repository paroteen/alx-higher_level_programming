#!/bin/bash
<<<<<<< HEAD
# sends a request to a URL passed as an argument, and displays only the status code of the response. no pipe
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
=======
# send a request to a url passed as an argument,and displays only the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
>>>>>>> e514e892f6cc2f6ae220c81aa6f9215bc7fe1247
