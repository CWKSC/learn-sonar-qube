# learn-sonar-qube

## `api/issues/list`

- severity
- component
- project
- line
- textRange
- message

```json
{
    "severity": "CRITICAL",
    "component": "local-project:python-preprocessor/workspace/python_preprocessor/parsing/if_derivative_parser.py",
    "project": "local-project",
    "line": 15,
    "textRange": {
        "startLine": 15,
        "endLine": 15,
        "startOffset": 8,
        "endOffset": 13
    },
    "message": "Refactor this function to reduce its Cognitive Complexity from 48 to the 15 allowed.",
}

{
    "severity": "MAJOR",
    "component": "local-project:python-preprocessor/workspace/python_preprocessor/parsing/if_derivative_parser.py",
    "project": "local-project",
    "line": 90,
    "textRange": {
        "startLine": 90,
        "endLine": 92,
        "startOffset": 30,
        "endOffset": 25
    },
    "message": "Replace this generic exception class with a more specific one.",
}
```

## `api/components/app`

- measures
  - lines
  - coverage

```json
{
    "key": "local-project",
    "uuid": "6ff3323b-3ae7-4897-b59b-59108507e1bf",
    "name": "local-project",
    "longName": "local-project",
    "q": "TRK",
    "project": "local-project",
    "projectName": "local-project",
    "fav": false,
    "canMarkAsFavorite": true,
    "measures": {
        "lines": "540.0",
        "coverage": "0.0",
        "duplicationDensity": "0.0",
        "issues": "8.0"
    }
}
```




`api/projects` for project auto create delete 
