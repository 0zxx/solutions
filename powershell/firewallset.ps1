$cidrList = Get-Content "C:\Users\user\Documents\hosts\cidrlist.txt"

foreach ($cidr in $cidrList) {
    $subnet, $mask = $cidr.split("/")
    $mask = [int]([math]::Pow(2, 32 - $mask) - 1)
    $subnetString = "$subnet/$mask"
    $subnetInt = [BitConverter]::ToUInt32([IPAddress]::Parse($subnet).GetAddressBytes(), 0)
    $subnetInt = $subnetInt -band (-bnot $mask)
    $displayName = "Bloquear $subnetString"
    New-NetFirewallRule -DisplayName $displayName -Direction Inbound -LocalAddress $subnetString -Action Block
}
