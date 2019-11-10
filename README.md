# sanlap
The project is an attempt to provide an easy to train and use chat bots. Deploy and run your own if you don't want to use cloud based platforms

### Context
****
The project has been mainly split into 3 parts:
1. Training - This would train the model given a good corpus
2. Saving - Saves the model for reuse. It is versioned (configurable) per save.
3. Using - There are two ways to use the saved models

|Method|Description|
|------|---------|
|Simple Check|com/sanlap/bot/check/check_model.py|
|Run Service|com/sanlap/bot/service/server.py|
|And the Run Client|com/sanlap/bot/client/client.py|

### Train
You can train a model by running the below script:

***com/sanlap/bot/train/sanlap.py*** 

It takes in a configuration file as an argument which contains details about how the mmodel should be trained?

