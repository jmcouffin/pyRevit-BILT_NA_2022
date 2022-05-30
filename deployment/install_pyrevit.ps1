#Declaring Path
#--------------------------------------------------
$basefilePath = "C:\pyRevit"
#Where pyRevit Installer are located
$pyRevit = $basefilePath + "\pyRevit_4.8.10.22040_signed.exe"
$pyRevitCLI = $basefilePath + "\pyRevit_CLI_4.8.10.22040_signed.exe"


#Installing pyRevit or pyRevit CLI
#--------------------------------------------------
Start-Process -Wait -FilePath $pyRevit -arg "/qn" -PassThru
Write-Host "pyRevit Installed"

Start-Process -Wait -FilePath $pyRevitCLI -arg "/qn" -PassThru
Write-Host "pyRevit CLI Installed"

#Extend pyRevit
#--------------------------------------------------
pyrevit extend ui pyBiltNA https://github.com/jmcouffin/pyRevit-BILT_NA_2022.git --dest="C:\pyRevit"