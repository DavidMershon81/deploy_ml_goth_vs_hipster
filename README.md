This is a silly little project that I made as part of following along with Jeremy Howard's fast.ai Deep Learning for Coders MOOC. 

During the class, I used a pretrained resnet model as the basis for a binary classifier that predicts if an image contains a goth or a hipster. 

After I was done fitting the model to my data set in a Jupyter notebook I saved the weights of the model and reloaded them into a simple flask based web app that allows the user to upload a photo and find out if it contains a goth or a hipster. (Note - the jupyter notebooks where I train the model are not contained in this repo, only the saved weights, website code, and docker related stuff needed to actually deploy the project)

I've since learned a lot more about the low level functioning of CNNs, residual networks, transfer learning, and all the rest of the stuff going on under the hood, but I still think this was a neat introduction to using a higher level deep learning library because I was able to build a usable end to end system with a machine learning model as one of it's components. 

Besides the ML and full stack web aspects of this project, I was also able to learn enough about Docker to package everything up in a way that it is easily deployable on a container based VPS instance.
