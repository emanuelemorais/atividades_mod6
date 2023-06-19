# Ponderada 4 - Backend para transmissão e armazenamento de imagens
## Como funciona

Para realizar essa atividade, foi desenvolvido um backend utilizando FastAPI para gravar vídeos, que consistem em sequências de várias imagens reproduzidas em rápida sucessão. Esses vídeos são salvos em um banco de dados, sendo o Supabase utilizado para essa finalidade.

O código que contém as rotas utilizadas no backend pode ser encontrado no arquivo `main.py`. A rota inicial `(/)` é um método GET que retorna uma página HTML contendo um botão para iniciar a gravação. Ao clicar no botão, ocorre um redirecionamento para a rota POST `(/record)`, que inicia a gravação e realiza o armazenamento dos dados no Supabase. Em seguida, o usuário é redirecionado de volta para a página inicial.

Para realizar a gravação de vídeos, foi desenvolvido um arquivo adicional chamado `record.py`. Nesse arquivo, utilizamos a biblioteca OpenCV para acessar a câmera do computador e capturar as informações quadro a quadro. Os quadros capturados são gravados em um arquivo de vídeo com a extensão `.mp4` seguindo o padrão de nomenclatura `output_{data}.mp4`, onde `{data}` representa a data e hora da gravação. Por fim, os videos são salvos numa pasta chamada `assets`, onde o backend consulta para o salvamento no supabase.

## [Video do funcionamento](https://www.youtube.com/watch?v=K87Rdv6F4M0)

## Como rodar

1. Clonar este repositório e acessar a pasta `ponderada 4`;
2. Rodar no terminal o comando `python -m venv ` ;
3. Ativar a venv criada;
4. Rodar no terminal o comando `pip install -r requirements.txt`;
5. Rodar o arquivo main com o comando `uvicorn main:app --reload`;
6. Acessar no navegador http://127.0.0.1:8000/ 
