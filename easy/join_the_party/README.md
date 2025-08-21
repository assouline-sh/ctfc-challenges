# Join the Party
## Web

I want to join the party, but it seems like there are all these conditions I need to fulfill to get in…


- When you go on the website, it says "Not an agent of the neu-ctf-club secure browser!". With burpsuite, change your User-Agent to neu-ctf-club. 
- Upon visiting the website again, it says "You currently do not Accept fl4g". So change your Accept to fl4g. 
- Then it says "Connection not s3cur3". So change your Connection to s3cur3. 
- Then it says "Not referred by the.bouncer". So add a new header Referer and set the value to the.bouncer. Make sure that the referer header has the first letter uppercase. This is actually a header so you can find the exact header by searching it up. 
- Then it says "Give-Flag is not 7ru3". So add another header, Give-Flag and set it to 7ru3. 
- Then you get the flag!


CTF{w3lc0me_t0_th3_p4rty!}

