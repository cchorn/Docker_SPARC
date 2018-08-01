# use Ubuntu 18.04 base image (stepped up from 16.04)
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
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

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

# Install python3 and pip package manager
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Install nodejs for Jupyter lab extensions
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN sudo apt-get install -y build-essential
RUN npm install -g yarn

# Install python3 packages
RUN pip3 install jupyter pandas numpy matplotlib neo h5py ggplot jupyter_contrib_nbextensions ipywidgets scipy notedown statsmodels seaborn plotly bokeh scikit-image scikit-learn

# Install Jupyterlab and extensions
RUN pip3 install jupyterlab
RUN jupyter labextension install @jupyterlab/toc jupyterlab_bokeh @jupyterlab/plotly-extension @jupyterlab/github

# Install python 2.7 and pip package manager
RUN apt-get install -y python2.7 python-pip
RUN sudo -H pip2 install --upgrade pip
RUN pip install pandas numpy matplotlib neo h5py ggplot scipy statsmodels seaborn ipykernel pybursts blackfynn plotly

# Install R
RUN apt-get install -y r-base r-base-dev

# Install rpy2 version 2.8.5; note: version in pip is ahead of the R version and does not work
RUN pip3 install rpy2==2.8.5
RUN pip install rpy2==2.8.5

# Set default R CRAN repo
RUN echo 'options("repos"="http://cran.rstudio.com")' >> /usr/lib/R/etc/Rprofile.site

# Install R kernel for Jupyter notebook
RUN Rscript -e "install.packages('devtools')"
RUN Rscript -e "devtools::install_github('IRkernel/IRkernel')"
RUN Rscript -e "IRkernel::installspec()"

# Install R Packages
RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('plyr')"
RUN Rscript -e "install.packages('reshape2')"
RUN Rscript -e "install.packages('dplyr')"
RUN Rscript -e "install.packages('tidyr')"
RUN Rscript -e "install.packages('psych')"
RUN Rscript -e "install.packages('pwr')"
RUN Rscript -e "install.packages('STAR')"
RUN Rscript -e "install.packages('ez')"
RUN Rscript -e "install.packages('bursts')"

# Configure Jupyter notebook
RUN jupyter notebook --generate-config && \
    ipython profile create
RUN echo "c.NotebookApp.ip = '*'" >>/root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >>/root/.jupyter/jupyter_notebook_config.py && \
echo "c.InteractiveShellApp.matplotlib = 'inline'" >>/root/.ipython/profile_default/ipython_config.py

# install notebook kernel for Python 2.7
RUN python2 -m pip install ipykernel
RUN python2 -m ipykernel install --user

# Install Jupyter notebook extensions
RUN jupyter contrib nbextension install --system

# Run the Jupyter notebook (comment out 1st command that runs the traditional notebook)
# CMD jupyter notebook --notebook-dir=/home --allow-root
CMD jupyter lab --allow-root

WORKDIR /home
RUN pwd

# Expose port to host
EXPOSE 8888
