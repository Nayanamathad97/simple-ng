pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "nayanapreetham/flask"
        REGISTRY_CREDENTIALS = "nayanapreetham"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Builds the image using the Dockerfile in root
                    app = docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    // Authenticates and pushes image to Docker Hub
                    docker.withRegistry('', REGISTRY_CREDENTIALS) {
                        app.push("${env.BUILD_ID}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('Deploy Container') {
            steps {
                sh "docker stop sample-container || true"
                sh "docker rm sample-container || true"
                sh "docker run -d --name sample-container -p 5000:5000 ${DOCKER_IMAGE}:latest"
            }
        } 
    }
} 
