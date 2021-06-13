# use Ubuntu 20.04 base image
FROM ubuntu:20.04

MAINTAINER cchorn "chorn@pitt.edu"

###############################################################################
#                      Global
###############################################################################

# run as root user
USER root
ENV DEBIAN_FRONTEND noninteractive

# Configure environment
ENV SHELL=/bin/bash \
    Notebook_USER=datawrangler \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

###############################################################################
#                      System
###############################################################################

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
    libzmq3-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    virtualenv \
    r-cran-nloptr \
    curl \
    # text editors
    nano \
    neovim \
    vim \
    # email support
    libio-socket-ssl-perl \
    libnet-ssleay-perl \
    sendemail

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

###############################################################################
#                      Python 3 packages
###############################################################################

# Install pip package manager
RUN apt-get update \
    && apt-get install -y python3-pip python3-dev python-setuptools libsndfile-dev

# Install python3 packages
RUN pip3 install \
    # early installs
    Cython \
    # jupyter packages
    jupyter \
    jupyterlab \
    jupyter_contrib_nbextensions \
    ipywidgets \
    jupyterlab-git \
    # plotting
    matplotlib \
    ggplot \
    seaborn \
    plotly \
    bokeh \
    altair \
    jupyter_bokeh \
    # machine learning
    scikit-learn \
    imbalanced-learn \
    XGBoost \
    # numerical and stats processing
    pandas \
    numpy \
    scipy \
    sympy \
    statsmodels \
    missingno \
    # misc
    h5py \
    scikit-image \
    neo

###############################################################################
#                      Jupyter lab extensions
###############################################################################

# Install nodejs for Jupyter lab extensions
# https://github.com/nodesource/distributions
RUN curl -sL https://deb.nodesource.com/setup_15.x | sudo -E bash -
RUN sudo apt-get install -y nodejs \
	&& apt-get clean \
	&& apt-get remove \
	&& rm -rf /var/lib/apt/lists/*

# Install yarn
RUN npm install -g yarn

RUN jupyter labextension install \
    # file managers and openers
    jupyterlab-python-file \
    # other extensions
    @jupyterlab/toc \
    jupyterlab-plotly \
    @jupyter-widgets/jupyterlab-manager \
    jupyter-matplotlib

###############################################################################
#                      R packages
###############################################################################

# Install R
RUN apt-get install r-base-dev \
	&& apt-get clean \
	&& apt-get remove \
	&& rm -rf /var/lib/apt/lists/*

# Set default R CRAN repo
RUN echo 'options("repos"="http://cran.rstudio.com")' >> /usr/lib/R/etc/Rprofile.site

# Install R Packages and kernel for Jupyter notebook
RUN Rscript -e "install.packages(c('devtools', 'ggplot2', 'plyr', 'reshape2', 'dplyr', 'tidyr', 'psych', 'pwr', 'STAR', 'ez', 'bursts'))"
RUN Rscript -e "install.packages('IRkernel')"
RUN Rscript -e "IRkernel::installspec()"

# Install rpy2 ... seems to only work if placed here, after R is installed
RUN pip3 install rpy2

###############################################################################
#                      Configure Jupyter notebook
###############################################################################

RUN jupyter notebook --generate-config && \
    ipython profile create
# TextFileContentsManager is needed to jupytext
RUN echo "c.NotebookApp.open_browser = False" >>/root/.jupyter/jupyter_notebook_config.py && \
    echo "c.InteractiveShellApp.matplotlib = 'inline'" >>/root/.ipython/profile_default/ipython_config.py && \
    echo "c.NotebookApp.contents_manager_class = 'jupytext.TextFileContentsManager'" >>/root/.jupyter/jupyter_notebook_config.py

# Run the Jupyter lab .. comment the first command because it is only for the notebook
CMD jupyter lab --allow-root --ip 0.0.0.0 --no-browser

###############################################################################
#                      Set directories and ports
###############################################################################

WORKDIR /home
RUN pwd

# Expose port to host
EXPOSE 8888
