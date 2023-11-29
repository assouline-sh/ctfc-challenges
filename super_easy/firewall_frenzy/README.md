# Firewall Frenzy
## Misc

You're doing a security audit for a client and look at their firewall rules... what a mess! Identify the vulnerable/out-of-place ports/services that might have slipped through the ice and exposed them to frosty cyber criminals!

Note: The value of the flag is the summation of all the vulnerable ports. For example, if ports 10 and 30 were identified as vulnerable, the flag would be: CTF{40}. 

- 23 (telnet)
- 513 (rlogin)
- 3389 (rdp)
- 23 + 513 + 3389 = 3925

CTF{3925}
