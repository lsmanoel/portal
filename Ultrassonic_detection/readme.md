# Detecção de passagem por ultrassom

Obs: arquivo main.py é apenas pra teste, não é pra usar no projeto. Os arquivos criados devem ser 
adaptados ao projeto, no escopo junto com a detecção de imagem.

## Detecção de passagem

Para a detecção da passagem de algum competidor pela linha de largada/chegada, 
foram criadas funções para o raspberry pi, em python, utilizando a biblioteca RPI.GPIO.

Pensa-se em utilizar 2 ultrassons para a medição em ambos os lados do portal
de passagem. É feito o monitoramento das distâncias para verificar se passam 1 
ou mais objetos pela linha simultaneamente. O arquivo cross_detection.py contém o código
para esta tarefa. 

As funções que devem ser chamadas na main (código do reconhecimento de imagem), devem ser:

    - calibrate() : para calibrar a distância base (largura do portal), retorna a média de 10 larguras medidas;
    - lineCrossed(baseLen,carLen): entra-se com o tamanho da base e do carro, retorna:
        - 0 : se não houve nenhuma pasagem;
        - 1 : se passou 1 carro;
        - 2 : se passou mais de 1 carro.

## Classe Car

Foi criada uma classe Car, para que sejam instanciados todos os competidores.
Cada objeto armazena:

    - Seu id;
    - Número de voltas percorridas;
    - Buffer com os tempos das voltas;
    - Posição a cada volta

É instanciada com o id do competidor, e deve ser utilizada a função Car.start() no momento 
de início da corrida.
A cada volta detectada do objeto, deve-se chamar a função  lapIncrement(position), esta atualiza o número
de cada volta, e seu tempo percorrido. Deve-se definir externamente, devido ao contexto, a sua posição.
Esta função atualiza os dados e os salva em um arquivo JSON para o envio dos dados.

## Dependências

As bibliotecas utilizadas são na sua maioria, nativas do Python 3. Para o acesso do GPIO no Raspbery Pi é preciso
instalar a RPi.GPIO.
