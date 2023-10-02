#!/bin/bash
<<<<<<< HEAD
# Get the byte size of the HTTP response header for a given URL.
curl -s "$1" | wc -c
=======
# getting content and displaying just content lenght information 
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
>>>>>>> e514e892f6cc2f6ae220c81aa6f9215bc7fe1247
