pipeline {
    agent {
        label ' jenkins-agent1'
    }
    environment {
        APP_NAME = "urotaxi"
        APP_VERSION= "1.0.0"
        DOCKER_USER="shoryasngh"
        DOCKER_PASS="Shorya@_1104"
        IMAGE_NAME="${DOCKER_USER}" + "/" + "${APP_NAME}"
        IMAGE_TAG="${BUILD_NUMBER}"
    }
    tools{
        jdk 'Java17'
        maven 'Maven3'
    }
    stages{
         stage("Clean workspace"){
            steps {
                cleanWs()
            }
         }
         stage("Checkout from SCM"){
            steps{
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/shorya1104/urotaxi.git'
            }

         }
         stage("Build application"){
            steps{
                sh "mvn clean verify"
            }
         }
         stage("Test Application"){
            steps {
                sh "mvn test"
            }
         }
         stage("Sonarqube Analysis"){
            steps {
                script {
                    withSonarQubeEnv(credentialsId: 'jenkins-sonarqube-token'){
                    sh "mvn sonar:sonar"
                    }
                }
            }
         }
         stage("Quality Gate"){
            steps {
                script {
                    waitForQualityGate abortPipeline: false, credentialsId: 'jenkins-sonarqube-token'

                }
            }
         }
         stage("Build & push docker image"){
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                    sh "chmod +x docker.sh"
                    sh "./docker.sh"
                    sh " sudo docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    // docker.withRegistry('',DOCKER_PASS){
                    //     docker_image = docker.build "{IMAGE_NAME}"
                    // }
                    // docker.withRegistry('', DOCKER_PASS){
                    //     docker_image.push(${IMAGE_NAME})
                    //     docker_image.push('latest')
                    // }
                }
            }
         }
    }
}
