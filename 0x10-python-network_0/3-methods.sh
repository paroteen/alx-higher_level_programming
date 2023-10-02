#!/bin/bash
<<<<<<< HEAD
# takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
=======
# displays http methods
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
>>>>>>> e514e892f6cc2f6ae220c81aa6f9215bc7fe1247
