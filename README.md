# DockerBTCNetwork
### Esse foi um trabalho que eu desenvolvi para melhorar minhas habilidades com a ferramenta Docker.

O trabalho é constituido por uma rede de 3 containers que se comunicam entre sí.

- **O primeiro container** é responsável por executar um banco de dados.
- **O segundo container** é responsável por preencher o banco de dados com os valores das variações do BTC.
- **O terceiro container** é responsável por extrair o maior valor desse banco de dados e exibir em uma página criada usando Flask.

#### OBS-1: Para executar o projeto basta ter o Docker instalado e executar `docker compose up`.
#### OBS-2: Para acessar a página com a variação basta digitar `localhost:8071` no navegador.
