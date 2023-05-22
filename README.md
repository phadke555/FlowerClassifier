# Flower Classifier

This is a deep learning image classifier built using Python. I am using HuggingFace Spaces to host a web application for this model. A 'convnext_tiny_in22k' image model was used to classify 12 different types of flowers: 'sunflower','rose', 'orchid', 'gladiolus', 'dahlia', 'hydrangea', 'anemone', 'lily', 'tulip', 'daisy', 'carnation', 'daffodil'.

The Python Notebook with the creation of the model is included utilizing the FastAI, PyTorch, and Pandas libraries. An 'app.py' Python script is also included which includes the code to run the web application. 

The web app is hosted at this link: https://huggingface.co/spaces/rohanphadke/flowerclassifier. Input an image of your choice and it will return the class of the flower.

---
title: Flowerclassifier
emoji: 🦀
colorFrom: purple
colorTo: indigo
sdk: gradio
sdk_version: 3.28.3
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
