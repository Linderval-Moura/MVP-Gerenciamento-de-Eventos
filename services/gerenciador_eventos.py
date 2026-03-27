from typing import List, Optional
from datetime import datetime
from models.evento import Evento
from repositories.evento_repository import EventoRepository

class GerenciadorEventos:
    """Responsável por orquestrar as regras de negócio (Camada de Serviço)."""
    
    def __init__(self, repository: EventoRepository) -> None:
        self._repository = repository

    def cadastrar_evento(self, nome: str, data: datetime, local: str, descricao: str) -> Evento:
        return self._repository.salvar(nome, data, local, descricao)

    def listar_eventos(self) -> List[Evento]:
        return self._repository.buscar_todos()

    def consultar_evento(self, id_evento: int) -> Optional[Evento]:
        return self._repository.buscar_por_id(id_evento)

    def atualizar_evento(self, id_evento: int, nome: str = None, data: datetime = None, local: str = None, descricao: str = None) -> bool:
        evento = self._repository.buscar_por_id(id_evento)
        if not evento:
            return False
        
        # Atualiza o objeto em memória
        if nome: evento.nome = nome
        if data: evento.data = data
        if local: evento.local = local
        if descricao: evento.descricao = descricao
        
        # Persiste a alteração no banco de dados
        return self._repository.atualizar(evento)

    def remover_evento(self, id_evento: int) -> bool:
        return self._repository.deletar(id_evento)