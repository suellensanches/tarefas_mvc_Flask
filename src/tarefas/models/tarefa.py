from tarefas.models.database import Database


class Tarefa:
    """Provê métodos para armazenar, recuperar e processar os dados 
    das tarefas criadas a partir do formulário principal.
    """
    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao


    def salvarTarefa(self):
        """Salvar a tarefa no banco de dados."""

        sql = 'INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao) # Protege contra SQL Injection


        # Gerenciador de contexto (with)
        # Acessa os métodos __enter__ e __exit__ da classe
        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def listarTarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""

        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao FROM 
        tarefa LIMIT 100;'''
        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    @staticmethod
    def apagarTarefa(id):
        sql = 'DELETE FROM tarefa WHERE id_tarefa = %s;'
        params = (id,)

        with Database() as db:
            db.executar(sql, params)

    def editarTarefas(self):
        sql = 'UPDATE tarefa SET titulo_tarefa = %s, data_conclusao = %s WHERE id_tarefa = %s; '  
        params = (self.titulo, self.data_conclusao, self.id)

        with Database() as db:
            return(db.executar(sql, params))

# Área 51 (testes)
# tarefa = Tarefa('Minha nova tarefa')
# tarefa.salvarTarefa()