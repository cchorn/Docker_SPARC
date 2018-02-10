# What is Docker?
Docker is a software system that uses containers. Containers are isolated user-defined instances that operate as separate computers and have various levels of restricted access to the host computer's resources (e.g., shared folders). More than one container can run simultaneously on a host, communicating with the host and other containers.

A "Docker image" is analogous to an executable file, which contains multiple applications, compared to a "Docker container," which is a running instance of the image.

# Advantages of Docker:
There are two significant advantages when using Docker images for science projects:
#### 1. Easy installation.
Docker can GREATLY reduce the time (and expertise) needed to install, run, and maintain software, especially analytic software using Python, R, and other open source resources, such as [Jupyter notebooks](https://jupyter.org/); Jupyter runs in an internet browser to provide access to multiple [programming kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) and is a good way to store notes and analyses to make them reproducible/shareable. A stockpile of pre-built Docker images are available for download from [Docker Hub](https://hub.docker.com/); Docker Hub is cloud service similar to Github but designed to maintain Docker images, which can require gigabytes of storage.
#### 2. Reproducible/shareable software environments.
By producing a Docker image, subsequent users can run the original versions of the software used for scientific data analyses.

# How to get started with Docker:
Docker can run on on Windows, OSX, and Linux. Installation of Docker on Windows and OSX comes with a lightweight Linux virtual environment. To get started, follow these steps:
### 1. Install Docker ...
for [Windows](https://docs.docker.com/docker-for-windows/install/), [OSX](https://docs.docker.com/docker-for-mac/install/), or some flavor of Linux, [Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/), [Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian/), [CentOS](https://docs.docker.com/engine/installation/linux/docker-ce/centos/), and [Fedora](https://docs.docker.com/engine/installation/linux/docker-ce/fedora/). You only need the free community edition of Docker.
### 2. Get a free Docker ID ...
by going to [Docker cloud](https://cloud.docker.com/). This will allow sign-in to the cloud service to download and search for Docker images.

# Basic Docker commands:
You can walkthrough the official [Docker tutorial](https://docker-curriculum.com/), which explains basic commands and provides test images, such as "Hello World." There is also a command [cheatsheet](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf).

Here are frequently used commands for the terminal:

*... to list all installed docker images use ...*
```
docker images
```
*... to list running and stopped containers use ...*
```
docker ps -a
```
*... to run a container from the image named "ubuntu" (this could be a different image; notice the lack of flags for sharing folders or ports between the container and host computer, more about this later) ...*
```
docker run ubuntu
```
# What's in the Docker image?
The image is loaded with analytical software, including:

* ***[Python 3.5](https://www.python.org/downloads/)***   
Python is a high-level interpreted general-purpose programming language. Python 3.5 is the base version of Python in the image. Entering "python" in the container's terminal will start Python 3.5 in the terminal.

* ***[Python 2.7](https://www.python.org/downloads/)***    
Entering "python2" in the terminal will start Python 2.7. Python 2 provides access to a multitude of older Python software.

* ***[R 3.4.3](https://www.r-project.org/)***    
R is a software environment for statistical computing and graphics.

* ***[Jupyter](https://jupyter.org/) and add-ons***   
[Jupyter notebook extensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/) (extensions to notebook functions, e.g., auto table of contents, spellchecker, scratchpad, convert Python 2 to 3)    
[ipywidgets](https://ipywidgets.readthedocs.io/en/stable/index.html)  (interactive HTML widgets for Jupyter notebooks)    

* ***Python packages:***   
[numpy](http://www.numpy.org/) (numerical arrays), Python 2 & 3  
[pandas](https://pandas.pydata.org/) (dataframes and numerical analysis), Python 2 & 3    
[scipy](https://www.scipy.org/scipylib/index.html) (efficient numerical routines), Python 2 & 3       
[matplotlib](https://matplotlib.org/) (plotting), Python 2 & 3    
[ggplot](http://ggplot.yhathq.com/) (plotting; a Python port of the popular R ggplot2 package), Python 2 & 3       
[seaborn](https://seaborn.pydata.org/)  (statistical data visualization built on top of matplotlib), Python 2 & 3    
[statsmodels](http://www.statsmodels.org/stable/index.html) (statistics), Python 2 & 3    
[rpy2](https://rpy2.readthedocs.io/en/version_2.8.x/) (interface between Python and R) Python 2 & 3    
[h5py](http://www.h5py.org/) (binary data storage in HDF5 format), Python 2 & 3    
[neo](http://neuralensemble.org/neo/) (electrophysiology data conversion), Python 2 & 3   
[notedown](https://github.com/aaren/notedown) (tool for converting R markdown files to Jupyter notebooks), Python 3     
[pybursts](https://github.com/rpoddighe/pybursts) (algorithm to detect activity bursts in time series data; Python implementation of the R "bursts" package), Python 2

* ***R packages:***    
[dplyr](http://dplyr.tidyverse.org/) (dataframe manipulation)    
[plyr](https://cran.r-project.org/web/packages/plyr/index.html) (dataframe manipulation)    
[reshape2](https://cran.r-project.org/web/packages/reshape2/index.html) (dataframe manipulation)    
[tidyr](https://cran.r-project.org/web/packages/tidyr/) (data tidying)      
[ggplot2](http://ggplot2.org/) (plotting)    
[pwr](https://cran.r-project.org/web/packages/pwr/) (power analysis)       
[psych](https://cran.r-project.org/web/packages/psych/) (among many things this package has convenient data summary stats functions)    
[ez](https://cran.r-project.org/web/packages/ez/) (analysis and visualization of factorial experiments)     
[STAR](https://cran.r-project.org/web/packages/STAR/index.html) (Spike Train Analysis with R)   
[bursts](https://cran.r-project.org/web/packages/bursts/index.html) (algorithm to detect activity bursts in time series data)

* ***sample Jupyter notebook:***
The file "Sample_Notebook.ipynb" contains code to check the installed Python and R packages and shows how to use the "rpy2" package to create a bridge from Python to R in a notebook running Python kernel. Usage note: you can use an [ipython magic command](http://ipython.readthedocs.io/en/stable/interactive/magics.html?highlight=magic#) to run Python 2 code in a notebook cell running a Python 3 kernel (or vice versa) but there is no easy way to pass data and variables outside this cell. I would recommend using Python 2 and Python 3 as separate notebooks and passing data using  [storemagic](https://ipython.org/ipython-doc/rel-0.12/config/extensions/storemagic.html)

* ***Customization.*** You can also install additional Python and R (and OS) packages in the container using standard terminal commands, e.g., "pip" commands for python 2, "pip3" commands for python 3; you'll need to "commit" these software changes to a new image to save.

A Dockerfile used to create the image is included in this Github repository [1], but you DO NOT need to create the image. This is time consuming and depending on computer speed could easily exceed 15 min. Instead, you can ***download the pre-built image from Docker Hub (see below) and begin working on data analysis immediately!***

# How to use the Docker image
First, download the image (a small 2.7 GB) by entering this command in the terminal:
```
docker pull cchorn/sparc:jupyter_V1.1
```
Next, enter the following command:
```
docker run --rm -it -p 8888:8888 -v ~/Desktop:/home/work cchorn/sparc:jupyter_V1.1
```
The "docker run" command starts a container based on an image, in this case "cchorn/sparc:jupyter_V1.1". The command also contains three flags:
* "-it" = interactive terminal, which will keep the container running in the terminal until you close it.
* "-p" = port mapping from the host port on the left and container port on the right of the ":". This means that when the Jupyter server runs on port 8888 in the container it will map to port 8888 on the host, i.e., you can go to this port in the host's web browser URL address and see the Jupyter notebook.
* "-v" = volume (folders) mapping from host to container, in this case the container will be able to see the host's "desktop" folder from the container's "work" folder; the host's folder name should be customized for your computer.

Note: the "--rm" flag will cause automatic deletion of stopped containers. If you intend to make software changes and save a new image you need to remove this flag before running the container.  

After entering the "run" command a URL will be generated (http://localhost:8888/ + a security token). Copy the URL to your browser to see the Jupyter notebook directory! From here, you can create new notebooks using Python and R kernels and access the container's command-line terminal in the host browser (menu button on far right). New notebooks and files you create will be saved to your host machine folder mapped with the "docker run" command. Any documents that you want to save must be stored in the "work" directory on the container, which is mapped to volume on your host computer (see above; the "-v" flag). On some host machine (e.g. Windows 7), you will need to determine the ip address of the running container and use this instead of "localhost" (e.g., [docker-machine ip](https://docs.docker.com/machine/reference/ip/))

The running container can be stopped by entering ctrl+C in the host's terminal. If you ran Docker without the "--rm" flag, you can now see the exited container in the container list by entering:
```
docker ps -a
```
A container can be removed using the command:
```
docker rm [container name]
```
The "container name" is a name generated by Docker, found at the end of each entry in the container list.

Alternatively, if you made software changes, you can save the container as a new image using the "commit" command. Please see the [Docker tutorial](https://docker-curriculum.com/).

# Other resources:
* [Jupyter tutorial](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)
* [Official Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)
* [Unix shell commands](http://swcarpentry.github.io/shell-novice/), from Software Carpentry
* [list of Python tutorials](https://wiki.python.org/moin/BeginnersGuide/Programmers)
* [Quick R](https://www.statmethods.net/), a beginner friendly place to learn R programming
* [PyPI - the Python Package Index](https://pypi.python.org/pypi), search for a package in the archive of > *129,000* packages and growing!
* [R package list by name](https://cran.r-project.org/web/packages/available_packages_by_name.html), there are > *12,000* packages! The R project site does not have a search function but you can use [Rseek](https://rseek.org/)

# Future plans for the base image:
* include example notebooks:  (1) show how to work with both Python 3 and Python 2; (2) graphing with matplotlib, seaborn, and ggplot2; and (3) statistics
* include specific neurophysiology packages for viewing, spike detection, clustering, etc.
* other suggests welcome!

[1] To build the docker image from the Dockerfile run the following command from the Dockerfile folder:
```
docker build --tag cchorn/sparc:jupyter_V1.1 .
```

---------------------

##### *Acknowledgements: This work was supported by awards from the National Institutes of Health (NIH) - Stimulating Peripheral Activity to Relieve Conditions ([SPARC](https://commonfund.nih.gov/Sparc/)) Program, including these projects:*
##### 1. *Defining gastric vagal mechanisms underlying emetic activation using novel electrophysiological and optical mapping technology. [3U18EB021772-02S2](https://projectreporter.nih.gov/project_info_description.cfm?aid=9533820&icde=37670422&ddparam=&ddvalue=&ddsub=&cr=2&csb=default&cs=ASC&pball=).*
##### 2. *Closed-loop neuroelectric control of emesis and gastric motility [1U18TR002205-01](https://projectreporter.nih.gov/project_info_description.cfm?aid=9405061&icde=37670484&ddparam=&ddvalue=&ddsub=&cr=5&csb=default&cs=ASC&pball=)*     

---------------------

###### *MIT license*

###### *Copyright (c) 2018 Charles Horn*

###### *Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:*

###### *The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.*

###### *THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*
