# End to End Text_Summarizer_Project

## WorkFlow For Project building

1. Update config.yaml file
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update components
6. Update the pipeline
7. Update the main.py
8. update the app.py

## Work Flow for Deploying Project (AWS CICD With GitHUB Actions)
1. Login To AWS Consol
2. Create IAM user for deployment

    #with specific access:
    1. EC2 access: It is Virtual Machine
    2. ECR: Elastic Container to save your docker image in aws

    #Discription About the Deployment
    1. Build Docker image for the Source Code
    2. Push Your Image to ECR
    3. Launch Your EC2
    4. Pull Your Image from ECR in EC2
    5. launch your docker image in EC2

    #Policy
    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

3. Create ECR repo to store/save docker image
    #ECR url
    -url : 090334662463.dkr.ecr.ap-south-1.amazonaws.com/text_summarizer

4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
    #optinal
    sudo apt-get update -y
    sudo apt-get upgrade

    #required
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker

6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

7. Setup github secrets:

    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_REGION = ap-south-1
    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com
    ECR_REPOSITORY_NAME = text_summarizer

