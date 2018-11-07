# use Ubuntu 18.04 base image
FROM ubuntu:18.04

MAINTAINER cchorn "chorn@pitt.edu"

# run as root user
USER root

ENV DEBIAN_FRONTEND noninteractive

# Install OS packages
# r-cran-nloptr is installed here because it is required for R package ez but will not install via R command line
RUN apt-get update && apt-get install -y \
    apt-utils \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    git \
    nano \
    libzmq3-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    virtualenv \
    r-cran-nloptr \
    curl 

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Configure environment
ENV SHELL=/bin/bash \
    Notebook_USER=datawrangler \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

# Copy example notebooks to tmp directory
COPY Jupyter_Notebooks/ /home/

# Install Python 3 packages
####################################################

# Install python3 and pip package manager
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip 

# Install python3 packages ... (only neo 0.5.2 will import Spike2 files)
RUN pip3 install jupyter jupyterlab pandas numpy matplotlib neo==0.5.2 h5py ggplot jupyter_contrib_nbextensions ipywidgets scipy notedown statsmodels seaborn plotly bokeh scikit-image scikit-learn sympy jupytext altair vega_datasets simplegeneric rpy2==2.8.5

# Install Python 2 and packages
####################################################

# Install python 2.7 and pip package manager ... an apt-get update is needed to configure the package manager
RUN apt-get update \
	&& apt-get install -y python2.7 python-pip 

RUN sudo -H pip2 install --upgrade pip

# Install python2 packages ... (only neo 0.5.2 will import Spike2 files)
RUN pip install pandas numpy matplotlib neo==0.5.2 h5py ggplot scipy statsmodels seaborn ipykernel pybursts blackfynn plotly jupytext rpy2==2.8.5

# Install Jupyter lab extensions
####################################################

# Install nodejs for Jupyter lab extensions
# https://github.com/nodesource/distributions
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN sudo apt-get install -y nodejs 

# Install yarn
RUN npm install -g yarn

# Install Jupyterlab extensions, commment out those not currently supported
RUN jupyter labextension install @jupyterlab/toc @jupyterlab/google-drive @jupyterlab/celltags jupyterlab_bokeh @jupyterlab/github qgrid @jupyter-widgets/jupyterlab-manager @jupyterlab/xkcd-extension @jupyterlab/git @jupyterlab/geojson-extension @jupyterlab/plotly-extension @mflevine/jupyterlab_html plotlywidget jupyterlab-drawio

# Install R and packages
####################################################

# Install R
RUN apt-get install r-base-dev \
	&& apt-get clean \
	&& apt-get remove \
	&& rm -rf /var/lib/apt/lists/*

# Set default R CRAN repo
RUN echo 'options("repos"="http://cran.rstudio.com")' >> /usr/lib/R/etc/Rprofile.site

# Install R Packages and kernel for Jupyter notebook
RUN Rscript -e "install.packages(c('devtools', 'ggplot2', 'plyr', 'reshape2', 'dplyr', 'tidyr', 'psych', 'pwr', 'STAR', 'ez', 'bursts'))"
RUN Rscript -e "devtools::install_github('IRkernel/IRkernel')"
RUN Rscript -e "IRkernel::installspec()"

# Configure Jupyter notebook
####################################################

RUN jupyter notebook --generate-config && \
    ipython profile create
# TextFileContentsManager is needed to jupytext
RUN echo "c.NotebookApp.open_browser = False" >>/root/.jupyter/jupyter_notebook_config.py && \
    echo "c.InteractiveShellApp.matplotlib = 'inline'" >>/root/.ipython/profile_default/ipython_config.py && \
    echo "c.NotebookApp.contents_manager_class = 'jupytext.TextFileContentsManager'" >>/root/.jupyter/jupyter_notebook_config.py

# install notebook kernel for Python 2.7
RUN python2 -m pip install ipykernel
RUN python2 -m ipykernel install --user

# Run the Jupyter lab .. comment the first command because it is only for the notebook
CMD jupyter lab --allow-root --ip 0.0.0.0 --no-browser

# set directories and ports
####################################################

WORKDIR /home
RUN pwd

# Expose port to host
EXPOSE 8888
