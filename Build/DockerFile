FROM fedora
RUN dnf -y install git
RUN dnf -y install make
RUN dnf -y install python3.8
RUN dnf -y install python3-pip
RUN dnf -y install graphviz
RUN dnf -y install pytest
RUN dnf -y install python3-tkinter
RUN pip install graphviz
RUN git clone https://github.com/Damian21sz/BOIL.git
WORKDIR /BOIL
RUN make .
