pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "✅ Build triggered by GitHub commit!"
                // Add your Python build/test commands here
                sh 'python3 --version'
                sh 'echo "You can add pytest or other commands here"'
            }
        }
    }
}
