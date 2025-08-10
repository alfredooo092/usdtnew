from flask import Blueprint, jsonify, request
import requests
from flask_cors import CORS

tron_bp = Blueprint('tron', __name__)

# Habilitar CORS para todas as rotas
CORS(tron_bp)

@tron_bp.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    """Buscar saldo USDT de uma carteira"""
    try:
        # API TronScan para saldo USDT TRC20
        url = f"https://apilist.tronscanapi.com/api/account?address={address}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Buscar saldo USDT (TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t)
            usdt_balance = 0
            if 'trc20token_balances' in data:
                for token in data['trc20token_balances']:
                    if token.get('tokenId') == 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t':
                        usdt_balance = float(token.get('balance', 0)) / 1000000  # Converter de micro USDT
                        break
            
            return jsonify({
                'success': True,
                'address': address,
                'balance': usdt_balance,
                'timestamp': data.get('date_created', 0)
            })
        else:
            return jsonify({
                'success': False,
                'error': f'API error: {response.status_code}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@tron_bp.route('/transactions/<address>', methods=['GET'])
def get_transactions(address):
    """Buscar transações USDT de uma carteira"""
    try:
        # Parâmetros da query
        limit = request.args.get('limit', 50)
        start = request.args.get('start', 0)
        
        # API TronScan para transações USDT TRC20 específicas
        url = f"https://apilist.tronscanapi.com/api/token_trc20/transfers"
        params = {
            'contract': 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t',  # USDT TRC20
            'relatedAddress': address,
            'limit': limit,
            'start': start
        }
        
        response = requests.get(url, params=params, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            
            transactions = []
            if 'token_transfers' in data:
                for tx in data['token_transfers']:
                    # Determinar se é enviado ou recebido
                    is_sent = tx.get('from_address', '').lower() == address.lower()
                    amount = float(tx.get('quant', 0)) / 1000000  # Converter de micro USDT
                    
                    transaction = {
                        'hash': tx.get('transaction_id', ''),
                        'from_address': tx.get('from_address', ''),
                        'to_address': tx.get('to_address', ''),
                        'amount': amount,
                        'timestamp': tx.get('block_ts', 0),
                        'is_sent': is_sent,
                        'status': 'COMPLETO' if tx.get('confirmed', True) else 'PENDENTE',
                        'block_number': tx.get('block', 0)
                    }
                    transactions.append(transaction)
            
            return jsonify({
                'success': True,
                'address': address,
                'transactions': transactions,
                'total': data.get('total', 0)
            })
        else:
            return jsonify({
                'success': False,
                'error': f'API error: {response.status_code}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@tron_bp.route('/transactions/sent/<address>', methods=['GET'])
def get_sent_transactions(address):
    """Buscar apenas transações enviadas"""
    try:
        # Buscar todas as transações
        response = get_transactions(address)
        data = response.get_json()
        
        if data.get('success'):
            # Filtrar apenas transações enviadas
            sent_transactions = [tx for tx in data['transactions'] if tx['is_sent']]
            
            return jsonify({
                'success': True,
                'address': address,
                'transactions': sent_transactions,
                'total': len(sent_transactions)
            })
        else:
            return response
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@tron_bp.route('/transactions/received/<address>', methods=['GET'])
def get_received_transactions(address):
    """Buscar apenas transações recebidas"""
    try:
        # Buscar todas as transações
        response = get_transactions(address)
        data = response.get_json()
        
        if data.get('success'):
            # Filtrar apenas transações recebidas
            received_transactions = [tx for tx in data['transactions'] if not tx['is_sent']]
            
            return jsonify({
                'success': True,
                'address': address,
                'transactions': received_transactions,
                'total': len(received_transactions)
            })
        else:
            return response
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

