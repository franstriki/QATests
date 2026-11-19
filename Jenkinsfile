pipeline {
    agent any

    stages {
        stage('1. Descargar Código') {
            steps {
                // Descarga automáticamente la rama desde el repositorio configurado en Jenkins
                checkout scm
            }
        }


        stage('2. Instalar Dependencias') {
            steps {
                bat '''
                    "C:\Users\franc\AppData\Local\Programs\Python\Python313\python.exe" -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('3. Ejecutar Pruebas QA') {
            steps {
                // Ejecuta Pytest y genera un reporte HTML
                bat '''
                    call venv\\Scripts\\activate
                    python -m pytest -v --html=reporte.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            // Guarda el reporte HTML en Jenkins al terminar (falle o pase la prueba)
            archiveArtifacts artifacts: 'reporte.html', allowEmptyArchive: true
        }
    }
}