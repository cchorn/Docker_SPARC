# What is Docker?
Docker is a software system that uses containers. Containers are isolated user-defined instances that operate as separate computers and have various levels of restricted access to the host computer's resources (e.g., shared folders). More than one container can run simultaneously on a host, communicating with the host and other containers.

A Docker container is a running instance of the Docker image.

# Advantages of Docker:
There are two significant advantages when using Docker images for science projects:
#### 1. Easy installation.
Docker GREATLY reduces the time (and expertise) needed to install, run, and maintain software, especially analytic software using Python, R, and other open source resources, such as [Jupyter notebooks](https://jupyter.org/); Jupyter runs in an internet browser to provide access to multiple [programming kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) and is a good way to store notes and analyses for sharing and reproduction. A stockpile of pre-built Docker images are available for download from [Docker Hub](https://hub.docker.com/); Docker Hub is a cloud service similar to Github but designed to maintain Docker images.
#### 2. Reproducible/shareable computing environments.
By using and sharing a specific Docker image for analysis, subsequent users can run the original versions of the software and recreate the analysis or extend the work to new problems.

# How to get started using Docker:
Docker can run on Windows, macOS, and Linux. Installation of Docker on Windows and macOS comes with a lightweight Linux virtual environment. Follow these installation steps:
### 1. Install Docker ...
for [Windows](https://docs.docker.com/docker-for-windows/install/), [macOS](https://docs.docker.com/docker-for-mac/install/), or populars flavor of Linux, [Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/), [Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian/), [CentOS](https://docs.docker.com/engine/installation/linux/docker-ce/centos/), and [Fedora](https://docs.docker.com/engine/installation/linux/docker-ce/fedora/). You need the free community edition of Docker.
### 2. Get a free Docker ID ...
Go to [Docker cloud](https://cloud.docker.com/) to sign-up. This will allow sign-in to the cloud service to download and search for Docker images.

# Basic Docker commands:
You can walk through the official [Docker tutorial](https://docker-curriculum.com/), which explains basic commands and provides test images. There is also a command [cheatsheet](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf).

Here are frequently used commands used at the terminal to see which docker images you have installed, those currently running, and how to run a new one:

*To list installed docker images on your local machine ...*
```
docker images
```
*To list running and stopped containers ...*
```
docker ps -a
```
*To run a container from an image (you can add flags to this command, such as shared folders and ports between the container and host computer; more about this later) ...*
```
docker run [image name]
```
# What's in the SPARC supplied Docker image?
The "sparc:jupyter_V.9" image runs ***[Ubuntu 18.04 Linux](https://wiki.ubuntu.com/Releases)*** distribution with the following analytic software:    
***NOTE: To maintain compatibility, some software is kept at slightly less than the current version; also, the list of R packages is short to reduce the size of the docker image, additional packages can be installed and a new Docker image can be saved to meet the needs of each user.***

* ***[Python 3.6.9](https://www.python.org/downloads/)***   
Python is a high-level interpreted general-purpose programming language. Entering the command "python" in the container's terminal will start Python 3 on the command line.

* ***[R 3.4.4](https://www.r-project.org/)***    
R is a software environment for statistical computing and graphics. Entering "R" on the command line starts R from the terminal.

* ***[Ruby 2.5.1p57](https://www.ruby-lang.org/en/)***    
A dynamic, open source programming language with a focus on simplicity and productivity. 

* ***[Jupyter notebook 6.0.3](https://jupyter.org/)***   
Jupyter notebook is an open-source web browser application platform (this can run on your local machine or by logging into a server) to create notebooks containing text notes, programming code, and graphics, which are shareable. Typical usage for these notebooks is to run Python code but many other languages can also be used, including R and Ruby.  

* ***[Jupyter lab 1.2.6](https://jupyterlab.readthedocs.io/en/stable/index.html)***    
Jupyter lab is a new interface for Jupyter notebooks (it does still support using notebooks in the traditional way; i.e., one notebook per browser tab). The Jupyter lab interface greatly increases functionality by providing a file browser,  many cutting-edge extensions, and the ability to a make panels in a single browser tab (e.g., a terminal, notebook, images all side-by-side). 

* ***[JupyterLab extensions](https://github.com/topics/jupyterlab-extension)***    
Several Jupyter lab notebook extensions are included, with others available through installation (https://github.com/topics/jupyterlab-extension). The installed extensions include:    
*---git---* 
[github](https://github.com/jupyterlab/jupyterlab-github) (file browser for github repos)      
[git](https://github.com/jupyterlab/jupyterlab-git) (version control)       
*---file type viewers---* 
[html](https://github.com/mflevine/jupyterlab_html)         
*---graphics---*   
[drawio](https://github.com/QuantStack/jupyterlab-drawio) (a vector drawing program)    
*---file management---*      
[Pyhon file creation](https://github.com/jtpio/jupyterlab-python-file)    
[google drive](https://github.com/jupyterlab/jupyterlab-google-drive) (google drive collaboration)    
*---sidebar extensions---*  
[table of contents](https://github.com/jupyterlab/jupyterlab-toc) (table of contents for Jupyter notebooks)

* ***Python packages:***    
*---numerical manipulations and dataframes---*   
[numpy](http://www.numpy.org/) (numerical arrays), Python 3  
[pandas](https://pandas.pydata.org/) (dataframes and numerical analysis), Python 3    
[scipy](https://www.scipy.org/scipylib/index.html) (efficient numerical routines), Python 3     
*---plotting and visualizations---*   
[matplotlib](https://matplotlib.org/) Python 3    
[ggplot](http://ggplot.yhathq.com/) (a Python port of the popular R ggplot2 package), Python 3       
[seaborn](https://seaborn.pydata.org/) (statistical data visualization built on top of matplotlib), Python 3    
[plotly](https://plot.ly/python/) Python 3    
[bokeh](https://bokeh.pydata.org/en/latest/) Python 3    
[altair](https://altair-viz.github.io) Python 3     
*---statistics and machine learning---*   
[statsmodels](http://www.statsmodels.org/stable/index.html) (statistics), Python 3  
[scikit-learn](http://scikit-learn.org/stable/) (machine learning), Python 3     
*---image analysis---*   
[scikit-image](https://scikit-image.org) Python 3    
*---electrophysiology---*   
[neo](http://neuralensemble.org/neo/) (electrophysiology data conversion), Python 3     
*---misc---*   
[rpy2](https://rpy2.readthedocs.io/en/version_2.8.x/) (interface between Python and R), Python 3    
[h5py](http://www.h5py.org/) (binary data storage in HDF5 format), Python 3    
[notedown](https://github.com/aaren/notedown) (tool for converting R markdown files to Jupyter notebooks), Python 3  
[jupytext](https://github.com/mwouts/jupytext) (edit jupyter notebooks as plain text python files), Python 3  
[blackfynn](http://docs.blackfynn.io/clients/python/index.html#python-client) (API for interaction with the Blackfynn platform for data storage/analysis), Python 3
    

* ***R packages:***   
*---numerical manipulations and dataframes---*   
[dplyr](http://dplyr.tidyverse.org/) (dataframe manipulation)    
[plyr](https://cran.r-project.org/web/packages/plyr/index.html) (dataframe manipulation)    
[reshape2](https://cran.r-project.org/web/packages/reshape2/index.html) (dataframe manipulation)    
[tidyr](https://cran.r-project.org/web/packages/tidyr/) (data tidying)      
*---plotting and visualizations---*   
[ggplot2](http://ggplot2.org/) (plotting; based on the book "The Grammar of Graphics" by Leland Wilkinson, 2005)    
*---statistics---*   
[pwr](https://cran.r-project.org/web/packages/pwr/) (power analysis)       
[psych](https://cran.r-project.org/web/packages/psych/) (among many things this package has convenient data summary statistics functions)    
[ez](https://cran.r-project.org/web/packages/ez/) (analysis and visualization of factorial experiments)   
*---electrophysiology---*   
[STAR](https://cran.r-project.org/web/packages/STAR/index.html) (Spike Train Analysis with R)     
[bursts](https://cran.r-project.org/web/packages/bursts/index.html) (algorithm to detect activity bursts in time series data)


* ***Customization.*** You can install additional Python, R, and operating system packages in the container using standard terminal commands, e.g., "pip" command for python 3 and "install.packages()" in R command line; use "apt install" in the Linux terminal for Ubuntu packages. You will need to "commit" these software changes to a new image to save (see below).

The Dockerfile used to create the image is included in this repository, but you DO NOT need to create the image. This is time consuming and depending on the speed of your computer could easily exceed 15 min. Instead, you can ***download the pre-built image from Docker Hub (see below) and begin working on data analysis immediately!***

# How to use the Docker image
First, download the image by entering this command in the terminal on your host machine (do this after installing the Docker application on your computer):
```
docker pull cchorn/sparc:jupyter_V1.9
```
Next, enter:
```
docker run --rm -it -p 8888:8888 -v ~/Desktop:/home/work cchorn/sparc:jupyter_V1.9
```
The "docker run" command starts a container based on the image "cchorn/sparc:jupyter_V1.9". The command also contains three flags:    
1 - "-it", interactive terminal, which will keep the container running in the terminal until you close it.    
2 - "-p", port mapping from the host port on the left and container port on the right of the ":" in the command. This means that when the Jupyter server runs on port 8888 in the container it will map to port 8888 on the host, i.e., you can go to this port in the host's web browser URL address and see the Jupyter notebook.   
3 - "-v", volume (folders) mapping from host to container, in this case the container will be able to see the host's "Desktop" folder from the container's "work" folder; ***the host's folder name should be customized for your computer: please change "Desktop" to match a folder on your computer.***     
4 - "--rm" flag will cause automatic deletion of stopped containers (stop the running container by executing keystrokes "ctrl-c" in the terminal). *If you intend to make software changes and save a new image you need to remove this flag before running the container.*  

After entering the "docker run" command a URL will be generated (http://localhost:8888/ + a security token). Copy the URL to your browser to see the Jupyter notebook directory (also copy the security token and enter it if requested). On some host machines (e.g., Windows 7 and 8), you will need to determine the ip address of the running container and use this instead of "localhost" (e.g., [docker-machine ip](https://docs.docker.com/machine/reference/ip/)).        

**Success!** You should now see the Jupyter lab interface. From here, you can create notebooks using Python and R and access the container's command line terminal. New notebooks and files you create will be saved to your host machine folder mapped with the "docker run" command. Any documents that you want to save must be stored in the container's "work" directory, which is mapped to host's volume you specified using the "-v" flag. 

The running container can be stopped by entering keystrokes "ctrl-c" in the host's terminal. If you ran Docker without the "--rm" flag, you can now see the exited container in the container list by entering:
```
docker ps -a
```
A container can be removed using the command:
```
docker rm [container name]
```
The "container name" is a name generated by Docker, found at the end of each entry in the container list.

Alternatively, if you made software changes, you can save the container as a new image using the ["commit" command](https://docs.docker.com/engine/reference/commandline/commit/), for example:
```
docker commit [container name] [repository name:tag]
```
This new image will be loaded into the Docker image list on your local machine. To see the list use the "docker images" command. You can also backup the image to your Docker cloud account using the ["push" command](https://docs.docker.com/engine/reference/commandline/push/). And, this image can then be shared with the scientific community.    

# Other resources:
* [Jupyter tutorial](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)
* [Official Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)
* [Unix shell commands](http://swcarpentry.github.io/shell-novice/), from Software Carpentry
* [list of Python tutorials](https://wiki.python.org/moin/BeginnersGuide/Programmers)
* [a guide to Ruby](http://rubykoans.com/)
* [Quick R](https://www.statmethods.net/), a beginner friendly place to learn R programming
* [PyPI - the Python Package Index](https://pypi.python.org/pypi), search for a package in the archive of > *129,000* packages and growing!
* [R package list by name](https://cran.r-project.org/web/packages/available_packages_by_name.html), there are > *12,000* packages! The R project site does not have a search function but you can use [Rseek](https://rseek.org/) database.

If you wish to build the docker image from the Dockerfile run the following command from the Dockerfile folder (Note: downloading the pre-built image from Docker cloud is easier):
```
docker build --tag cchorn/sparc:jupyter_V1.9 .
```

---------------------

##### *Acknowledgements:
Derek Miller, University of Pittsburgh; testing Blackfynn API code   
Stephanie Fulton, University of Pittsburgh; testing Docker functionality   
Michael Sciullo, University of Pittsburgh; testing Docker functionality   

This work was supported by awards from the National Institutes of Health (NIH) - Stimulating Peripheral Activity to Relieve Conditions ([SPARC](https://commonfund.nih.gov/Sparc/)) Program, including these projects:*
##### 1. *Defining gastric vagal mechanisms underlying emetic activation using novel electrophysiological and optical mapping technology. [3U18EB021772-02S2](https://projectreporter.nih.gov/project_info_description.cfm?aid=9533820&icde=37670422&ddparam=&ddvalue=&ddsub=&cr=2&csb=default&cs=ASC&pball=).*
##### 2. *Closed-loop neuroelectric control of emesis and gastric motility [1U18TR002205](https://projectreporter.nih.gov/project_info_description.cfm?aid=9405061&icde=37670484&ddparam=&ddvalue=&ddsub=&cr=5&csb=default&cs=ASC&pball=)*     

---------------------

###### *MIT license*
###### *2020*

###### *Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:*

###### *The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.*

###### *THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*
