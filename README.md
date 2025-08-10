# USDT Tron Monitor - Sistema Completo

Sistema completo para monitoramento de carteiras USDT TRC20 na blockchain Tron com APIs reais.

## 🚀 Funcionalidades

- ✅ **Gestão de Carteiras** - Adicionar, remover e sincronizar carteiras USDT TRC20
- ✅ **Saldos Reais** - Busca saldos atualizados da blockchain Tron
- ✅ **Transações Reais** - Histórico completo de transações enviadas e recebidas
- ✅ **Dashboard Completo** - Visão geral com estatísticas e resumos
- ✅ **Detecção de Duplicados** - Identifica transações duplicadas
- ✅ **Comprovantes** - Gera comprovantes de transações
- ✅ **Interface Responsiva** - Funciona em desktop e mobile

## 🛠️ Tecnologias

- **Backend:** Python Flask com APIs proxy para TronScan
- **Frontend:** HTML5, CSS3, JavaScript vanilla
- **APIs:** TronScan API para dados reais da blockchain
- **Banco de Dados:** LocalStorage (sem necessidade de BD externo)

## 📦 Instalação

### Requisitos
- Python 3.7+
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Extrair arquivos:**
   ```bash
   unzip usdt-tron-monitor.zip
   cd usdt-tron-final
   ```

2. **Criar ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar o sistema:**
   ```bash
   python src/main.py
   ```

5. **Acessar o sistema:**
   - Abra o navegador em: http://localhost:5000
   - Usuário: admin
   - Senha: 123456

## 🔧 Configuração para Servidor

### Para Apache/Nginx
- Copie os arquivos para o diretório web do servidor
- Configure o Python Flask como WSGI
- Certifique-se que a porta 5000 está acessível

### Para Servidor VPS
```bash
# Instalar dependências do sistema
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Seguir passos de instalação acima
# Para executar em produção:
python src/main.py --host=0.0.0.0 --port=5000
```

## 📊 Como Usar

1. **Adicionar Carteiras:**
   - Vá em "Minhas Carteiras"
   - Clique "Adicionar Carteira"
   - Insira nome e endereço TRC20

2. **Visualizar Transações:**
   - "Enviado" - Transações de saída
   - "Recebido" - Transações de entrada
   - Clique "Atualizar" para buscar dados reais

3. **Monitorar Saldos:**
   - Dashboard mostra saldos totais
   - Clique "Sincronizar" para atualizar

## 🔑 Credenciais Padrão

- **Usuário:** admin
- **Senha:** 123456

## 🌐 APIs Utilizadas

- **TronScan API:** Para saldos e transações reais
- **Endpoint:** https://apilist.tronscanapi.com/api/
- **Token USDT:** TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t

## 📝 Notas Importantes

- Sistema busca dados reais da blockchain Tron
- Transações são verificáveis no TronScan
- Dados persistem no navegador (localStorage)
- Não requer banco de dados externo
- APIs têm rate limiting - use com moderação

## 🆘 Suporte

Se encontrar problemas:
1. Verifique se as dependências estão instaladas
2. Confirme que a porta 5000 está livre
3. Verifique logs no console do navegador
4. Teste conectividade com APIs TronScan

---
**Versão:** 2.0 - APIs Reais
**Data:** 10/08/2025
**Status:** Produção ✅

