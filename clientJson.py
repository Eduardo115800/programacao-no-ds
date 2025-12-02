cliente = {
    "id": 1,
    "nome": "Joaquim Silva",
    "email": "joaquim@email.com",
    "pagamentos": []
}

def adicionar_pagamento(cliente, valor, data, metodo):
    cliente["pagamentos"].append({
        "valor": valor,
        "data": data,
        "metodo": metodo
    })

# Teste
adicionar_pagamento(cliente, 250.0, "2025-12-01", "Cartão de Crédito")
adicionar_pagamento(cliente, 100.0, "2025-12-02", "Pix")

print(cliente)
