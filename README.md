# Nose watch

A script that watches files and re-runs tests with nose when files
have changed.

====================

## Must have

* use `pyinotify` to monitor files; **no polling**
* file changes events should be throttled
* simple invocation: `nosewatch <nose args>`
* nice output messages

## Nice to have

* inclusion/exclusion of files to watch
* flexible configuration
* stop and restart tests if a file changes while tests ar running
* keyboard shortcuts for manualy restarting tests
