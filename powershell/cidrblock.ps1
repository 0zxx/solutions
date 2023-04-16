$cidrList = Get-Content -Path "cidr_list.txt"
foreach ($cidr in $cidrList) {
    netsh advfirewall firewall add rule name="Block IPs" dir=in interface=any action=block remoteip=$cidr
}
