C:\Users\LENOVO\BS\file wav
$list = Get-Content C:\Users\LENOVO\BS\link.txt

$clnt = New-Object System.Net.WebClient

foreach($url in $list) 
{ 

	#Get the filename 
	$filename = [System.IO.Path]::GetFileName($url) 

	#Create the output path 
	$file = [System.IO.Path]::Combine($pwd.Path, $filename) 

	Write-Host -NoNewline "Getting ""$url""... "

	#Download the file using the WebClient 
	$clnt.DownloadFile($url, $file) 

	Write-Host "done." 
}