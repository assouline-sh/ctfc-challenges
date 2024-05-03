# Puzzling Pcap
## Forensics

- Open Pcap in Wireshark and search for http traffic
- Navigate to imgur links, and see it is a QR code broken up into several images
- Download all images found in traffic
- Put images together with `convert -append *.png out.png` to complete the QR code
- Scan the QR code

CTF{follow_our_socials}
