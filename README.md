# serial-monitor
Script para monitoramento de portas seriais

Este script permite gerar um App executável para monitoramento de portas seriais.
Ele lista as portas em uso e exibe uma notificação quando novos dispositivos são conectados.
O App permanece o tempo todo minimizado na system tray.

## 🚀 Começando

Você pode usar o script Python ou a versão compilada. Ambas as versões possuem a mesma funcionalidade.

### 📋 Pré-requisitos

Para executar o script vc vai precisará ter o interpretador Python instalado. Todas as dependências podem ser intaladas via PIP:
```
pip install -R requirements.txt
```

### 🔧 Geração do executável

Para gerar o arquivo executável usamos o PyInstaller.

Dentro da pasta do projeto execute:

```
pyinstaller --icon=serial-port.ico --onefile --noconsole serial-monitor.py
```

Após a conclusão do processo o arquivo .EXE estará disponível no diretório dist.

Basta adicionar um atalho para esse arquivo na Pasta de Inicialização do Windows que o App será executado na inicialização do sistema.
