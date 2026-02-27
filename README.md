# Flowminer - Pedágio Digital com MasterPag

Sistema de pagamento de pedágio eletrônico integrado com o gateway MasterPag para geração de PIX.

## 🚀 Características

- ✅ Geração de PIX com QR code
- ✅ Código copia e cola automático
- ✅ Contagem regressiva de 1 hora
- ✅ Dados de cliente aleatórios (CPF válido, nome, email, telefone)
- ✅ Interface responsiva
- ✅ Integração com API MasterPag

## 📋 Pré-requisitos

- Conta no MasterPag
- Chaves de API do MasterPag (pública e secreta)

## 🔧 Configuração

### Credenciais do MasterPag

As credenciais estão configuradas no arquivo `debitos.html`:

```javascript
const publicKey = 'pk_53G9Asb20SkxsSEynta-9QyUPPzunSLE-6GZNyqnacOpuIlE';
const secretKey = 'sk_iwD_yFYQsZErmiGHYS3At8rgzpQnhxrg2QhyjJTxD62WwSPq';
```

**⚠️ Importante:** Para produção, mova essas credenciais para variáveis de ambiente.

## 📁 Estrutura do Projeto

```
flowminer-deploy/
├── index.html           # Página inicial
├── debitos.html         # Página de débitos e geração de PIX
├── css/                 # Estilos
│   ├── debitos.css
│   ├── main.css
│   └── modal.css
├── lib/                 # Bibliotecas externas
│   ├── bootstrap/
│   ├── jquery/
│   ├── sweetalert2/
│   └── fonts/
├── images/              # Imagens do projeto
├── vercel.json          # Configuração do Vercel
└── README.md            # Este arquivo
```

## 🌐 Como Usar

1. Acesse a página inicial (`index.html`)
2. Digite a placa do veículo
3. Selecione os débitos
4. Escolha "Pix" como forma de pagamento
5. O QR code será gerado automaticamente
6. Copie o código ou escaneie o QR code para pagar

## 🔄 Funcionalidades da Geração de PIX

### Dados Aleatórios

Cada transação gera:
- **CPF válido** com algoritmo de validação
- **Nome brasileiro** aleatório
- **Email** com domínios variados (@gmail.com, @icloud.com, @hotmail.com)
- **Telefone** com DDD (11-99) e número aleatório

### Contagem Regressiva

- PIX expira em 1 hora
- Contagem regressiva em tempo real
- Alerta quando expira

## 📝 Notas Importantes

- A data de vencimento sempre mostra o dia atual
- Os dados do cliente são gerados aleatoriamente a cada transação
- O QR code é gerado usando serviço externo (qrserver.com)
- Recomenda-se usar um backend para requisições de produção

## 🚀 Deploy no Vercel

1. Faça push do repositório para GitHub
2. Acesse https://vercel.com
3. Clique em "New Project"
4. Selecione o repositório do GitHub
5. Clique em "Deploy"

O projeto será automaticamente hospedado no Vercel!

## 📞 Suporte

Para dúvidas sobre a integração com MasterPag, consulte:
- https://app.masterpagbr.com/docs/intro/first-steps

## 📄 Licença

Projeto desenvolvido para Flowminer - 2026
