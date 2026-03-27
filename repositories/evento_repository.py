import psycopg2
from typing import List, Optional
from datetime import datetime
from models.evento import Evento

class EventoRepository:
    """Responsável por gerenciar a persistência dos dados no PostgreSQL (Camada de Dados)."""
    
    def __init__(self, db_config: dict) -> None:
        self.db_config = db_config

    def _conectar(self):
        """Abre a conexão com o banco de dados."""
        return psycopg2.connect(**self.db_config)

    def salvar(self, nome: str, data: datetime, local: str, descricao: str) -> Evento:
        """Insere o evento no banco e retorna o objeto Evento com o ID gerado pelo PostgreSQL."""
        query = """
            INSERT INTO eventos (nome, data, local, descricao)
            VALUES (%s, %s, %s, %s) RETURNING id;
        """
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (nome, data, local, descricao))
                novo_id = cursor.fetchone()[0] # Pega o ID gerado pelo SERIAL do banco
                conn.commit()
                return Evento(novo_id, nome, data, local, descricao)

    def buscar_todos(self) -> List[Evento]:
        """Busca todos os eventos no banco de dados, ordenados por data."""
        query = "SELECT id, nome, data, local, descricao FROM eventos ORDER BY data ASC;"
        eventos = []
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                for linha in cursor.fetchall():
                    # Instancia um objeto Evento para cada linha retornada do banco
                    eventos.append(Evento(*linha))
        return eventos

    def buscar_por_id(self, id_evento: int) -> Optional[Evento]:
        """Busca um evento específico pelo seu ID."""
        query = "SELECT id, nome, data, local, descricao FROM eventos WHERE id = %s;"
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_evento,))
                linha = cursor.fetchone()
                if linha:
                    return Evento(*linha)
        return None

    def atualizar(self, evento: Evento) -> bool:
        """Atualiza os dados de um evento existente no banco."""
        query = """
            UPDATE eventos
            SET nome = %s, data = %s, local = %s, descricao = %s
            WHERE id = %s;
        """
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (evento.nome, evento.data, evento.local, evento.descricao, evento.id))
                linhas_afetadas = cursor.rowcount
                conn.commit()
                return linhas_afetadas > 0

    def deletar(self, id_evento: int) -> bool:
        """Remove um evento do banco de dados."""
        query = "DELETE FROM eventos WHERE id = %s;"
        with self._conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id_evento,))
                linhas_afetadas = cursor.rowcount
                conn.commit()
                return linhas_afetadas > 0