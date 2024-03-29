pipeline {
    agent {
        label ' jenkins-agent1'
    }
    environment {
        APP_NAME = "urotaxi"
        APP_VERSION= "1.0.0"
        DOCKER_USER="shoryasngh"
        DOCKER_PASS= 'dockerhub'
        IMAGE_NAME="${DOCKER_USER}" + "/" + "${APP_NAME}"
        IMAGE_TAG = "${APP_VERSION}-${BUILD_NUMBER}"
        IMAGE_WITH_TAG="${IMAGE_NAME}" + ":" + "${IMAGE_TAG}"
        CONTAINER_NAME="mysql_db"
        MYSQL_USER= ""
        MYSQL_PASSWORD= ""
        MYSQL_DB= "urotaxi"
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
                    docker.withRegistry('',DOCKER_PASS){
                        docker_image=docker.build "${IMAGE_NAME}"
                        docker_image.push("latest")
                    }
                    // docker.withRegistry('',DOCKER_PASS){
                    //     docker_image.push("${IMAGE_WITH_TAG}")
                    //     // docker_image.push('latest')
                    // }
                    // sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                    // sh "python3 docker_login.py"
                    // sh "docker image push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
         }
        stage("Trivy Scan") {
           steps {
               script {
	            sh ('docker run -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image shoryasngh/urotaxi:latest --no-progress --scanners vuln  --exit-code 0 --severity HIGH,CRITICAL --format table')
               }
           }
       }
	   stage ('Cleanup Artifacts') {
           steps {
               script {
                    // sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "docker rmi ${IMAGE_NAME}:latest"
               }
          }
       }
         stage("run app with docker-compose"){
            steps {
                script {
                    sh "python3 install_docker-compose.py"
                    withCredentials([usernamePassword(credentialsId: 'mysqlcredentials', passwordVariable: 'MYSQL_PASSWORD', usernameVariable: 'MYSQL_USER')]){
                        writeFile file: 'env.list', text: "MYSQL_PASSWORD=${MYSQL_PASSWORD}\nMYSQL_USER=${MYSQL_USER}"
                        sh "docker-compose --env-file env.list up -d"
                        sh "docker cp src/main/db/urotaxidb.sql ${CONTAINER_NAME}:/"
                        // sh "cd src/main/db/"
                        // sh " docker exec -it ${CONTAINER_NAME} mysql -u {MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DB} < urotaxidb.sql"
                    }
                }
            }
         }
    }
}
