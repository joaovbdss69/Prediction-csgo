# 🧬 Prediction CS:GO

## 🎯 Objetivo

O objetivo desse projeto é realizar a modelagem de 3 algoritmos de categorização diferentes para o mesmo dataset para identificar como cada um lida com aqueles dados e mostrar suas implementações.

Os 3 algoritmos que serão implementados são:
- KNN
- RandomForest
- Rede Neural

O dataset em questão é sobre rounds jogados dentro do jogo CS:GO em 700 demos de torneios de alto nível nos anos de 2019 e 2020 onde a cada 20 segundos é tirado uma "foto" do round até que a partida fosse decidida. O conjunto de dados foi publicado originalmente pela Skybox como parte de seu CS:GO AI Challenge, ocorrendo da primavera ao outono de 2020, entretanto o local no qual foi disponibilizado e se tem todas as informações segue abaixo:

https://www.openml.org/search?type=data&sort=runs&id=43430&status=active


## ETL

- Criação de variável resposta baseada na coluna round_winner (tr_win) ✔️
- Verificação da váriavel "Map"✔️
- Separação das 25 váriaveis com maior correlação com a target ✔️
- Análise da distribuição da variável resposta x features ✔️
- Verificação da distribuição da variável resposta ✔️
- Geração do Dataset final✔️

  Obs: Foi realizado algumas verificações durante o pré processamento, para verificação de valores nulos nas features e na target

  ## Construção dos Modelos

  ### KNN

- Divisão entre treino e teste, como padrão foi utilizado o split entre 80 - 20

     ![SeparacaoTreinoTesteKNN](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/SeparacaoTreinoTesteKNN.png)

- Testando diversos Valores de K para achar o melhor para o problema com base na acurácia
  ![TesteK](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/TesteK.png)

- Criação de modelo e treinamento

- Resultados pela matriz de confusão e métricas de acurácia,precisão,recall e F1 Score

  ![MatrizConfusaoKNN](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/MatrizConfusaoKNN.png)

  ### RandomForest 

- Divisão entre treino e teste, como padrão foi utilizado o split entre 80 - 20

    ![SeparacaoTreinoTesteRandomForest](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/SeparacaoTreinoTesteRandomForest.png)

- Seleção de parâmetros do modelo
    - n_estimators
    - max_depth
    - max_features
    - criterion   

    ![ParametrosRandomForest](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/ParametrosRandomForest.png)


-  E para atingir os melhores valores para esses parâmetros foi utilizado o BayesianOptimization

    ![BayesianOptimizationRandomForest](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/BayesianOptimizationRandomForest.png)


-  Criação de modelo e treinamento

    ![TreinamentoModeloRandomForest](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/TreinamentoModeloRandomForest.png)

-  Resultados pela Curva ROC e matriz de confusão e métricas de acurácia,precisão,recall e F1 Score

  - Curva ROC

    ![CurveROCRandomForest](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/CurveROCRandomForest.png)

  - Matriz de Confusão

    ![MatrizConfusaoRandomForest](https://github.com/joaovbdss69/Prediction-csgo/blob/main/reports/figures/MatrizConfusaoRandomForest.png)



  ### Rede Neural



## Organização do Projeto 🛠️

Foi utilizado para construção da estrutura inicial o <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">Cookiecutter</a>, onde ele propoe uma estrutura lógica e flexivel para trabalhos de Data Science. O mesmo cria um projeto com a estrutura abaixo: 
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
  
