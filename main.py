from datetime import datetime
from repositories.evento_repository import EventoRepository
from services.gerenciador_eventos import GerenciadorEventos

if __name__ == "__main__":
    print("--- Iniciando Sistema de Gerenciamento de Eventos (Arquitetura em Camadas) ---")
    
    # Configurando as camadas (Injeção de Dependência)
    repositorio = EventoRepository()
    gerenciador = GerenciadorEventos(repositorio)

    # 1. CADASTRAR
    gerenciador.cadastrar_evento("Tech Summit 2026", datetime(2026, 10, 15, 9, 0), "Centro de Convenções", "Maior evento de TI da região.")
    gerenciador.cadastrar_evento("Workshop de Python", datetime(2026, 11, 20, 14, 0), "Auditório B", "Workshop prático sobre OOP e SOLID.")
    print("Eventos cadastrados com sucesso!")

    # 2. LISTAR
    print("\n--- Lista de Eventos ---")
    for ev in gerenciador.listar_eventos():
        print(ev)

    # 3. CONSULTAR POR ID
    print("\n--- Consultando Evento ID 1 ---")
    evento_consultado = gerenciador.consultar_evento(1)
    if evento_consultado:
        print(f"Detalhes: {evento_consultado.nome} | Descrição: {evento_consultado.descricao}")

    # 4. ATUALIZAR
    print("\n--- Atualizando Evento ID 2 ---")
    gerenciador.atualizar_evento(2, local="Laboratório 1 - Novo Local")
    print("Evento atualizado:", gerenciador.consultar_evento(2))

    # 5. REMOVER
    print("\n--- Removendo Evento ID 1 ---")
    gerenciador.remover_evento(1)
    print("Eventos restantes:")
    for ev in gerenciador.listar_eventos():
        print(ev)