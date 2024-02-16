pipeline {
	agent any

	stages {
		stage('Quality Gate') {
			steps {
				withSonarQubeEnv('SQserver') {
					sh '/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner'
				}

				script {
					def qg = waitForQualityGate()
					if(qg.status != 'OK') {
						error "Quality Gate failure : ${qg.status}"
					}
				}
			}
		}

	        stage('List files') {
			steps {
				sh 'ls -lah .'
			}
		}
	}
}