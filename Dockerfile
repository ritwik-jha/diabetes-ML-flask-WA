FROM centos:7

COPY (path_to_this_directory)  /root/code

CMD python3 /root/code/app.py
