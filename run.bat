@echo off
echo Installing Node.js...

REM Set the version of Node.js to install
set NODE_VERSION=v18.17.0

REM Set the download URL for Node.js (change the version as needed)
set NODE_URL=https://nodejs.org/dist/%NODE_VERSION%/node-%NODE_VERSION%-x64.msi

REM Set the download path
set DOWNLOAD_PATH=%TEMP%\nodejs.msi

REM Download Node.js
echo Downloading Node.js from %NODE_URL%...
powershell -Command "Invoke-WebRequest -Uri %NODE_URL% -OutFile %DOWNLOAD_PATH%"

REM Install Node.js
echo Installing Node.js...
start /wait msiexec.exe /i %DOWNLOAD_PATH% /quiet

REM Clean up
del %DOWNLOAD_PATH%

REM Check installation
echo Checking Node.js version...
node -v
npm -v

echo Node.js installation complete.

start cmd /k "cd library-archive && npm install"
start cmd /k "cd archive_backend && python manage.py runserver"
start cmd /k "cd library-archive && npm run dev"

