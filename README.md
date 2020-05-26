# PyScanner

I built a port scanner from scratch using python and a little socket programming to scan for 65,536 ports. It was originally built on mobile (Pythonista3).

## Usage

The scanner tries to do a good enough job of resolving the hostname on its own, so you don't need to enter trivial hostnames such as http://www.<whatever>.com. Rather you can simply enter <whatever>.com and it should resolve to an IP before the scan begins. You should be able to see this in the output.

Also, this tool is currently single-threaded, but I'm going to try to be updating it since I'm porting it over from mobile so that it can handle these portscans at a higher speed, perhaps with a threads setting prior to the scan initialization, similar to how nmap uses the -T flag for determining threads.

Enjoy!
