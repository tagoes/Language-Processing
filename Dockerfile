FROM python

RUN apt update
RUN pip install jupyterlab

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--LabApp.token=''"]

RUN pip install torch
RUN pip install numpy matplotlib
RUN pip install sklearn