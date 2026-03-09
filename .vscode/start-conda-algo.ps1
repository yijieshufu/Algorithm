# 初始化 conda 并激活 algo 环境（在 Cursor 终端里每次新开终端可运行此脚本）
$condaExe = "C:\Users\Administrator\miniconda3\Scripts\conda.exe"
(& $condaExe "shell.powershell" "hook") | Out-String | Where-Object { $_ } | Invoke-Expression
conda activate algo
