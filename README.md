# Arabic Dialect Classification Project

## Overview
This project focuses on classifying Arabic dialects using Natural Language Processing (NLP) techniques. We implemented and compared three models: Logistic Regression, Long Short-Term Memory (LSTM) networks, and Gated Recurrent Unit (GRU) networks to determine which model performs best for this classification task.


## Dataset
The dataset consists of Arabic text samples labeled with their respective dialects. The data is stored in the `data/` directory, with subdirectories for raw and processed data. The preprocessing steps include tokenization, normalization, and vectorization.

## Models
### Logistic Regression
A baseline model using Logistic Regression, which serves as a simple and interpretable classifier for text data. The implementation can be found in `notebooks/Logistic_Regression.ipynb` and the corresponding script is `scripts/train_logistic_regression.py`.

### Long Short-Term Memory (LSTM)
An LSTM model, which is a type of recurrent neural network (RNN) capable of learning long-term dependencies. This model is more complex and can capture the sequential nature of the text data. The implementation can be found in `notebooks/LSTM_Model.ipynb` and the corresponding script is `scripts/train_lstm.py`.

### Gated Recurrent Unit (GRU)
A GRU model, another type of RNN similar to LSTM but with a different gating mechanism that can also capture long-term dependencies in sequences. The implementation can be found in `notebooks/GRU_Model.ipynb` and the corresponding script is `scripts/train_gru.py`.



### Evaluation
The results for each model, including accuracy, precision, recall, and F1-score, are obtained. Each subdirectory contains model-specific metrics and visualizations.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

