from typing import List, Optional
from datetime import datetime
from models.evento import Evento
from repositories.evento_repository import EventoRepository

class GerenciadorEventos:
    """Responsável por orquestrar as regras de negócio (Camada de Serviço)."""
    
    def __init__(self, repository: EventoRepository) -> None:
        # Injeção de dependência do repositório
        self._repository = repository

    def cadastrar_evento(self, nome: str, data: datetime, local: str, descricao: str) -> Evento:
        novo_id = self._repository.gerar_id()
        evento = Evento(novo_id, nome, data, local, descricao)
        self._repository.salvar(evento)
        return evento

    def listar_eventos(self) -> List[Evento]:
        return self._repository.buscar_todos()

    def consultar_evento(self, id_evento: int) -> Optional[Evento]:
        return self._repository.buscar_por_id(id_evento)

    def atualizar_evento(self, id_evento: int, nome: str = None, data: datetime = None, local: str = None, descricao: str = None) -> bool:
        evento = self._repository.buscar_por_id(id_evento)
        if not evento:
            return False
        
        # Atualiza os dados se eles foram fornecidos
        if nome: evento.nome = nome
        if data: evento.data = data
        if local: evento.local = local
        if descricao: evento.descricao = descricao
        
        # Em um banco de dados real, chamaríamos o repository.salvar(evento) aqui
        return True

    def remover_evento(self, id_evento: int) -> bool:
        return self._repository.deletar(id_evento)