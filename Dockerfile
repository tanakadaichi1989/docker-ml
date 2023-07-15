FROM continuumio/anaconda3
RUN pip install keras tensorflow
WORKDIR /workspace
CMD jupyter-lab --no-browser --port=8888 --ip=0.0.0.0 --allow-root