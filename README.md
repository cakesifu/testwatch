# Nose watch

A script that watches files and re-runs tests with nose when files
have changed.

====================

## Must have

* use `pyinotify` to monitor files; **no polling**
* file changes events should be throttled
* don't need to learn any new cli arguments

## Nice to have

* stop and restart tests if a file changes while tests ar running
