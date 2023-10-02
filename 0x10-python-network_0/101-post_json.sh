#!/bin/bash
<<<<<<< HEAD
# Sends a JSON POST request to a given URL with a given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
=======
# sends a json post request to a rul passsed as the first argument,a dn displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
>>>>>>> e514e892f6cc2f6ae220c81aa6f9215bc7fe1247
