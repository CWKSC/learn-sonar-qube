docker run ^
    --rm ^
    --network=host ^
    -e SONAR_HOST_URL="http://localhost:9000" ^
    -v "%cd%/src:/usr/src" ^
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=local-project -Dsonar.token=sqp_c27ba1d2c1351567667311ba3179ad0857adcb14" ^
    sonarsource/sonar-scanner-cli 

