# Testwatch

A script that watches files and re-runs tests when files
have changed.

## Installation

For now install from git with the following:
```bash
pip install -e git+git://github.com/cezar-berea/testwatch.git@master
```

## Running

```bash
testwatch --command py.test tests
```


====================

## TODO

### Must have

- [x] use `pyinotify` to monitor files; **no polling**
- [x] file changes events should be throttled
- [x] simple invocation: `testwatch --command <test runner invocation>`
- [ ] decent feedback and output messages

### Nice to have

- [ ] inclusion/exclusion of files to watch
- [ ] flexible configuration
- [ ] stop and restart tests if a file changes while tests ar running
- [ ] keyboard shortcuts for manualy restarting tests
