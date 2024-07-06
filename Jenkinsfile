pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('yuvalraif-dockerhub')
    }

    stages {
        stage('Checkout') {
            steps {
            git branch: 'main', credentialsId: 'bb4afcc2-ed4b-4bbc-93d9-eab81e06a0ad', url: 'https://github.com/yuval40/WorldOfGames.git'
            }


        stage('Build') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'yuvalraif-dockerhub', toolName: 'docker']) {
                        bat 'docker-compose -f docker-compose.yml up -d'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    dir('Tests') {
                        bat 'python e2e.py'
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'yuvalraif-dockerhub', toolName: 'docker']) {
                        bat 'docker-compose -f docker-compose.yml down'
                        bat 'docker tag worldofgames:wog yuvalraif/worldofgames:v1.0'
                        bat 'docker push yuvalraif/worldofgames:v1.0'
                    }
                }
            }
        }
    }
}