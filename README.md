# PyScanner

I built a port scanner from scratch using python3 and a little socket programming to scan for 65,536 ports. It was originally built on mobile (iOS Pythonista3). This won't function running it with Python2 (though it can be ported over with some simple changes if needed).

Also, this tool is currently single-threaded, but I'm going to try to be updating it since I'm porting it over from mobile so that it can handle these portscans at a higher speed, perhaps with a threads setting prior to the scan initialization, similar to how nmap uses the -T flag for determining threads.

## Usage

This scanner is built purely for use with iOS' Pythonista3 Python IDE. Trying to run this on a desktop environment will require doing some porting but isn't too difficult so I may get around to it. In the meantime, the usage requires Pythonista3 to be installed and for this script to be run from within Pythonista3 using Python3.

**Note:** By default Pythonista3 will attempt to run the script using Python2 so make sure you press and hold the play button and select Python3 when starting the port scanner up.

following the above instructions  will prompt the scanner to request a hostname:

```
Please enter a target hostname to scan
```

PyScanner tries to do a good enough job of resolving the hostname on its own, so you don't need to enter trivial hostnames such as `http://www.<whatever>.com`. Rather you can simply enter `<whatever>.com` and it should resolve to an IP before the scan begins. You should be able to see this in the output.

#### Example

```
Please enter a target hostname to scan
scanme.nmap.org

========================================
Please wait while scanning target 45.33.32.156
========================================
port 22 is open
```

That's all for now,
Enjoy!
