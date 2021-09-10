FROM centos:latest
RUN yum install python3 -y
RUN pip3 install keras
COPY Student.csv /
COPY student.h5 /
COPY students.py /

ENTRYPOINT ["python3","/students.py"]

