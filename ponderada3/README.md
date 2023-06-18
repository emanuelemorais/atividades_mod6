# Ponderada 3 - Processamento de imagens e detecção de objetos

Para a execução dessa atividade, foram necessárias duas etapas: o treinamento do modelo utilizando o YOLO v8 e a aplicação ao vivo do mesmo utilizando a câmera do notebook.

Na primeira etapa, foi utilizado o Google Colaboratory para realizar o treinamento do modelo. Para isso, foi usado um conjunto de dados do Roboflow específico para o treinamento do modelo de detecção de rachaduras. Após a importação desse conjunto de dados, foi feito o treinamento do modelo, o qual foi executado com 10 épocas. Após a conclusão do treinamento, é possível obter um arquivo com extensão ".pt", que representa o modelo treinado. Esse arquivo contém os parâmetros aprendidos durante o processo de treinamento, como pesos e configurações do modelo.

Na segunda etapa, foi utilizado o arquivo ".pt" para aplicar o modelo treinado e realizar a detecção de rachaduras em tempo real usando a câmera do notebook. Para isso, foi feito um script em Python que acessa a câmera do notebook e submete os frames à detecção do modelo. Ao processar cada quadro da câmera, o modelo treinado identifica a presença de rachaduras e, quando detecta uma rachadura, marca o local correspondente desenhando um quadrado ao redor dele. 
 
 Video: https://drive.google.com/file/d/10jP5PniwTeHi1euJTGsMRh_dmw2BKcLg/view?usp=sharing
