FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
    cron

RUN apt-get install sudo
#RUN sudo npm install npm@latest -g

#RUN apt-get install -y npm

#RUN \
#    cd /tmp && \
#    wget http://nodejs.org/dist/v8.5.0/node-v8.5.0.tar.gz && \
#    tar xvzf node-v8.5.0.tar.gz && \
#    rm -f node-v8.5.0.tar.gz && \
#    cd node-v* && \
#    ./configure && \
#    CXX="g++ -Wno-unused-local-typedefs" make && \
#    CXX="g++ -Wno-unused-local-typedefs" make install && \
#    cd /tmp && \
#    rm -rf /tmp/node-v* && \
#    npm install -g npm && \
#    echo -e '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/
ADD . /code/
RUN chmod 777 /code/start.sh
CMD ["/code/start.sh"]