docker container run ^
    --detach ^
    --hostname "python-preprocessor-container" ^
    --interactive ^
    --name "python-preprocessor-container" ^
    --privileged ^
    --rm ^
    --stop-timeout 0 ^
    --tty ^
    --volume "%cd%/workspace/:/workspace/" ^
    python-preprocessor-image

code --folder-uri vscode-remote://attached-container+707974686f6e2d70726570726f636573736f722d636f6e7461696e6572/workspace
