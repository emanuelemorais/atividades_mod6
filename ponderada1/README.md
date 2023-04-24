# Turtlesim: simulando um ambiente robótico integrado no ROS

## [Vídeo de demonstração do funcionamento](https://youtu.be/JymhKMY6EbQ)

## Como foi feita a implementação

Para realizar essa atividade foi necessário criar um nó que controla o movimento da tartaruga virtual no turtlesim. Para isso foi necessário baixar o Ubuntu 22.04 e instalar e configurar o ROS2.

O código utiliza as bibliotecas rclpy e geometry_msgs para criar um nó chamado "turtle_controller" que publica mensagens no tópico "turtle1/cmd_vel". A classe "TurtleController" é uma subclasse da classe "Node" da biblioteca rclpy, que define o comportamento do nó. A função "move_turtle" controla a ordem e a duração dos movimentos chamando as funções de movimento apropriadas em intervalos regulares de tempo. 

Já função "main" é responsável por iniciar o nó do ROS e encerrar o nó depois que o movimento é concluído. Quando executado, o código publica mensagens de movimento no tópico "turtle1/cmd_vel" para controlar a tartaruga virtual e imprimir a mensagem "Movimento iniciado" na tela para indicar que o movimento foi iniciado.

Para garantir a execução bem sucedida da atividade, é necessário abrir dois terminais no Ubuntu. No primeiro terminal, é criado um nó responsável pela renderização da tartaruga. No segundo terminal, o código é executado e através do ROS2, é possível publicar informações no tópico "turtle1/cmd_vel", movimentando assim a tartaruga no turtlesim. Desse modo, a comunicação estabelecida entre o publicador e o subscriber é do tipo pub-sub.

Por fim, a tartaruga foi programada para desenhar uma estrela, utilizando cinco funções consecutivas. Cada uma dessas funções contém as coordenadas que a tartaruga deve percorrer para formar corretamente as partes da estrela.

<img src="https://user-images.githubusercontent.com/99221221/233877543-8e39f7ea-5b9c-4130-b0b7-46db46f5079e.png" width="400" />

### Passo-a-passo para execução (passos que segui)

1. Instalar Ubuntu 22.04 (caso o computador seja Windows)
2. Instalar e configurar ROS2 e Turtlesim no Ubuntu 22.04
3. Rodar o comando `ros2 run turtlesim turtlesim_node` no terminal do Ubuntu 22.04 (Isso irá abrir o turtlesim)
4. Acessar o diretório a `atividades_mod6/ponderada1/` desse repositório e colocar o comando `python3 estrela3.py` para rodar o script
5. Após isso será possível ver a tartaruga desenhar uma estrela

### Estrutura de arquivos

```
├── ponderada1
│    ├── .gitignore
│    ├──  README.md
│    ├── estrela.py
│    ├── requeriments.txt
``` 
