# Swift Sentry

This repo provides Sentry integration for Openstack [Swift](https://github.com/openstack/swift)
through a [custom log handler](https://docs.openstack.org/swift/latest/admin_guide.html#custom-log-handlers).

## Installation

```
pip install git+https://github.com/sapcc/swift-sentry
```

## Usage

A minimal complete configuration looks like this:

```
log_custom_handlers = swift_sentry.sentry_logger
sentry_dsn = https://<key>@sentry.io/<project>
sentry_ignore_loggers = ignore_this_logger, and_this_logger
sentry_log_level = ERROR
```

Add the Swift Sentry configuration options under the `[Default]` section of
some service's config file, e.g. `proxy-server.conf`, `object-expirer.conf`,
`account-server.conf`, etc.

### Configuration Options

| Option | Required | Description |
| --- | --- | --- |
| `log_custom_handlers` | yes | Add `swift_sentry.sentry_logger` to this config option. Refer to Swift's [documentation](https://docs.openstack.org/swift/latest/admin_guide.html#custom-log-handlers) for more info regarding custom log handler hooks. |
| `sentry_dsn` | no | DSN (Data Source Name) for your Sentry Project. If `sentry_dsn` is not specified then the DSN value is read from the `SENTRY_DSN` environment variable. If both are configured then the environment variable has priority. |
| `sentry_ignore_loggers` | no | A comma-separated list of loggers for Sentry to [ignore](https://docs.sentry.io/platforms/python/logging/#ignoring-a-logger). |
| `sentry_log_level` | no | Log records with a level higher than or equal to this value are sent to Sentry. This value defaults to `ERROR`. You may want to set this value if you also want to send `INFO` or `DEBUG` messages. |
