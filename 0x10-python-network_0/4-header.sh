#!/bin/bash
<<<<<<< HEAD
# Send a GET request to a given URL with a header variable.
curl -sH "X-School-User-Id: 98" "${1}"
=======
# sends arguments using get
curl -sG "$1" -H "X-School-User-Id: 98"
>>>>>>> e514e892f6cc2f6ae220c81aa6f9215bc7fe1247
