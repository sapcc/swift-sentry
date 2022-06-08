# Archived project. No maintenance.

This project is not maintained anymore and is archived.

# Swift Sentry

This repo provides Sentry integration for Openstack [Swift](https://github.com/openstack/swift)
through a [custom log handler](https://docs.openstack.org/swift/latest/admin_guide.html#custom-log-handlers).

## Installation

```
pip install git+https://github.com/sapcc/swift-sentry
```

## Usage

Configure the Sentry DSN through the `SENTRY_DSN` environment variable:

```sh
export SENTRY_DSN='https://<key>@sentry.io/<project>'
```

Add the Swift Sentry configuration options under the `[Default]` section of the
specific service's config file for which you want to integrate Sentry. e.g.
`proxy-server.conf`, `object-expirer.conf`, `account-server.conf`, etc.

A minimal complete configuration looks like this:

```
log_custom_handlers = swift_sentry.sentry_logger
sentry_ignore_loggers = ignore_this_logger, and_this_logger
```

### Configuration Options

| Option | Required | Description |
| --- | --- | --- |
| `log_custom_handlers` | yes | Add `swift_sentry.sentry_logger` to this config option. Refer to Swift's [documentation](https://docs.openstack.org/swift/latest/admin_guide.html#custom-log-handlers) for more info regarding custom log handler hooks. |
| `sentry_ignore_loggers` | no | A comma-separated list of loggers for Sentry to [ignore](https://docs.sentry.io/platforms/python/logging/#ignoring-a-logger). |
