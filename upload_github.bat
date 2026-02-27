@echo off
REM Script para fazer upload automático para GitHub
REM Extrai arquivo RAR e faz upload de tudo

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo  FLOWMINER - UPLOAD AUTOMATICO PARA GITHUB
echo ============================================================
echo.

REM Verificar se Git está instalado
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Git nao esta instalado!
    echo Baixe em: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Pedir informações
set /p arquivo="Nome do arquivo RAR (ex: flowminer-deploy.rar): "
if not exist "%arquivo%" (
    echo [ERRO] Arquivo '%arquivo%' nao encontrado!
    pause
    exit /b 1
)

set /p usuario="Usuario do GitHub: "
set /p token="Token de acesso do GitHub: "
set /p repo="Nome do repositorio (ex: flowminerv2): "

echo.
echo ============================================================
echo RESUMO:
echo   Arquivo: %arquivo%
echo   Usuario: %usuario%
echo   Repositorio: %repo%
echo ============================================================
echo.

set /p confirmar="Deseja continuar? (S/N): "
if /i not "%confirmar%"=="S" (
    echo Operacao cancelada!
    pause
    exit /b 0
)

echo.
echo [1/5] Extraindo arquivo...

REM Tentar extrair com WinRAR
if exist "C:\Program Files\WinRAR\unrar.exe" (
    "C:\Program Files\WinRAR\unrar.exe" x "%arquivo%" . >nul 2>&1
    goto :extrair_ok
)

REM Tentar extrair com 7-Zip
if exist "C:\Program Files\7-Zip\7z.exe" (
    "C:\Program Files\7-Zip\7z.exe" x "%arquivo%" >nul 2>&1
    goto :extrair_ok
)

echo [ERRO] WinRAR ou 7-Zip nao encontrado!
echo Instale um deles para extrair o arquivo
pause
exit /b 1

:extrair_ok
echo [OK] Arquivo extraido com sucesso!

echo [2/5] Configurando Git...
git config --global user.email "flowminer@example.com"
git config --global user.name "Flowminer Deploy"

echo [3/5] Inicializando repositorio...
git init

echo [4/5] Adicionando arquivos...
git add .
git commit -m "Deploy Flowminer com integracao MasterPag"
git branch -M main

echo [5/5] Fazendo upload para GitHub...
set "url=https://%usuario%:%token%@github.com/%usuario%/%repo%.git"
git remote add origin %url%
git push -u origin main

if errorlevel 1 (
    echo.
    echo [ERRO] Erro ao fazer push!
    echo Verifique seu token e repositorio
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  UPLOAD CONCLUIDO COM SUCESSO!
echo ============================================================
echo.
echo Seu projeto esta no GitHub!
echo URL: https://github.com/%usuario%/%repo%
echo.
echo O Vercel vai fazer o deploy automaticamente!
echo Acesse: https://vercel.com para acompanhar
echo.
pause
