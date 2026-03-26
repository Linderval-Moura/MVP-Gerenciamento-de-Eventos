from typing import List, Optional, Dict
from models.evento import Evento

class EventoRepository:
    """Responsável por gerenciar a persistência dos dados (Camada de Dados)."""
    
    def __init__(self) -> None:
        self._eventos: Dict[int, Evento] = {}
        self._proximo_id: int = 1

    def salvar(self, evento: Evento) -> None:
        self._eventos[evento.id] = evento

    def gerar_id(self) -> int:
        id_atual = self._proximo_id
        self._proximo_id += 1
        return id_atual

    def buscar_todos(self) -> List[Evento]:
        return list(self._eventos.values())

    def buscar_por_id(self, id_evento: int) -> Optional[Evento]:
        return self._eventos.get(id_evento)

    def deletar(self, id_evento: int) -> bool:
        if id_evento in self._eventos:
            del self._eventos[id_evento]
            return True
        return False