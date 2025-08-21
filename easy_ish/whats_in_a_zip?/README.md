# What's in a Zip
## Misc

It's cold outside... better zip up! Wait, not that kind of zip. I have this zip file... I wonder what's in it?

- `fcrackzip -v -D -p vocab challenge.zip`, unzip with password ‘scooby’
- mount the directory: `mkdir to_mount`; `sudo mount -o loop d.img to_mount`
- hint says it is encrypted with aes-256-cbc, ‘openssl enc -d -aes-256-cbc -in data.enc -out out.txt’ where key.txt is the password

CTF{you_found_me!}
