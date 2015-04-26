# Pikka Bird Server (Python)

[![Build Status](https://travis-ci.org/tiredpixel/pikka-bird-server-py.png?branch=master,stable)](https://travis-ci.org/tiredpixel/pikka-bird-server-py)

Pikka Bird ops monitoring tool Server component.

Pikka Bird Server provides an API to which [Pikka Bird Collector][collector]
sends metrics reports, storing in a [PostgreSQL][postgresql] database. Pikka
Bird Server is a [Python][python] [Flask][flask] application.

One of the design goals of Pikka Bird is to enable production-suitable setup in
a minimum of steps and configuration. To support this, Pikka Bird Server uses
[Gunicorn][gunicorn] to provide concurrent request workers. Other setups can be
used if preferred, however.

Pikka Bird is currently in a draft phase, which means that payloads and schemas
might be changed in a backwards-incompatible fashion. Although it is unlikely,
in extreme cases this could require you to reinstall with an empty database. If
this upsets you too much, please wave and come back later. :) Currently, it is
not recommended that you use Pikka Bird as a replacement for any of your usual
monitoring tools.

Pikka Bird Server can currently only collect metrics and store them in the
database. There is no serving metrics via the API, no aggregation, no reporting, 
no alerting -- you get the idea. :)

More sleep lost by [tiredpixel](https://www.tiredpixel.com/).


## Installation

Install the following externals:

- [Python][python]
  
  The default version supported is defined in `.python-version`. Any other
  versions supported as defined in `.travis.yml`.

- [PostgreSQL][postgresql]
  
  This is specific dependency, as extensive use is made of PostgreSQL-specific
  functionality which may not be available in other databases.

Install using [Pip][pip]:

    pip install pikka-bird-server

There are currently no released server packages (stay tuned).

Migrate the database:

    bin/pikka-bird-server -c database-migrate


## Usage

To run the API:

    bin/pikka-bird-server

Run [Pikka Bird Collector][collector].

Look at your database. :P

Help is at hand:

    bin/pikka-bird-server -h


## Development

Copy the example configuration for development, adjusting to taste:

    cp .env.example .env

Copy the example configuration for testing, adjusting to taste, adding the
environment variable `CI=true` (the tests are destructive to the database):

    cp .env.example .test.env

Install locally using [Pip][pip] editable mode:

    pip install -r requirements.txt
    pip install -e .

Start a server using [Honcho][honcho], which reads `Procfile`:

    honcho start

Run the tests, which use [py.test][py_test]:

    honcho run -e .test.env py.test


## Stay Tuned

We have a [Librelist][librelist] mailing list!
To subscribe, send an email to <pikka.bird@librelist.com>.
To unsubscribe, send an email to <pikka.bird-unsubscribe@librelist.com>.
There be [archives](http://librelist.com/browser/pikka.bird/).

You can also become a
[watcher](https://github.com/tiredpixel/pikka-bird-server/watchers)
on GitHub. And don't forget you can become a
[stargazer](https://github.com/tiredpixel/pikka-bird-server/stargazers)
if you are so minded. :D


## Contributions

Contributions are embraced with much love and affection! <3 Please fork the
repository and wizard your magic, preferably with plenty of fairy-dust sprinkled
over the tests. Then send me a pull request. :) If you're thinking about
working on something involved, it would be great if you could wave via the
issue tracker or mailing list; I'd hate for good effort to be wasted!

Do whatever makes you happy. We'll probably still like you. :)


## Blessing

May you find peace, and help others to do likewise.


## Licence

© [tiredpixel](https://www.tiredpixel.com/) 2015.
It is free software, released under the MIT License, and may be redistributed
under the terms specified in `LICENSE.txt`.


[collector]: https://github.com/tiredpixel/pikka-bird-collector-py
[flask]: http://flask.pocoo.org/
[gunicorn]: http://gunicorn.org/
[honcho]: https://github.com/nickstenning/honcho
[librelist]: http://librelist.com/
[pip]: https://pypi.python.org/pypi/pip
[postgresql]: http://www.postgresql.org/
[py_test]: http://pytest.org/latest/
[python]: https://www.python.org/
