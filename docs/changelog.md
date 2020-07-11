# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2020-07-11

### Added

- Automated deployment of docsify documentation with travis ci.

### Fixed

- `euchre play` - Properly rotate dealer one spot to the left after each hand
    instead of to the right.

## [0.3.0] - 2020-07-10

### Added

- `euchre play --watch` - Watch computers play a game of euchre amongst themselves.

### Changed

- `euchre play`
  - Human player (User) can now play a game of euchre with computers by default!
  - Regulate game output pace by default so that games are easier to follow!
  - Removed debug logs from game output.

### Fixed

- `euchre play` - No longer print that a user has proposed a trump suit when
    they have in fact passed.

## [0.2.0] - 2020-07-09

### Changed

- `euchre play`
  - Choose first dealer by first dealt Black Jack.
  - CPU player names are now randomized instead of hardcoded.
  - CPU players now make a more informed decision on whether to call pick up.
  - CPU players now discard their lowest value card after picking up.
  - CPU players now call trump if they have 3 or more cards of a suit in their hand.
  - Updated game print out formatting.

### Fixed

- `euchre play` - Discarded card is now added back to the deck after a player
    picks up.

## [0.1.0] - 2020-07-06

### Added

- `euchre play` - Four CPU players can successfully play a full game of euchre
    together, making random decisions (within the rules).
- `euchre --version` - Check current installed version.
- `euchre --help` - Print out cli usage.