function weight = bal_read(s1)
%for i = 1:50
fprintf(s1,'IP');
str1=fscanf(s1,'%s');
str2=strtok(str1,'g');
weight = str2num(str2);
