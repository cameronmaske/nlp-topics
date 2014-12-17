FROM stackbrew/ubuntu:latest
RUN apt-get -y update
RUN apt-get install -y python python-dev python-pip
RUN apt-get install -y ant mercurial openjdk-7-jdk
RUN apt-get install -y libatlas3-base libatlas-base-dev
WORKDIR /temp/
RUN hg clone http://hg-iesl.cs.umass.edu/hg/mallet
RUN cd mallet; ant
RUN apt-get install -y libblas3gf libc6 libgcc1 libgfortran3 liblapack3gf libstdc++6 build-essential gfortran python-all-dev libatlas-base-dev
RUN apt-get install -y unzip

WORKDIR /code/
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install nltk
RUN python -m nltk.downloader -d /usr/share/nltk_data brown
RUN python -m nltk.downloader -d /usr/share/nltk_data reuters
RUN unzip /usr/share/nltk_data/corpora/reuters.zip -d /usr/share/nltk_data/corpora/

CMD python app.py