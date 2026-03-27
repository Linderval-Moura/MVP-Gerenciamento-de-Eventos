from datetime import datetime
from repositories.evento_repository import EventoRepository
from services.gerenciador_eventos import GerenciadorEventos

# Credenciais para corresponderem ao PostgreSQL local
DB_CONFIG = {
    "dbname": "sistema_eventos", # Nome do banco
    "user": "admin",             # Seu usuário do PostgreSQL
    "password": "admin123",      # Sua senha do PostgreSQL
    "host": "localhost",
    "port": "5432"
}

if __name__ == "__main__":
    print("--- Iniciando Sistema de Gerenciamento de Eventos (Conectado ao DB) ---")
    
    try:
        repositorio = EventoRepository(DB_CONFIG)
        gerenciador = GerenciadorEventos(repositorio)

        # 1. CADASTRAR (O banco vai gerar o ID automaticamente)
        e1 = gerenciador.cadastrar_evento("Tech Summit 2026", datetime(2026, 10, 15, 9, 0), "Centro de Convenções", "Maior evento de TI.")
        e2 = gerenciador.cadastrar_evento("Workshop Python", datetime(2026, 11, 20, 14, 0), "Auditório B", "Workshop prático sobre OOP.")
        print("Eventos cadastrados com sucesso no banco de dados!")

        # 2. LISTAR
        print("\n--- Lista de Eventos no Banco ---")
        eventos = gerenciador.listar_eventos()
        for ev in eventos:
            print(ev)

        # Assume que os IDs gerados foram os primeiros (ex: 1 e 2)
        # Se rodar este script várias vezes, os IDs vão incrementar. 
        # Pegando o ID do último evento adicionado para testar a atualização e remoção.
        if eventos:
            ultimo_id = eventos[-1].id
            primeiro_id = eventos[0].id

            # 3. CONSULTAR
            print(f"\n--- Consultando Evento ID {primeiro_id} ---")
            evento_consultado = gerenciador.consultar_evento(primeiro_id)
            if evento_consultado:
                print(f"Encontrado: {evento_consultado.nome}")

            # 4. ATUALIZAR
            print(f"\n--- Atualizando Evento ID {ultimo_id} ---")
            gerenciador.atualizar_evento(ultimo_id, local="Novo Local Atualizado")
            print("Evento atualizado:", gerenciador.consultar_evento(ultimo_id))

            # 5. REMOVER
            print(f"\n--- Removendo Evento ID {primeiro_id} ---")
            gerenciador.remover_evento(primeiro_id)
            print("Lista após remoção:")
            for ev in gerenciador.listar_eventos():
                print(ev)

    except Exception as e:
        print(f"Erro ao conectar ou executar operação no banco: {e}")