# Docker(Container Technology)
The 2nd task given by IIEC-RISE to create a menu which can run Docker commands to launched and stop any Operating System.

# About the task
In this task we can give voice commands to launched or stop Operating System in Docker and it will open a Web Apllication accordingly.  

# What is Docker ?
   Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. It is a Container technology used to launched different Operating Systems in few seconds. It provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security allow you to run many containers simultaneously on a given host. We can even run Docker containers within host machines that are actually virtual machines,
    for example :- In RHEL 8 Operating System we can open other operating systems like ubuntu:14.04 and centos:7 by using docker.

# How it works?

=> First of all we have to run the python menu on IDLE, it will ask you for your voice command.

![](/Images/saying.png)

=> If you give a command to start or open docker it will take you to the Web Application where you can launched any operating system whoes image files availabel in select option.

![](/Images/start.png)

=> In this Web Application you have to first enter your Operating System (O.S) name and select the image file of your Operating System and than submit it.

![](/Images/start%20docker.png)

=> For example if you Enter C7 as a name of your O.S and select centos:7 image file and submit it.

![](/Images/input%202.png)

Than we get output as shown below:

![](/Images/C7%20launched.png)

It shows that centos:7 Operating System is launched in docker with C7 as a username.

=> And if you go to your linux (RHEL8) system and give "docker ps" command in terminal you can check how many Operating System is running in Docker.

![](/Images/output.PNG)

As you can see in above image centos:7 with username C7 is running in Docker.

=> And if you give a command to stop or quit docker it will take you to the Web Application where you can stop the running operating system in Docker.

![](/Images/stop.png)

=> Now you have to enter username to stop a particular Operating System and submit it. 

![](/Images/stop%20docker.png)

=> For example : if you enter C7 and submit it than we get output as shown below

![](/Images/C7%20stopped.png)

It shows that the Operating System with a username of C7 is successfully stopped. 
