-- Criação do banco de dados (opcional, dependendo do SGBD)
-- CREATE DATABASE sistema_eventos;

-- Tabela principal de eventos
CREATE TABLE eventos (
    -- PK: Identificador único autoincremental
    id SERIAL PRIMARY KEY,
    
    -- NOT NULL: O nome é obrigatório. VARCHAR para limite razoável de texto.
    nome VARCHAR(150) NOT NULL,
    
    -- TIMESTAMP: Fundamental para ordenar os eventos cronologicamente.
    data TIMESTAMP NOT NULL,
    
    -- VARCHAR(200): Endereço físico ou link do evento.
    local VARCHAR(200) NOT NULL,
    
    -- TEXT: Flexibilidade para descrições longas sem limite rígido.
    descricao TEXT
);

-- ÍNDICE: Buscas por data (ex: eventos futuros, eventos de hoje) 
CREATE INDEX idx_eventos_data ON eventos(data);