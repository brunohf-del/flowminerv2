#!/usr/bin/env python3
"""
Script para fazer upload automático de arquivos para GitHub
Extrai o arquivo, cria as pastas e faz upload de tudo
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 70)
    print("  FLOWMINER - UPLOAD AUTOMÁTICO PARA GITHUB")
    print("=" * 70)
    print()

def verificar_git():
    """Verifica se Git está instalado"""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        return True
    except:
        print("❌ Git não está instalado!")
        print("   Baixe em: https://git-scm.com/download/win")
        return False

def extrair_arquivo(arquivo_rar):
    """Extrai o arquivo RAR"""
    print(f"📦 Extraindo {arquivo_rar}...")
    try:
        # Tenta usar WinRAR
        subprocess.run(['unrar', 'x', arquivo_rar, '.'], check=True, capture_output=True)
        print("✅ Arquivo extraído com sucesso!")
        return True
    except:
        try:
            # Tenta usar 7-Zip
            subprocess.run(['7z', 'x', arquivo_rar], check=True, capture_output=True)
            print("✅ Arquivo extraído com sucesso!")
            return True
        except:
            print("❌ Erro ao extrair arquivo!")
            print("   Instale WinRAR ou 7-Zip")
            return False

def fazer_upload(usuario, token, repo):
    """Faz o upload para GitHub"""
    print(f"\n📤 Fazendo upload para GitHub...")
    print(f"   Repositório: {repo}")
    
    try:
        # Configurar Git
        subprocess.run(['git', 'config', '--global', 'user.email', 'flowminer@example.com'], check=True, capture_output=True)
        subprocess.run(['git', 'config', '--global', 'user.name', 'Flowminer Deploy'], check=True, capture_output=True)
        
        # Inicializar repositório
        subprocess.run(['git', 'init'], check=True, capture_output=True)
        
        # Adicionar arquivos
        print("   Adicionando arquivos...")
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        
        # Fazer commit
        print("   Fazendo commit...")
        subprocess.run(['git', 'commit', '-m', 'Deploy Flowminer com integração MasterPag'], check=True, capture_output=True)
        
        # Configurar branch
        subprocess.run(['git', 'branch', '-M', 'main'], check=True, capture_output=True)
        
        # Adicionar remote
        url_remote = f"https://{usuario}:{token}@github.com/{usuario}/{repo}.git"
        subprocess.run(['git', 'remote', 'add', 'origin', url_remote], check=True, capture_output=True)
        
        # Fazer push
        print("   Fazendo push...")
        resultado = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True)
        
        if resultado.returncode == 0:
            print("✅ Upload concluído com sucesso!")
            print(f"\n🎉 Seu projeto está no GitHub!")
            print(f"   URL: https://github.com/{usuario}/{repo}")
            return True
        else:
            print(f"❌ Erro ao fazer push: {resultado.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

def main():
    limpar_tela()
    print_header()
    
    # Verificar Git
    if not verificar_git():
        input("\nPressione Enter para sair...")
        return
    
    # Pedir informações
    print("📋 INFORMAÇÕES NECESSÁRIAS:\n")
    
    arquivo_rar = input("Nome do arquivo RAR (ex: flowminer-deploy.rar): ").strip()
    if not os.path.exists(arquivo_rar):
        print(f"❌ Arquivo '{arquivo_rar}' não encontrado!")
        input("\nPressione Enter para sair...")
        return
    
    usuario = input("Usuário do GitHub: ").strip()
    token = input("Token de acesso do GitHub: ").strip()
    repo = input("Nome do repositório (ex: flowminerv2): ").strip()
    
    print("\n" + "=" * 70)
    print("RESUMO:")
    print(f"  Arquivo: {arquivo_rar}")
    print(f"  Usuário: {usuario}")
    print(f"  Repositório: {repo}")
    print("=" * 70)
    
    confirmar = input("\nDeseja continuar? (S/N): ").strip().upper()
    if confirmar != 'S':
        print("Operação cancelada!")
        return
    
    print()
    
    # Extrair arquivo
    if not extrair_arquivo(arquivo_rar):
        input("\nPressione Enter para sair...")
        return
    
    # Fazer upload
    if fazer_upload(usuario, token, repo):
        print("\n✨ Tudo pronto! O Vercel vai fazer o deploy automaticamente!")
        print("   Acesse: https://vercel.com para acompanhar")
    
    input("\nPressione Enter para sair...")

if __name__ == '__main__':
    main()
