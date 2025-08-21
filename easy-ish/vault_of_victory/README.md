# Vault of Victory
## RE

I heard that when street fighters win a flag, they keep it in their vault. They need to sign in with their username and password to access their flag. However, Puckman got mad at Blanka for beating him and locked Blanka out of his account! Help Blanka sign into the vault to get his flag. 

- Run strings on the binary and see possible usernames and passwords
- Other users logins give fake flags; can’t log in as blanka
- Inspect the binary and see that you can overflow the username by overflowing the password. Calculate how much padding is needed
- Enter anything for the username, enter “3lectr1cThund3rAAAAAAAAAblanka” for the password to overwrite username as ‘blanka’
- Successfully log in!


CTF{u_w0n_the_b0f}

