$filePath = ".\cloudflare.txt"
$filePath2 = ".\twitter.txt"
$filePath3 = ".\github.txt"
$filePath4 = ".\microsoft.txt"

$ruleName = "cloudflare"
$ruleName2 = "twitter"
$ruleName3 = "github"
$ruleName4 = "microsoft"

$networkProfile = "Domain"
$networkProfile2 = "Private"
$networkProfile3 = "Public"

# Obtém os endereços IPv4 e IPv6 a partir do arquivo de texto
$addresses = Get-Content $filePath | Where-Object {$_ -match "(?:\d{1,3}\.){3}\d{1,3}\/24|[0-9A-Fa-f:]+\/\d{1,3}"}
$addresses2 = Get-Content $filePath2 | Where-Object {$_ -match "(?:\d{1,3}\.){3}\d{1,3}\/24|[0-9A-Fa-f:]+\/\d{1,3}"}
$addresses3 = Get-Content $filePath3 | Where-Object {$_ -match "(?:\d{1,3}\.){3}\d{1,3}\/24|[0-9A-Fa-f:]+\/\d{1,3}"}
$addresses4 = Get-Content $filePath4 | Where-Object {$_ -match "(?:\d{1,3}\.){3}\d{1,3}\/24|[0-9A-Fa-f:]+\/\d{1,3}"}
$addresses5 = Get-Content $filePath5 | Where-Object {$_ -match "(?:\d{1,3}\.){3}\d{1,3}\/24|[0-9A-Fa-f:]+\/\d{1,3}"}
$addresses6 = Get-Content $filePath6 | Where-Object {$_ -match "(?:\d{1,3}\.){3}\d{1,3}\/24|[0-9A-Fa-f:]+\/\d{1,3}"}

# Cria uma nova regra de bloqueio de saída com a lista de endereços
New-NetFirewallRule -DisplayName $ruleName -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses -Action Block -Profile $networkProfile
New-NetFirewallRule -DisplayName $ruleName -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses -Action Block -Profile $networkProfile2
New-NetFirewallRule -DisplayName $ruleName -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses -Action Block -Profile $networkProfile3

New-NetFirewallRule -DisplayName $ruleName2 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses2 -Action Block -Profile $networkProfile
New-NetFirewallRule -DisplayName $ruleName2 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses2 -Action Block -Profile $networkProfile2
New-NetFirewallRule -DisplayName $ruleName2 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses2 -Action Block -Profile $networkProfile3

New-NetFirewallRule -DisplayName $ruleName3 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses3 -Action Block -Profile $networkProfile
New-NetFirewallRule -DisplayName $ruleName3 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses3 -Action Block -Profile $networkProfile2
New-NetFirewallRule -DisplayName $ruleName3 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses3 -Action Block -Profile $networkProfile3

New-NetFirewallRule -DisplayName $ruleName4 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses4 -Action Block -Profile $networkProfile
New-NetFirewallRule -DisplayName $ruleName4 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses4 -Action Block -Profile $networkProfile2
New-NetFirewallRule -DisplayName $ruleName4 -Direction Outbound -LocalPort Any -Protocol Any -RemoteAddress $addresses4 -Action Block -Profile $networkProfile3
