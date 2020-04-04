# clockify
Simple clockify timer api call

Generate api key here https://clockify.me/user/settings

Set api key in env var: /home/$USER/.bashrc 

`export CLOCKIFY_KEY="YOU_KEY"`

## Start Timer
`python3 clockify.py -s -d "description task"`

## Stop Timer
`python3 clockify.py -e`

## ToDo
- set interval time like

`python3 clockify.py -i -S start_time -E end_time -d "description task"`

For now only the "Développement" project are available.
