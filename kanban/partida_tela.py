# Lista de partidas-telas y los procesos que componen la ruta de dicha tela
# Se deben traer todas los registros de partida_tela (FabricBatch) que tengan status activo
partidas_telas = [
    {
        # Codigo del pedido
        'codigo_pedido': 'P001',
        # codigo de la partida
        'codigo_partida': 'H9610',
        # Codigo de la tela
        'codigo_tela': 'JE003012/ RI001597',
        'fecha_objetivo': '2024-02-10',        
        # Lista de los codigos de los procesos que componen la ruta de la tela, ordenados por el atributo secuencia de menor a mayor
        # Verificar la tabla de trayecto_seleccionado (SelectedPath) y eliminar de la lista de procesos a enviar todos los procesos que tengan el atributo de end_real_datetime o start_real_datetime
        # es decir omitir todos los procesos que ya esten finalizados o ya hayan empezado
        'secuencia_proceso': [
            'P001',
            'P002',
            'P005',
            'P003'    
        ],
        # cantidad a procesar
        'cantidad': 100,
    },
]
