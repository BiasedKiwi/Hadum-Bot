# Changelog

All notable changes to the bot will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unrealeased

## Added

-   streak system to the coinflip command

## Changed

-   fetch limit for memes. It is now at 100 posts rather than 200

## v0.5.5

## Added

-   logging

### Changed

-    Renovated the Help command

## v0.5.4

### Added

-   new CLI argument

### Changed

-   using bot_settings.Json and now uses config.ini

### Removed

-   install.sh

### Fixed

-   .env related issues
-   Background task issues

### Added

-   Buttons
-   A 'Clear' Alias to the purge command

## v0.2.0

### Added

-   Help command.
-   Missing space in successful cog message
-   More tests
-   Random Warning Messages
-   A masskick and massban command for when dealing with multiple users.
-   A new verbose output option: logs minor error messages in the console instead of silently ignoring them.
-   Added Docker Support

### Changed

-   Progress bar in favor of a status bar in the loading animation.
-   Error handler to be compatible with the new output system

### Fixed

-   Ban and Kick command
-   Issue where username of banned user would not be displayed correctly to the user
-   Issue where importing from `utils` directly would not work
-   Conversion error when converting to int with the `kick` command

### Removed

-   Wikipedia auto response.

### Deprecated

-   Install using install.sh
