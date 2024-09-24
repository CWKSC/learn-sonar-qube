docker run ^
    --rm ^
    --network=host ^
    -e SONAR_HOST_URL="http://localhost:9000" ^
    -v "C:\Develop\GitHub\learn-sonar-qube\cs5351-software-engineering-group-project-main:/usr/src" ^
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=local-project -Dsonar.token=sqp_eb35ab63a86ef63585563776d0cc2a644b9c2239" ^
    sonarsource/sonar-scanner-cli 

