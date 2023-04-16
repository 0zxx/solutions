Get-ChildItem *.txt
$outputFile = "C:\cidrlist.txt"
foreach ($file in (Get-ChildItem *.txt)) {
    Get-Content $file.FullName | ForEach-Object { $_ | Out-File -FilePath $outputFile -Encoding utf8 -Append }
}
