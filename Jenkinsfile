pipeline {
    agent {
        label 'jenkins-agent1'
    }
    environment {
        APP_NAME = "urotaxi"
        APP_VERSION= "1.0.0"
        DOCKER_USER="shoryasngh"
        DOCKER_PASS="Shorya@_1104"
        IMAGE_NAME="${DOCKER_USER}" "+/" + "${APP_NAME}"
        IMAGE_TAG="${APP_VERSION}-${BUILD_NUMBER}"
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
                git branch: 'main', credentialsId: 'github', url: ''
            }

         }
    }
}