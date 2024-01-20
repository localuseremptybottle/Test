pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                script {
                    git branch: 'Main', url: 'https://github.com/localuseremptybottle/Test'
                }
            }
        }

        stage('Run Api Test') {
            steps {
                script {
                    powershell 'pip3 install -r requirements.txt'
                    powershell 'pytest --alluredir=reports'
                }
            }
        }

        stage('Report Publish') {
            steps {
                script {
                    allure includeProperties: false, jdk: '', results: [[path: 'reports']]
                }
            }
        }
    }
}
