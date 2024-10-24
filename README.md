# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# sapientIA

**NOME DA SOLUÇÃO: mpg(Modelo preditivo da Gazeta)**

## Integrantes: 
- <a href="https://www.linkedin.com/in/ana-beggiato/">Ana Beatriz Passos Beggiato</a>
- <a href="https://www.linkedin.com/in/david-deodato-41b9b72b7/">David Deodato de Alvarenga Nascimento</a>
- <a href="https://www.linkedin.com/in/gabriel-nascimento-563382243/">Gabriel Santos do Nascimento</a> 
- <a href="https://www.linkedin.com/in/igor-sampaio-silva/">Igor Sampaio Silva</a> 
- <a href="https://www.linkedin.com/in/luizapetenazzi/">Luiza Faria Petenazzi</a>
- <a href="https://www.linkedin.com/in/otavio-vasc/">Otavio de Carvalho Vasconcelos</a> 
- <a href="https://www.linkedin.com/in/vitor-balbo/">Vítor Margarido Balbo</a>

## Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/marcelo-gonçalves-phd-a550652/">Marcelo Luiz do Amaral Gonçalves</a>
### Instrutores
- <a href="https://www.linkedin.com/in/filipe-gonçalves-08a55015b/">Filipe Gonçalves de Souza Nogueira da Silva</a>
- <a href="https://www.linkedin.com/in/fillipe-resina-b2211a22/">Fillipe Manoel Xavier Resina</a> 
- <a href="https://www.linkedin.com/in/francisco-escobar/">Francisco de Souza Escobar</a> 
- <a href="https://www.linkedin.com/in/geraldo-magela-severino-vasconcelos-22b1b220/">Geraldo Magela Severino Vasconcelos</a>
- <a href="https://www.linkedin.com/in/jefferson-o-silva/">Jefferson de Oliveira Silva</a> 
- <a href="https://www.linkedin.com/in/renato-penha/">Renato Penha</a> 

## 📝 Descrição

&nbsp;&nbsp;&nbsp;&nbsp;O projeto em questão busca resolver um desafio que a Rede Gazeta, um dos maiores grupos de comunicação do Espírito Santo, enfrenta para prever suas metas de vendas publicitárias. A empresa tem se baseado somente nos dados do ano anterior para prever sua receita, sem levar em consideração os fatores importantes, como sazonalidade, eventos especiais ou a performance de setores específicos.Essas decisões têm sido feitas de acordo com o feelen dos gestores, que causam inconsistências e inferiorizam a posição competitiva da empresa. 

&nbsp;&nbsp;&nbsp;&nbsp;A proposta, portanto, é desenvolver um modelo preditivo utilizando uma análise de dados históricos como: valor de contratos, tipo de mídia, veículo, unidade de negócio, entre outros fatores. A meta é gerar previsões financeiras mais próximas da realidade utilizando algoritmos mais sofisticados para reduzir a subjetividade das decisões e melhorar a assertividade de suas metas de receita. Com isso, a Rede Gazeta poderá ajustar suas estratégias de forma mais assertiva, identificando oportunidades de crescimento, reduzindo risco, competindo de forma mais agressiva ao mercado, com decisões mais fundamentadas, maximizando o seu desempenho financeiro e mantendo sua liderança no segmento de comunicação. 


<b>Link para vídeo demonstrativo:</b> <a href="https://youtube.com/shorts/tuRBvFtDwm4?feature=share">IAgora by SapientIA</a>

## 📁 Estrutura de pastas

Dentre os arquivos presentes na raiz do projeto, definem-se:

- <b>readme.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>assets</b>: todas as imagens e mídias utilizadas nos notebooks e documentação são posicionadas aqui.

- <b>documents</b>: aqui estarão todos os documentos do projeto. Há também uma pasta denominada <b>extras</b> onde estão presentes documentos complementares.

- <b>notebooks</b>: todos os Jupyter Notebooks criados para desenvolvimento do projeto.

## 💻 Execução dos projetos

### Requisitos

Para executar os notebooks, os seguintes pré-requisitos devem ser atendidos:

1. **Localmente (VS Code)**:
   - Instalação do Python 3.x: [Link para download](https://www.python.org/downloads/)
   - Instalação do VS Code: [Link para download](https://code.visualstudio.com/)
   - Instalação do Jupyter Notebook:
     - Execute no terminal:
       ```bash
       pip install notebook
       ```
   - Instalação das bibliotecas necessárias:
     - Execute no terminal o comando a seguir para instalar as dependências:
       ```bash
       pip install -r requirements.txt
       ```

2. **Google Colab**:
   - Acesso a uma conta Google para utilizar o Colab.
   - **Passos para executar no Google Colab**:
     1. Abra o [Google Colab](https://colab.research.google.com/).
     2. Faça o upload do arquivo `.ipynb` do notebook.
     3. Execute as células do notebook normalmente.
     > **Nota:** Certifique-se de salvar uma cópia do notebook em seu Google Drive clicando em "Arquivo > Salvar uma cópia no Drive", para garantir que as alterações realizadas não sejam perdidas.

### Passos para execução

#### Execução local no VS Code

1. Clone o repositório:
   ```bash
   git clone https://github.com/Inteli-College/2024-2A-T12-IN03-G02
   ```

2. Navegue até o diretório do projeto:
    ```bash
    cd 2024-2A-T12-IN03-G02
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/MacOS
    venv\Scripts\activate      # Windows
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. No VS Code, abra o notebook desejado e execute as células.
#### Execução no Google Colab

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. Faça upload do arquivo `.ipynb` para o Colab.
3. Caso o notebook utilize arquivos locais ou datasets, faça o upload dos arquivos necessários no Google Colab.
4. Execute as células do notebook.

   **Dica**: Lembre-se de salvar uma cópia no seu Google Drive para garantir que suas alterações não sejam perdidas.

## 🗃 Histórico de lançamentos

* 1.0.0 - 10/10/2024
    * [sprint 5] Lançamento da primeira versão do modelo preditivo com documentação.
* 0.6.0 - 27/09/2024
    * [sprint 4] Comparação de modelos preditivos
* 0.3.1 - 13/09/2024
    * [sprint 3] Preparação de dados e modelo preditivo preliminar
* 0.2.7 - 30/08/2024
    * [sprint 2] Análise exploratória e levantamento de hipóteses
* 0.1.3 - 16/08/2024
    * [sprint 1] Documentação de entendimento do negócio

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" ><a rel="cc:attributionURL" href="https://github.com/Inteli-College/2024-1B-T12-IN02-G03">This work</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Inteli-College/2024-1B-T12-IN02-G03">INTELI, Ana Beatriz Passos Beggiato, David Deodato de Alvarenga Nascimento, Gabriel Santos do Nascimento, Igor Sampaio Silva, Luiza Faria Petenazzi, Otavio de Carvalho Vasconcelos e Vítor Margarido Balbo</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Creative Commons Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>