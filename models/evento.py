from datetime import datetime

class Evento:
    """Entidade central do sistema (Camada de Domínio)."""
    
    def __init__(self, id_evento: int, nome: str, data: datetime, local: str, descricao: str) -> None:
        self._id = id_evento
        self.nome = nome          # Usa o setter para validar
        self._data = data
        self.local = local        # Usa o setter para validar
        self._descricao = descricao

    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if not novo_nome.strip():
            raise ValueError("O nome do evento não pode ser vazio.")
        self._nome = novo_nome

    @property
    def data(self) -> datetime:
        return self._data

    @data.setter
    def data(self, nova_data: datetime) -> None:
        self._data = nova_data

    @property
    def local(self) -> str:
        return self._local

    @local.setter
    def local(self, novo_local: str) -> None:
        if not novo_local.strip():
            raise ValueError("O local não pode ser vazio.")
        self._local = novo_local

    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao: str) -> None:
        self._descricao = nova_descricao

    def __str__(self) -> str:
        data_formatada = self._data.strftime("%d/%m/%Y %H:%M")
        return f"[{self._id}] {self._nome} - {data_formatada} em {self._local}"