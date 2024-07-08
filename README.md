This is a silly little project that I made as part of following along with Jeremy Howard's fast.ai Deep Learning for Coders MOOC. 

During the class, I used a pretrained resnet model as the basis for a binary classifier that predicts if an image contains a goth or a hipster. 

After I was done fitting the model to my data set in a Jupyter notebook I saved the weights of the model and reloaded them into a simple flask based web app that allows the user to upload a photo and find out which subcuture (goth or hipster) the model predicts it represents.

I've since learned a lot more about the low level functioning of CNNs, residual networks, transfer learning, and all the rest of the stuff going on unde the hood, but I still think this was a neat introduction to using a higher level deep learning library, and actually building a usable end to end system with a machine learning model as one of it's components. 
